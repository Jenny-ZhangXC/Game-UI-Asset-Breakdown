---
name: game-ui-asset-breakdown
description: Split game UI screenshots into transparent assets, clean backgrounds, and animation parts, with inspected deliverables and a README. 将小游戏界面拆成透明素材、干净背景及动效部件，检查并交付素材包与说明；不用于网页或玩法开发。
---

[English](#english) · [简体中文](#简体中文)

<a id="english"></a>

# Game UI Asset Breakdown


Turn a flattened concept image into inspectable, composable game artwork. Process only the requested elements when the user limits the scope. Do not build websites, publish sites, or create game projects by default.

## 1. Inspect and plan

View each input image rather than relying on its filename. Identify the screen's purpose, style, element boundaries, and occlusions. List candidate assets, source bounds, processing methods, and which objects remain in the background.

Separate elements needing interaction, reuse, different text, movement, or animation. Keep fixed scenery in the background. Do not impose an asset count or separate incidental scenery without a purpose.

- Title logo: usually one complete transparent image.
- Ordinary text, numbers, and taglines: extract as copy. Do not describe generated fonts as original font files.
- Buttons: separate blank bases, text, and reusable icons.
- Round controls: separate base and icon when useful; do not invent missing states by default.
- Characters: keep the whole character unless a specific action requires body parts or frames.
- Animation decorations: separate rotors, clouds, plant clusters, leaves, and similar parts as needed.

Briefly explain the plan, then proceed without confirmation for every asset. Clarify only when missing information materially affects delivery, such as reconstructing a full identifiable character from a head-only screenshot. A screenshot is sufficient to begin; do not demand nonexistent layered sources.

## 2. Choose processing methods

Prioritize the original appearance and visible pixels instead of redrawing everything. Label assets with one or more methods: `extracted`, `inpainted`, `reconstructed`, or `new`.

- Extraction: isolate the object and export transparency. A rectangular crop is not a cutout.
- Text removal: remove variable copy, repair the underlying base, and preserve borders, highlights, and shadows.
- Completion: fill missing or occluded regions while preserving existing shapes, colors, and character features.
- Background repair: collect regions occupied by independent elements, remove those objects, and fill the scene behind them without duplicates.
- Reconstruction: use when reliable extraction is unavailable. Explain that it does not precisely recover original layers.

Use available image generation/editing tools, usually built-in image_gen. Follow the imagegen skill's tool and saving rules when available. View local inputs before editing. Generate or edit each asset separately, explicitly identifying references and edit targets. Request real transparency for isolated assets; keep backgrounds opaque when appropriate. Do not invent tools or write alternative API runners. If tools are unavailable, explain the limitation, preserve completed work, and do not substitute placeholders.

Each prompt should identify a single target, visual invariants, and excluded objects. Never print image base64. Save selected outputs in the delivery directory promptly, recording sources and processing methods.

## 3. Animation parts and background consistency

Deliver static animation parts by default, not rigs, frame sequences, or configured engine animations.

- Windmill: separate the building and complete rotor; record the hub pivot.
- Cloud: independent drifting layer.
- Plant cluster: preserve roots and tips; sway around the base.
- Character: a full character supports subtle whole-body movement; its ground shadow can be separate.
- Leaf: a small isolated sprite for drifting or particles.

Remove moving objects from the background. For extra overlays, state that static counterparts remain. A shadow asset must contain only a shadow; a rotor asset must contain only the rotor.

## 4. Inspect and correct

Check files and actual transparency, then visually inspect every image. Metadata or an alpha channel cannot replace visual inspection. Look for baked-in checkerboards, light/dark fringes, speckles, residual text, clipped parts, unrelated objects, style drift, and character identity changes.

Check the background for separated objects left behind. Reassemble principal assets at their source positions to inspect scale, layering, alignment, and occlusion. Use actual deliverables, not a new generated illustration unrelated to them. An HTML overview may show real images; use permitted image tools when an exported composite is needed.

Correct observed problems individually, with at most two targeted retries per asset by default. If an asset remains unsuitable, list the unresolved issue and retain usable work. Do not generate indefinitely, claim everything is complete, or introduce unrequested style changes.

## 5. Organize delivery

Read [Delivery conventions](references/delivery.md). Write the manifest, layout, text list, and README. Record actual dimensions and layout; mark estimated coordinates as estimates. Distinguish geometric centers from hub, root, and other physical pivots.


Organize by purpose: background, ui, icons, characters, effects, preview. Create only needed directories. Use stable English filenames and version revisions instead of overwriting selected outputs.

The README must explain file purposes, scenery retained in the background, layers, coordinates, pivots, animation suggestions, inpainting, and known issues. Add engine-specific guidance only when the user names an engine such as Cocos. Do not invent PSD files, font sources, or commercial licenses.

Validate and package with Python 3 and Pillow. Prefer an available environment runtime; disclose limitations if dependencies cannot be obtained.

```sh
python scripts/check_pack.py <delivery-directory> --zip <zip-path-outside-delivery-directory>
```

The helper only reads images, checks the manifest, and packages files. It does not edit images or assess visual quality and semantics. Fix errors first. Incomplete delivery may remain unpackaged or explicitly list unfinished work in the README; never conceal failed checks.

Finish with an overview, links to the asset ZIP and README, and a brief account of extraction/inpainting scope and unresolved work. Report only work actually completed and inspected.

---

<a id="简体中文"></a>

# Game UI Asset Breakdown（游戏 UI 素材拆分）



把合成效果图变为可检查、可组装的美术素材。用户只指定部分元素时，仅处理指定范围。不要开发网页、发布站点或默认创建游戏工程。

## 工作流程

### 1. 检视与规划

实际查看每张输入图，不仅依赖文件名。判断页面用途、风格、元素边界及遮挡关系。列出候选素材、原图范围、处理方法及其在底图中的去留。

原则：需要交互、复用、换文字、移动或动画的元素独立；固定景物合入背景。不固定拆分数量，不逐片拆无用途的景物。

- 标题 Logo：通常作为整体透明图。
- 普通文字、数字、标语：提取文案；不把生成字体误称为原始字体。
- 按钮：空白底板、文字、可复用图标分开。
- 圆形功能按钮：底板和图标可分开；原图没有的状态不默认增画。
- 角色：默认完整人物；仅在具体动作需要时规划身体部件或动画帧。
- 动效装饰：按需求拆转子、云层、植物簇、飘叶等。

简短说明拆分方案后继续工作，不逐素材请求确认。只有缺失信息会明显改变交付（例如截图只有头部却要求还原全身身份）时才澄清。用户提供截图即足以开展合理拆分；不要求提供不存在的分层源文件。

### 2. 选择图片处理方法

优先保留原图外观与可见像素，避免把所有元素无差别重画。为每个素材标记 `extracted`（提取）、`inpainted`（局部补绘）、`reconstructed`（整体重建）或 `new`（新增）；可记录多项处理。

- 提取：分离对象，透明背景导出；普通矩形裁切不等于抠图。
- 去字：去除可变文案，修复其后底板，保留边框、高光和阴影。
- 补全：只补缺失或被遮挡部分，尽量保持已有形状、颜色、人物特征。
- 底图：汇总独立元素的移除区域，补齐遮挡背景，避免残影。
- 重建：无法可靠提取时才用，并清楚说明不能精确恢复原始图层。

使用可用的图像生成/编辑工具（通常为内置 image_gen）；如 imagegen 技能可用，遵循其工具和保存规则。编辑前查看本地输入；每个资产单独生成/编辑，并明确参考图与编辑目标。透明素材显式要求真实透明背景，底图按场景选择不透明背景。不要用另行编写的 API runner 或凭空替代工具。工具不可用时说明限制，保留已完成成果，不交付占位图冒充完成。

提示中指定唯一目标、需保留的外观及需排除的其他物体。不要输出工具的 base64 内容。及时保存最终选定文件到交付目录，记录其源图和处理方法。

### 3. 动效拆分与背景一致性

默认输出静态动画部件，不承诺骨骼、帧序列或已配置的引擎动画。

- 风车：建筑与完整转子分离，记录轮毂锚点。
- 云：独立漂移层。
- 植物簇：完整根部和穗尖，以根部为摆动轴。
- 人物：整体轻晃时完整人物即可，脚底投影可独立。
- 飘叶：单独小素材，用于漂移或粒子。

作为移动层的对象应从底图移除；若只是额外覆盖装饰，注明底图已有静态内容，避免误认为完整分层。投影应只有投影，转子应只有转子。

### 4. 检查与修正

先检查文件和真实透明区域，再实际查看每张图片；元数据或存在 alpha 通道不能代替视觉检查。注意不透明棋盘格、白边黑边、杂点、残字、裁断、误带其他物体、画风和身份漂移。

检查底图中是否残留独立对象。将主要素材按原位置组合预览，检查大小、层级、对齐和遮挡。组合是质量检查，不是重新生成一张与素材无关的效果图。概览可用 HTML 加实际图片；若需要合成导出图，使用环境允许的图像工具。

仅针对发现的问题修正，默认每项最多两次针对性重试。若仍不合格，列出具体未完成问题，保留可用结果，避免无限生成或宣称全部完成。不要扩大为未请求的画风改版。

### 5. 整理交付

阅读 [交付约定](references/delivery.md)，写入素材清单、布局、文案和 README。记录实际尺寸和布局，不能把猜测坐标描述为已验证值。区分几何中心与轮毂、根部等真实锚点。

目录按用途组织（background、ui、icons、characters、effects、preview），只创建需要的目录。文件名用稳定英文名；重做使用版本文件名，不覆盖已选择版本。

README 必须包含实际文件用途、背景保留内容、层级、坐标约定、锚点、动效建议、补绘与已知问题。只有用户指定 Cocos 等引擎时增加针对性说明。不得虚构 PSD、字体源文件或商用授权。

运行下面工具检查并打包（需要 Python 3 与 Pillow；缺依赖时优先使用环境提供的运行时，无法获得时说明验证限制）：

```text
python scripts/check_pack.py <交付目录> --zip <交付目录之外的zip路径>
```

工具只读图片、检查清单并打包，不修改图像。它验证透明区域与文件约束，不判断视觉质量或语义。存在待修复错误时先修正；不完整交付可以不打包或在 README 中明确列出未完成项，不把检查失败藏起来。

最终展示总览，链接素材 ZIP 和 README，简要说明提取/补绘范围与未完成项。只报告确已完成并检查过的内容。
