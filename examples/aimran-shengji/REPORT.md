# REPORT — ui-aimran-test「声记」录音转文字落地页

## 1. 挑件清单

| 组件 id | 用在哪一块 | 为什么选它 | 改了哪些参数 |
|---|---|---|---|
| uv-btn-shine | 首屏「免费试用」主按钮 | 索引明确的「主行动按钮扫光」默认件，全页唯一主特效位 | `--c1` 换成本页 `--brand #0e7c66`；字号走 `--fs-m`；hover 触发改手机端 3.8s 周期自动扫光（见第 3 节） |
| uv-tx-marker-highlight | 卖点区右侧「1 小时录音 5 分钟出稿」段 | 落地页卖点段落用，索引明示一页不超一组 | `--c1/--c2` 换成荧光黄 `#ffd43b` / 荧光蓝 `#74c0fc`；字号挂 `--fs-l`；保留 IntersectionObserver 滚动触发，未加 Replay 按钮（非演示页不需要） |
| uv-btn-ripple | 成功提示演示区的触发按钮 | 触屏原生友好的点击反馈件，浅色底警告→按钮用中深色 | `--c1` 换 `--brand-strong #0a5f4e`（比主色更深，波纹更清楚）；字号 `--fs-s` |
| uv-tg-billing | 定价区月付/年付切换 | 定价页专用件，与 uv-rd-plans 官方搭配 | `--c1` 换 `--brand`、`--c2`（省 20% 徽标）换 `--ok #2f9e68`；文字改「月付/年付/省 20%」 |
| uv-rd-plans | 定价区套餐单选（免费/标准/专业） | 真实 radio 实现，整行点选，定价页配套件 | 3 行套餐文案与价格改为本页数据；`--c1` 换 `--brand`；行底色挂 `--card` |
| uv-ld-status-words | 等待演示区「正在转写」状态条 | 多步处理等待，圆环+状态文案逐句上滑，步骤感正是题目要的 | 文案按真实步骤写「上传→识别→区分说话人」；`--c1/--c2` 换青绿系；保留 `role="status"` |
| uv-toast-success | 成功提示演示（点击按钮触发） | 索引默认的操作成功反馈件，自带 aria-live | `--c1` 换 `--brand`，打勾底色换 `--ok`；原码 `.uv-zs` 固定尺寸演示容器改为 `position:fixed` 全页底部弹入，宽度 `max-width:calc(100vw-40px)` 保 320px 不溢出 |

共 7 件，≥4 件达标；全部为索引 HTML+CSS 类（含几行 JS 触发的），未用 React+Motion 件。

## 2. tokens 表

| 类别 | token | 值 | 用处 |
|---|---|---|---|
| 颜色 | --brand | #0e7c66 | 主色：按钮、开关、选中态 |
| 颜色 | --brand-strong | #0a5f4e | 次级按钮底（波纹可见性） |
| 颜色 | --accent | #e8590c | 强调橙（本页未动用，备用） |
| 颜色 | --hl-1 / --hl-2 | #ffd43b / #74c0fc | 荧光笔两色 |
| 颜色 | --ok | #2f9e68 | 成功打勾、省 20% 徽标 |
| 颜色 | --ink / --ink-2 | #1c2321 / #5b6662 | 正文 / 次级文字 |
| 颜色 | --paper / --card | #f7f6f2 / #ffffff | 页底 / 卡底 |
| 圆角 | --r-s / --r-m / --r-l / --r-pill | 8 / 14 / 20 / 999px | 小件 / 卡与套餐行 / 演示块 / 药丸按钮 |
| 字号 | --fs-xs ~ --fs-xl | 13 / 15 / 17 / 22 / 30px | 辅注 / 组件基准 / 正文 / 小标题 / H1 |
| 动效时长 | --t-fast / --t-med / --t-slow | .25s / .45s / .9s | 微反馈 / 位移弹跳 / 荧光笔划线 |
| 缓动 | --ease-out / --ease-spring | cubic-bezier(.25,.1,.25,1) / (.34,1.56,.64,1) | 常规 / 弹性（开关旋钮、套餐选中、toast 入场） |

各组件内部用组件自带 CSS 变量（--c1/--c2/--s/--k）承接本页 tokens，原码默认配色（#0071e3 等）未进站。

## 3. 手机端处理

| 组件 | 手机（390）触发方式 |
|---|---|
| uv-btn-shine | 原版 hover 独占 → `@media (hover:none)` 下改 3.8s 周期自动扫光（索引先例口径）；保留 :active 按压反馈 |
| uv-tx-marker-highlight | 滚动进入视野触发，手机可用，未改 |
| uv-btn-ripple | pointerdown 触发，触屏原生友好，未改 |
| uv-tg-billing | 真实 checkbox 点击即触发，触点 ≥44px（padding 1em 级），未改 |
| uv-rd-plans | 真实 radio 整行 label 点选，触屏原生，未改 |
| uv-ld-status-words | 纯自动动画无触发问题，未改 |
| uv-toast-success | 点击按钮触发；弹层 fixed 定位，宽度限 `calc(100vw-40px)`，390/320 均不横溢 |

## 4. 自查结果（playwright chromium 真浏览器实测）

- 数据自洽：免费 60 分钟/月；标准 600 分钟/月 ¥29（年付折算 ¥23，¥23×12=¥276≈¥278/年 省 20%）；专业 3000 分钟/月 ¥79（年付 ¥63）；演示样例 42 分钟录音、3 步流程、3 位说话人、出稿 5 分钟；卖点「1 小时录音 5 分钟出稿」与等待区「约 5 分钟出全文」及成功提示「用时 5 分钟」互相印证，无打架。联动实测：切换年付后价格实时变「¥23/月（年付折算）」✓
- 390 宽无横滚：`scrollWidth=390`，`hscroll=false` ✓（1280 桌面同样无横滚 ✓）
- reduced-motion：全 7 件均保留（扫光停用、荧光笔直接显示、状态条只留末句文案+减速圆环、toast 改为常驻显示、套餐/开关过渡缩至 .01s）✓
- 等待条保留 `role="status"`，toast 保留 `aria-live="polite"` ✓
- 功能点测：年付切换 ✓、套餐选中 ✓、toast 弹出（opacity 1、animation uv-zs）✓、荧光笔滚动触发 class=on ✓、控制台 0 报错 ✓

## 5. 索引问题

- 链接与说明均对得上：7 件 `md` 全码文件全部拉取成功，技术标注（HTML+CSS / 需几行 JS）与实际一致，无失效链接。
- 小瑕疵两处：① uv-tx-marker-highlight 原码 JS 里对 `.rp` Replay 按钮做 `querySelector(...).addEventListener`，若使用者删掉演示按钮会直接抛错（索引 HTML 片段含该按钮所以照抄没事，但精简时易踩）；② uv-toast-success 原码是固定 20em×14em 的演示容器加内部绝对定位，当真实全页 toast 用需自行改 fixed 定位，索引「手机端注意」未提示这一点。
- 想用但索引没有的场景：无（本单五块场景全在精选 24 件内覆盖）。
