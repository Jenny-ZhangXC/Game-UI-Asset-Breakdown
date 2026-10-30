[English](#english) · [简体中文](#简体中文)

<a id="english"></a>

# Game UI Asset Breakdown


Upload a mini-game UI screenshot or concept image and let an agent organize it into independent artwork for game development.

## Capabilities

- Analyze an entire screen or selected elements; separate transparent icons, logos, button bases, and characters.
- Remove button text, complete occluded regions, and repair clean backgrounds.
- Separate static animation parts such as rotors, clouds, and plant clusters.
- Inspect transparency, edges, completeness, and reassembly.
- Deliver manifests, layout, text copy, and a README, with an optional ZIP.

## Usage

Place this directory in a compatible agent's skill directory, preserving its structure. Codex's default personal location is `~/.codex/skills/game-ui-asset-breakdown/`; automatic discovery depends on the host's configuration.

Upload an image, then ask:

> Use $game-ui-asset-breakdown to split this mini-game UI into transparent artwork, a clean background, and necessary animation parts. Inspect the results and deliver an asset pack with a README.

You can limit the scope:

> Use $game-ui-asset-breakdown to extract only the loading-screen logo, empty progress track, and gradient fill. Save the text separately.

## Requirements

- An agent supporting skill files.
- Available image generation/editing tools, usually built-in image_gen.
- Python 3 and Pillow for the helper. If necessary, install Pillow in the selected environment with `python -m pip install Pillow`.

The skill does not include an image model, service credentials, or commercial API credits. Do not commit API keys to a public repository.

## Validation and packaging

```sh
python scripts/check_pack.py path/to/delivery
python scripts/check_pack.py path/to/delivery --zip path/to/assets.zip
```

The ZIP must be outside the delivery directory and must not already exist. The checker validates PNG decoding, dimensions, transparent regions, and basic file constraints. It does not assess semantics or visual quality; the agent must still inspect each image.

## Structure

```text
game-ui-asset-breakdown/
├── SKILL.md                    # English first, then Chinese / 先英文后中文
├── README.md                   # English first, then Chinese / 先英文后中文
├── agents/openai.yaml          # Bilingual metadata / 双语界面信息
├── references/delivery.md       # Bilingual delivery conventions / 双语交付约定
└── scripts/check_pack.py        # Validation and packaging / 检查与打包
```


## Limitations

Extraction and AI inpainting do not recover original layers. Completion or reconstruction may change details, and edges may require cleanup. Deliveries should label methods and known issues.

This skill does not recover PSD files, original fonts, or licenses. It does not implement games, create websites by default, or promise rigs, frame sequences, or configured engine scenes.

## Rights and licensing

Skill instructions and scripts do not grant rights to input artwork, third-party fonts, or generated assets. No open-source license is currently included. Maintainers wishing to grant modification and redistribution rights should separately choose and add an appropriate license.

---

<a id="简体中文"></a>

# Game UI Asset Breakdown


上传一张小游戏界面截图或效果图，让 Agent 将其整理为可用于游戏开发的独立美术素材。

## 功能

- 分析整页界面或指定元素，拆出透明图标、标题、按钮底板和角色。
- 去除按钮文字、补齐遮挡区域、修复干净底图。
- 分离风车转子、云层、植物簇等静态动效部件。
- 检查透明度、边缘、完整性与重组效果。
- 整理素材清单、布局、文案和 README，按需生成 ZIP。

## 使用

将本目录放入兼容 Agent 的技能目录，保留子目录结构。Codex 的默认个人位置为 `~/.codex/skills/game-ui-asset-breakdown/`；能否自动发现技能，以实际平台配置为准。

上传图片后输入：

> 使用 $game-ui-asset-breakdown 将这张小游戏 UI 拆成透明美术素材、干净背景和必要动效部件，检查后交付素材包与 README。

也可以只要求特定元素：

> 使用 $game-ui-asset-breakdown，只拆出加载页 Logo、进度条底槽和渐变填充，文字另存。

## 运行要求

- 支持技能文件的 Agent。
- 可用的图像生成／编辑工具，通常为内置 image_gen。
- 检查脚本需要 Python 3 和 Pillow。必要时在所选环境运行 `python -m pip install Pillow`。

技能不自带图像模型、凭证或商业 API 额度。公开仓库不应包含 API Key。

## 检查与打包

```sh
python scripts/check_pack.py path/to/delivery
python scripts/check_pack.py path/to/delivery --zip path/to/assets.zip
```

ZIP 必须位于交付目录之外，不能覆盖已存在文件。检查器验证 PNG 解码、尺寸、透明区域和基本文件约束，不判断语义或视觉质量；Agent 仍应逐张查看。

## 结构

```text
game-ui-asset-breakdown/
├── SKILL.md                    # English first, then Chinese / 先英文后中文
├── README.md                   # English first, then Chinese / 先英文后中文
├── agents/openai.yaml          # Bilingual metadata / 双语界面信息
├── references/delivery.md       # Bilingual delivery conventions / 双语交付约定
└── scripts/check_pack.py        # Validation and packaging / 检查与打包
```

## 限制

提取和 AI 补绘不等于恢复原始图层。补全与重建可能改变细节，边缘可能需精修，交付中应注明处理方式和已知问题。

不恢复 PSD、原始字体或授权，不开发游戏、不默认创建网站，也不承诺骨骼动画、帧序列或已配置的引擎场景。

## 版权与许可

技能说明和脚本不代表对输入图片、第三方字体或输出素材提供版权授权。当前未附开源许可证；若希望授予修改和再分发权，应由维护者另行选择并添加许可证。
