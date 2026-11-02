---
name: ui-workflow
description: >-
  当用户要为某个产品/项目新建或改版网页界面、做 UI 设计、改页面样式/版式，或要从真界面派生宣传静图、动画、Bento 时使用。按六关 UI 工作流执行（需求 Grill、出样选向、Design Tokens 锁定、单页实现（4a 真页面 + 4b 宣传物料）、截图与构图验收修改单循环、审查上线）。是总控流程，自己不做设计。不依赖特定厂商/agent，单 agent 亦可全程执行。
---

# UI 工作流总控

本技能是六关 UI 工作流的总控与调度，自己不做设计。Taste、UI UX Pro Max、Emil、Impeccable、Hallmark 为推荐配合（若环境已安装），仍按各自技能的触发工作；本技能只在对应关口点名调用，不把它们的步骤吞进总控，避免抢触发。未安装时按本技能 references 的对应口径直接执行。出样分工：默认由执行本技能的 agent 本人出样（自出）；可选把方向探索外包给本环境可用的其他 agent 或设计工具。

总控原则：做减返工。决定尽早锁死，把用户的活变成选择题。返工多不是 AI 不行，是前面没定死。先锁方向，再做页面；每次只改一类，不推倒重来。

执行者是执行本技能的 agent：追问、组织技能、派单、出对比、维护 tokens 与版本、截图验收、审查。用户只做选择题：答 5 题、选方向、确认锁定表、逐条提修改单、最终拍板上线。执行本技能的 agent 不替用户选风格、不擅自解锁、不覆盖母版。

## 六关速览

| 关 | 做什么 | 产物 | 过关条件 |
|---|---|---|---|
| 1 | 需求 Grill。先核现状，判定新建或改版，定产物类型（真页面 / 宣传物料 / 两者），答 5 题，写未来功能 UI 预留 | `brief.md` | 用户说清要什么。页面数、功能数以《现有功能清单》为准 |
| 2 | 先定 2–3 张标杆，再出 3 个方向，只做首屏，按 `composition.md` 摆。用户选 1 个，或组合选 | `explorations/` 下 benchmarks、vA、vB、vC + 对比截图 | 用户已选定。交付已经由复核者读到文件字节并校验通过 |
| 3 | 把选中方向锁成 Design Tokens（含展示档） | `design-tokens.md`（已批准版） | 用户确认锁定表 |
| 4 | 4a：做透 1 个真标杆页（母版），再复制组件与 tokens。4b（产物含宣传物料时）：用 4a 的组件、tokens、数据，在 Stageshow 画幅里出静图、动画、Bento | 4a 标杆页 + 组件清单；4b `promo/` 成品 | 用户确认标杆页。按钮、卡片、标题栏已是可复用组件。4b 产出后回关 3 重新提取对账 |
| 5 | 桌面 + 手机双截图验收 + 构图问答 + 数字反读，修改单循环 | `reviews/review-vN.md` | 回执和修改单逐条对得上。默认 2-3 轮；超了先判定方向错还是细节没完 |
| 6 | 审查后上线 | 审查结论。过关才部署 | Impeccable、Hallmark 已查（推荐配合，若环境已安装；未安装时按本技能 references 的对应口径直接执行），评审小测试过关。部署后公网打开实测一次 |

细则在 `references/gates.md`。进某一关之前先读该关，再按该关打开下面的参考。六关按顺序走。返工模板写明：跳过 1-2 直接做完整站 = 必然全站返工（这里的 1-2 指方向小样和锁定表）。

## 硬规矩

1. 阶段分界：关 1–3 是设计探索——样稿可由出样者直做、一次性、选后即弃、不进仓库；关 4 起才进真仓库，此后走该项目既有的开发与验收流程。本技能不重写该项目既有的开发与验收流程的步骤。
2. 和开发工作流的关系：这是该项目既有的开发与验收流程的 UI 专用轻量版。纯视觉页/个人站走本流程即可，不必上全套 accept。正式项目仍走 grill -> to-spec -> 验收清单。
3. 出样顺序：默认由执行本技能的 agent 本人出样（自出）。可选把方向探索外包给本环境可用的其他 agent 或设计工具。外包时简报须写明所用技能、自带 tokens 清单；交付以文件落盘可读为准，并做逐项自查、数据自洽。产出按交付判定通则严验。要比审美或用户点名时才多家同题，分别记录各家产出与结论。细则见 `references/sampling-and-vendors.md`。
4. 交付判定通则（所有出样者）：一切交付以文件落盘且可被复核者读到为准，不认口头声称。交付 = 复核者读到文件字节并校验通过（实读/md5），任何口头或文字「已交付」声称不算。外部样稿同样过 brief 逐项 + 数据自洽，「概念更丰富」不能抵规格缺失。
5. tokens：锁定后改 tokens 是全站变更，必须用户明确说「解锁改 X」，并在 `CHANGELOG-UI.md` 记一行。锁定源以复核者从样稿代码逐值提取的版本为准；出样者自带清单只作意图参考。两者差异逐条裁定，决定补充进锁定版的走 `CHANGELOG-UI.md` 留痕。字号、字体栈、圆角见 `references/type-and-tokens.md`。
6. 修改单循环：一轮一类、≤5 条。默认 2-3 轮，超了先停下问「是方向错了还是细节没完」——方向错回关 2，不要在细节里打转。模板见 `templates/change-request.md`，细则见 `references/review-and-rework.md`。
7. 主线是 Agent Skill 直接生成代码（HTML/React）。OpenPencil、Figma 不进主线，本工作流不依赖 OpenPencil。设计工具只在两个场景作辅线：只想要一张效果图/PNG 给人看，或探索版式灵感（OpenPencil 类）；以后要招设计师或外包协作、把设计稿交给别人（Figma）。
8. Stageshow（源 benjitaylor/skills；推荐配合，若环境已安装）是关 4b 的下游生产线，不再是旁路：只出宣传用的静图 / 动画 / Bento，只能使用 4a 的组件、锁定 tokens 与同一份数据源，不得自行发明样式，也不替代 4a 真界面与关 5 验收。4b 完成后，从 4b 代码重新提取 tokens，与锁定版逐条对账，差异写入 `CHANGELOG-UI.md`。未安装时，按 `composition.md` 第三节的口径，用页面逐帧截图加 ffmpeg 出片。构图规矩（`references/composition.md`）的【通用】条两线都要遵守，【物料】条在真页面禁用。先生图后还原、中后台口径、评审小测试三组方法借自 Oil UI 的公开方法，已并入本技能 references。

## 关口调度

| 关口 | 派谁 |
|---|---|
| 关 1 | 执行本技能的 agent 问，用户答。Brief 用 `templates/brief.md` |
| 关 2 | 先定标杆，出样按 `references/composition.md` 摆。UI UX Pro Max（推荐配合，若环境已安装；未安装时按本技能 references 的对应口径直接执行）定结构与组件选型。脱离参考图时，Taste（推荐配合，若环境已安装；未安装时按本技能 references 的对应口径直接执行）定原创方向。出样默认由执行本技能的 agent 本人出样（自出）。要走先生图时才读 `references/image-first.md` |
| 关 3 | 不新调审美技能。按 `references/type-and-tokens.md` 锁定 |
| 关 4 | 4a：执行本技能的 agent 定方案、写简报、做验收。标杆页、组件化、tokens 一致，按 `composition.md` 的【通用】【页面】条执行。4b：Stageshow 按它的 look → story → example → screen → choreograph → rehearse 走，look 一步把 4a 组件放进 Stage，不用 kit 自带外观。版式定版之后才用 Emil / animate（推荐配合，若环境已安装；未安装时按本技能 references 的对应口径直接执行）加动效。仪表盘、数据表、表单读 `references/admin-workspace.md` |
| 关 5 | 按修改单改，加做 `composition.md` 第六节构图问答、标签碰撞检测、屏上数字反读，并跑 `references/density.md` 的密度校验脚本出 density.json（自查必须引用读数，见该文件第四节）；4b 另跑 Stageshow 的影片闸门。审查技能留到关 6 |
| 关 6 | Impeccable（推荐配合，若环境已安装；未安装时按本技能 references 的对应口径直接执行）做 audit / polish。Hallmark（推荐配合，若环境已安装；未安装时按本技能 references 的对应口径直接执行）做 sloplint。只有 iOS 向 App 页才加 Apple Design / mobile-native（推荐配合，若环境已安装；未安装时按本技能 references 的对应口径直接执行）。评审小测试见 `references/review-and-rework.md` |

定版把 Emil 记为全套 16 技能，没有列出 16 个名字。Emil 为推荐配合（若环境已安装）；未安装时按本技能 references 的对应口径直接执行。点名范围只有关 4 动效和关 6 的 Apple / 移动端审查。

## 参考文件索引

- `references/gates.md`：每关开始时读。六关步骤、产物、过关。
- `references/sampling-and-vendors.md`：关 2 派单、核对技能、逐项自查、验收交付时读。
- `references/type-and-tokens.md`：关 3 锁定字号、字体、圆角、间距、tokens 时读；改字号时再读。
- `references/image-first.md`：直出小样排版平庸、方向定不下，或用户想先看图定方向时读。不是关 2 的默认路。
- `references/density.md`：关 1 写逐格内容配额、关 4 定版式、关 5 跑密度校验时读。密度脚本在 `scripts/density_check.py`。
- `references/benchmark-density.md`：关 2 定标杆、关 5 对标时读。已验收样例的逐格元素盘点；标杆必须含外部样例，自制小样不算。
- `references/admin-workspace.md`：做仪表盘、数据表、表单这类工作区或后台页时读。
- `references/composition.md`：关 2 出样、关 4 实现、关 5 验收时读。构图规矩，分【通用】【物料】【页面】三类。
- `references/review-and-rework.md`：关 5 修改单循环、微调快车道，以及关 6 审查上线时读。

模板：关 1 复制 `templates/brief.md`。关 5 复制 `templates/change-request.md`。

## 文件结构约定

每个 UI 项目统一：

```
<project>/
  brief.md                # 关1
  explorations/           # 关2 三个方向 + 对比图
  design-tokens.md        # 关3 锁定版
  explorations/benchmarks/ # 关2 标杆图
  src/ ...                # 关4a 真页面代码（组件与 tokens 为准，母版）
  promo/                  # 关4b 宣传物料源码 + dist 成品（只引用 src 的组件与 tokens）
  reviews/review-v1.md    # 关5 每轮验收与修改单
  CHANGELOG-UI.md         # 解锁/变更记录一行一条
```

关 2 未选中的稿留在 `explorations/`，按 vA、vB、vC 存档，不删，日后回看不用重生成。
