#!/usr/bin/env python3
"""逐格密度校验：对成品 PNG 按 layout.json 声明的格子逐格量两个读数。

- ink：内容像素占格子面积的比例（与格内主导色差异超过阈值的像素）。
- bbox_fill：内容像素的外接矩形面积占格子面积的比例（内容摊得开不开）。

只写「是/通过」不算验收；关 5 的密度结论必须引用本脚本输出的 density.json 原文。
用法：python3 density_check.py <png> <layout.json> [density.json 输出路径]
layout.json 格式：
{"cells":[{"name":"逐字稿","x":0.34,"y":0.14,"w":0.32,"h":0.52,
            "min_bbox_fill":0.35,"min_ink":0.05}]}
坐标为相对整图的比例（0-1）。min_* 缺省时用 bbox_fill>=0.35、ink>=0.05。
退出码：全部 PASS 为 0，任一 FAIL 为 1，参数/文件错误为 2。
依赖：Pillow。
"""
import json
import sys
from collections import Counter

from PIL import Image

DEFAULT_MIN_BBOX_FILL = 0.35
DEFAULT_MIN_INK = 0.05
DIFF_THRESHOLD = 28  # 与主导色的欧氏距离超过此值算内容像素
STRIDE = 2           # 采样步长（速度与精度折中）


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    png_path, layout_path = sys.argv[1], sys.argv[2]
    out_path = sys.argv[3] if len(sys.argv) > 3 else "density.json"
    with open(layout_path, encoding="utf-8") as f:
        layout = json.load(f)
    im = Image.open(png_path).convert("RGB")
    W, H = im.size
    px = im.load()

    results = []
    all_pass = True
    for cell in layout["cells"]:
        x0 = int(cell["x"] * W)
        y0 = int(cell["y"] * H)
        x1 = int((cell["x"] + cell["w"]) * W)
        y1 = int((cell["y"] + cell["h"]) * H)
        # 主导色：采样格内像素取众数（按 16 级量化防抖）
        counts = Counter()
        for yy in range(y0, y1, STRIDE * 4):
            for xx in range(x0, x1, STRIDE * 4):
                r, g, b = px[xx, yy]
                counts[(r // 16, g // 16, b // 16)] += 1
        (qr, qg, qb), _ = counts.most_common(1)[0]
        bg = (qr * 16 + 8, qg * 16 + 8, qb * 16 + 8)
        total = 0
        ink = 0
        minx, miny, maxx, maxy = None, None, None, None
        for yy in range(y0, y1, STRIDE):
            for xx in range(x0, x1, STRIDE):
                total += 1
                r, g, b = px[xx, yy]
                d2 = (r - bg[0]) ** 2 + (g - bg[1]) ** 2 + (b - bg[2]) ** 2
                if d2 > DIFF_THRESHOLD * DIFF_THRESHOLD:
                    ink += 1
                    if minx is None or xx < minx:
                        minx = xx
                    if maxx is None or xx > maxx:
                        maxx = xx
                    if miny is None or yy < miny:
                        miny = yy
                    if maxy is None or yy > maxy:
                        maxy = yy
        ink_ratio = ink / total if total else 0.0
        if minx is None:
            bbox_fill = 0.0
        else:
            bbox_fill = ((maxx - minx) * (maxy - miny)) / float((x1 - x0) * (y1 - y0))
        min_bbox = cell.get("min_bbox_fill", DEFAULT_MIN_BBOX_FILL)
        min_ink = cell.get("min_ink", DEFAULT_MIN_INK)
        ok = bbox_fill >= min_bbox and ink_ratio >= min_ink
        all_pass = all_pass and ok
        results.append({
            "cell": cell["name"],
            "ink": round(ink_ratio, 3),
            "bbox_fill": round(bbox_fill, 3),
            "min_ink": min_ink,
            "min_bbox_fill": min_bbox,
            "verdict": "PASS" if ok else "FAIL",
        })

    report = {"image": png_path, "size": [W, H], "cells": results,
              "verdict": "PASS" if all_pass else "FAIL"}
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
