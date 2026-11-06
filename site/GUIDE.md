# List introduction maintenance / 介绍页维护

The introduction is separate from the application. English is at `/`, Chinese at `/zh/`. It builds with Python's standard library and never reads environment files. / 介绍页与应用独立，英文默认、中文位于 `/zh/`；仅需 Python 标准库，不读取环境文件。

## Content and code / 内容与代码

- `site/content.json`: both languages, concrete workflow, storage and snapshot-sharing explanation. Update them together. / 同步维护双语文案、实际流程与存储分享说明。
- `site/build.py`: layout, gallery filenames, source sample validation, SEO metadata and existing banner copy. / 页面结构、图片清单、示例来源检查与分享元信息。
- `site/demo.js`: unsaved adaptation of `getComparisonBuckets` in `src/lib/app-selectors.ts`. If those four conditions change, update both and check every bucket. It is an explanation, not the full React workspace. / 四类对比规则的无保存演示，源规则变化后同步更新并检查四种结果。
- `site/style.css`: actual #002fa7 blue, gray shell and ruled-paper surfaces from `src/index.css`. Preserve readable focus states and mobile layout. / 继承真实应用的蓝色、灰色外壳与纸张视觉，保持键盘焦点和移动端布局。
- Example items are validated against `DEFAULT_ITEMS` in `src/lib/workspace-constants.ts`. English sample labels are explanatory translations. / 示例核对内置条目，英文为介绍用译文。

## Replace these assets / 替换哪些素材

| File | Replace when / 何时替换 |
| --- | --- |
| `site/assets/gallery-current.png` | Gallery or notebook creation changes / 总览或新建入口变化 |
| `site/assets/stack-current.png` | Cover, stack or navigation changes / 封面、堆叠或翻页变化 |
| `site/assets/marked-current.png` | Page layout, checkbox or completion marker changes; also used as hero / 内页、勾选或高亮变化，同时用于首屏 |
| `site/assets/compare-current.png` | Review/comparison layout or result labels change / 对比界面或结果分类变化 |
| `docs/readme/banner.png` | Approved banner changes; used as Open Graph image / 已确认 banner 更新时同步 |
| `docs/readme/assets/frankie.svg` | Approved family signature changes / 系列签名更新 |

## Capture actual UI / 采集真实界面

Run `npm ci` then `npm run dev -- --port 8336 --host 127.0.0.1`. Use a new local origin so existing personal notebooks stay untouched. Use bundled defaults or clearly labelled demo data, never personal records. Wait for fonts and card transitions to settle before capture. / 使用新的本地域名端口，避免修改已有个人清单；只用内置数据或明确的演示数据，等待字体和翻页动画稳定。

1. Capture the default gallery. Open stack view and capture the cover. / 采集总览，打开堆叠视图采集封面。
2. Move to the first page and tick two bundled items. Capture the marker/checkbox treatment. These are staged examples, not a user's history. / 第一页勾选两个内置条目，注明为示例记录。
3. Generate a snapshot from bundled data, open it locally, review your answers, then use Compare this group. Capture the four result groups. Do not include full share-key URLs in documentation or screenshots. / 本地打开内置数据快照，填写自己的答案再对比，不公开完整分享参数。
4. Update both captions in `content.json`, then rebuild. The hero crops a real capture in CSS; adjust its crop if the app layout changes. / 同步双语图片说明并重新构建，界面尺寸改变时调整首屏 CSS 裁切。

Sharing semantics are owned by `src/lib/app-state-storage.ts` and `src/lib/notebook-utils.ts`; local IDs and encryption keys are in those files too. Recheck the privacy explanation if persistence, URL encoding or import changes. / 若本地存档、链接编码或导入方式变化，重新核对这些源码与隐私说明。

## Build and check / 构建与检查

```sh
python3 site/build.py --out /tmp/list-intro-preview
python3 -m http.server 8320 --bind 127.0.0.1 --directory /tmp
node --check site/demo.js
```

Open `http://127.0.0.1:8320/list-intro-preview/` and `.../zh/`. Check desktop and 390px phone width, all image loads, language links, sample checkbox changes/reset, and `#use`/`#start`. No app server or model API is needed for the introduction. / 检查双语、桌面与手机宽度、图片、语言链接、示例四类状态与重置、锚点；介绍页不需要应用服务器或 AI API。

The existing `.github/workflows/pages.yml` publishes `_site` on `main` after relevant changes. Commit only reviewed task files. The notebook data and app behavior are outside an intro-only update. / 现有工作流发布 `_site`，仅提交审核后的本次文件。
