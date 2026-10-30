[English](#english) · [简体中文](#简体中文)

<a id="english"></a>

# Delivery Conventions


## Files

- `manifest.json` contains an `assets` array. Each entry requires `id`, `file`, `name`, `methods`, `transparent`, `width`, and `height`.
- `file` is relative to the pack root. Absolute paths, `..`, and symlinks outside the directory are prohibited.
- `methods` is a non-empty array containing extracted / inpainted / reconstructed / new.
- `transparent` is a boolean. When true, the image must contain transparent pixels and visible content.
- Optional fields include `source`, `notes`, and `knownIssues`. Explicitly mark uncertainty.
- `layout.json` includes `canvas.width`, `canvas.height`, `coordinateSystem`, and `layers`.
- Recommended coordinates: source-image pixels, top-left origin, y increasing downward. Each layer includes assetId, x/y, width/height, zIndex, and anchor. Anchors are normalized coordinates within the asset; engine conversion may be needed.
- Transparent padding and cropping affect anchors. Set `estimated: true` for estimated coordinates.
- `texts.json` stores readable keys and original copy. Do not invent OCR results; flag uncertain text for review.

Example manifest:

```json
{
  "assets": [
    {"id":"button_primary","name":"Primary button base","file":"ui/button_primary.png","methods":["inpainted"],"transparent":true,"width":600,"height":180,"notes":"Button text removed"},
    {"id":"background","name":"Clean background","file":"background/background.png","methods":["inpainted"],"transparent":false,"width":1080,"height":1920}
  ]
}
```

## README contents

1. Input, scope, and tools actually used.
2. File purposes, filenames, and processing methods.
3. Background elements retained and removed.
4. Layer order and coordinate conventions, including positions needing adjustment.
5. Rotor, character, and plant pivots and suggestions for animating static parts.
6. Independent text-layout guidance; engine-specific notes when requested.
7. Inpainted, reconstructed, and newly added areas and differences from the source.
8. Unfinished work, visual defects, and verification limits.

Do not describe static images as rigged animation. Do not claim nine-slice configuration, atlases, or production compression unless actually created and verified.

## Overview and reassembly

Use actual delivered images for the overview. Show names and methods; display transparency on checkerboard or neutral backgrounds. Reassembly must use actual assets and layout. Do not build a web product: a simple local HTML inspection page is sufficient as an auxiliary preview.

---

<a id="简体中文"></a>

# 交付约定


## 文件

- manifest.json：`assets` 数组；每项必须有 `id`, `file`, `name`, `methods`, `transparent`, `width`, `height`。
- `file` 为包根目录相对路径，禁止绝对路径、`..`、目录外软链接。
- `methods` 为非空数组，可用 extracted / inpainted / reconstructed / new。
- `transparent` 为布尔值。为 true 时实际图片应既有透明像素也有可见内容。
- 可加 `source`, `notes`, `knownIssues`，事实不明时明确标记。
- layout.json：写 `canvas.width/height`, `coordinateSystem`, `layers`。
- 推荐坐标为原图像素、左上原点、y 向下；每层含 assetId、x/y、width/height、zIndex、anchor。锚点是素材内部归一化坐标；实际引擎可能需要转换。
- 裁切边距与尺寸会影响锚点；坐标是估算时用 `estimated: true`。
- texts.json：可读键名与原文文案，不虚构 OCR 结果；不确定文字标注待确认。

示例 manifest：
```json
{
  "assets": [
    {"id":"button_primary","name":"主按钮底板","file":"ui/button_primary.png","methods":["inpainted"],"transparent":true,"width":600,"height":180,"notes":"已移除按钮文字"},
    {"id":"background","name":"干净背景","file":"background/background.png","methods":["inpainted"],"transparent":false,"width":1080,"height":1920}
  ]
}
```

## README 内容

1. 输入与处理范围；使用的实际工具。
2. 素材用途、文件名及处理方式。
3. 底图保留、移除的元素。
4. 图层顺序及布局坐标约定；哪些坐标需要微调。
5. 转子、人物、植物等锚点与静态部件动画建议。
6. 文字独立排版建议；如有指定，引擎适配说明。
7. 补绘、整体重建、额外新增的范围及原图差异。
8. 未完成项、视觉缺陷与验证限制。

不要把静态图片包写成骨骼动画包；不要声称已配置九宫格、图集或上线压缩，除非确实制作并验证。

## 总览与重组

总览优先使用实际交付图像制作，显示名称、处理方式，透明图在棋盘格或中性底色上显示。重组使用实际素材与真实布局。无需重做网页产品；简单本地 HTML 检视页可以作为辅助预览。
