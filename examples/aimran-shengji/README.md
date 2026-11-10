# 动效货架实测：声记（录音转文字落地页）

v1.7 的独立验证单：给一个没有参与编写索引的 agent 出一道题——为虚构的「录音转文字」工具做一个单页落地页，动效只许从 `references/aimran-picks.md` 索引里取、至少 4 件，不许用索引外的现成件，也不许现编索引里已有的同类效果。

结果：约 7 分钟交活，用了 7 件（uv-btn-shine、uv-tx-marker-highlight、uv-btn-ripple、uv-tg-billing、uv-rd-plans、uv-ld-status-words、uv-toast-success），全部换成自定 tokens（原组件默认配色零残留），手机端触发按索引纪律处理，`prefers-reduced-motion` 全部保留。验收方直读代码 + 真浏览器复核：价格与分钟数数据自洽、390 宽无横滚、控制台零报错。执行者还反过来给索引挑出两处小毛病（某件的演示按钮 JS 绑定陷阱、某件原码是演示容器需改定位），已补进入选索引。

- `index.html` — 成品页，单文件可直接打开（在线版：https://lzwmt.com/aimran-test/ ）
- `mobile.png` — 390 宽真浏览器截图
- `REPORT.md` — 执行者自述：挑件清单、tokens 表、手机端处理、自查结果、索引问题
