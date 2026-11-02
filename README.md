# ui-workflow：一套减少返工的 UI 设计工作流（AI Agent 技能）

给 AI agent 用的 UI 工作流技能。核心判断：**UI 返工多，不是因为 AI 不会设计，而是因为决定没有提前定死**——方向没选、tokens 没锁、数据口径没统一，做到一半全是返工。这套流程把决定拆成六关逐个锁死，用户全程只做选择题，执行者（任何 agent）按关推进。

不依赖特定厂商或 agent：单 agent 也可全程执行；环境里装有 Taste、UI UX Pro Max、Emil、Impeccable、Hallmark 等设计技能时，本技能只在对应关口点名调用，不抢它们的触发。

## 六关

| 关 | 做什么 | 产物 | 过关条件 |
|---|---|---|---|
| 1 | 需求 Grill：核现状、判新建/改版、定产物类型、答 5 题、写未来功能预留 | `brief.md` | 用户说清要什么 |
| 2 | 先定 2–3 张标杆，再出 3 个方向（只做首屏），用户选 1 个或组合选 | `explorations/` vA/vB/vC ＋ 对比截图 | 用户已选定，交付经字节校验 |
| 3 | 把选中方向锁成 Design Tokens（双轨制：意图版 ＋ 代码提取版，差异逐条裁定） | `design-tokens.md`（已批准版） | 用户确认锁定表 |
| 4 | 4a 做透 1 个真标杆页（母版），再复制组件与 tokens；4b 宣传物料（静图/动画/Bento）用同一套组件、tokens、数据派生 | 标杆页 ＋ 组件清单；`promo/` 成品 | 用户确认标杆页 |
| 5 | 桌面 ＋ 手机双截图验收 ＋ 构图问答 ＋ 数字反读，修改单循环（默认 2–3 轮） | `reviews/review-vN.md` | 回执与修改单逐条对得上 |
| 6 | 审查后上线，部署后公网实测一次 | 审查结论 | 评审小测试过关才部署 |

## v1.3 密度纪律（治「空格子」）

宣传物料最常见的翻车是格子空洞：自查写「全过」，交出来的图一半是空白。v1.3 为此加了三件套（详见 `references/density.md`）：

- **配额前置**：brief 必须含逐格内容配额表，每格元素逐项列明并给下限；
- **格随内容定**：先内容清单后网格，达不到配额的格缩小、合并或取消，不许留空格；
- **读数验收**：按实际网格写布局文件，跑 `scripts/density_check.py` 量每格墨水覆盖率，全格 PASS 才算完成；自查结论必须附读数证据，只写「是」无效。标杆必须含外部样例（`references/benchmark-density.md`）。

## 数据自洽纪律

图里的每个数字都要互相咬合：单一数据源生成、其余画面从它派生；占比与时长对得上、均值与柱值对得上、达标率与天数对得上。验收时从数据源重算，而不是听执行者自述——实测证明自报清单会整段转写错误（见案例）。

## 安装与使用

把本仓库整个目录放进你的 agent 技能目录即可（SKILL.md 为标准 agent-skill 格式），例如：

- pi：`~/.pi/agent/skills/ui-workflow/`
- Claude Code：`~/.claude/skills/ui-workflow/`

对话里让 agent「按 ui-workflow 做这个页面」即可启动；它会从关 1 的 5 道题开始，把你需要拍板的事逐关变成选择题。

## 文件地图

- `SKILL.md`——总控：六关速览、原则、与其他技能的调用关系
- `references/gates.md`——六关全文
- `references/composition.md`——构图与版式口径
- `references/density.md`、`references/benchmark-density.md`——密度纪律与标杆拆解
- `references/type-and-tokens.md`——字号阶梯、字体栈、tokens 纪律
- `references/sampling-and-vendors.md`——出样分工、交付判定通则、逐项自查表
- `references/image-first.md`——先生图后还原的备选路
- `references/admin-workspace.md`——中后台/工作区型页面口径
- `references/review-and-rework.md`——关 5/6 验收与修改单循环
- `templates/brief.md`、`templates/change-request.md`——简报与修改单模板
- `scripts/density_check.py`——密度读数脚本

## 实测案例

[examples/qichi-sleep-report/](examples/qichi-sleep-report/)：一道例题（虚构睡眠 App 的年度报告物料），三个不同的 AI 执行者互不知情、只用本技能各做一遍，全程独立验收。结论速览：三方数据勾连全过、密度纪律生效；同时暴露了共同问题（数据爱凑整、图表标注不避让、寄语格稀疏），以及一条介质教训——**可落地性由交付介质决定**：只规定「出图」时，执行者会选固定画布或 SVG；要真页面，必须在简报里写明真实视口宽度、HTML＋CSS 变量与断点。
