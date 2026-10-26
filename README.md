# ROCC Wallpaper Studio

**把 ROCC 的设计经验，变成你自己的动漫壁纸创作工作流。**

ROCC Wallpaper Studio 是一个免费的动漫壁纸创作项目，包含简易网页工作台，以及可用于 **Codex / Claude Code** 的 Agent Skill。选择创作方向、描述主题，再用你自己的图像工具或 API 生成并检查作品。

**Anime wallpaper workflows for your own AI tools.** A bilingual web studio and a portable Codex / Claude Code Skill, with four art directions and structured visual review.

[网站入口 · 中文](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=zh#studio) · [Website · English](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=en#studio) · [用 Codex / Claude Code 创作](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=zh#install)

> **访问状态 / Access:** 网站目前为作者预览，仅向已有访问权限的账号开放；GitHub 仓库与 Skill 已公开。若网站提示无权限，仍可按下方说明直接使用 Skill。The website is currently owner-private; this repository and its Skill are public and can be used independently.

## 网站是什么？

网页把设计方法、图像生成和 Agent 使用入口放在一起：

- **工作台：** 填写主题，选择方向、用途与配色；使用自己填写的图像 API Key 生成。
- **动漫方法：** ROCC 风格置首，另有七龙珠、火影、哆啦A梦研究方向。
- **使用 Skill：** 选择 Codex 或 Claude Code，网页整理指令并打开相应工具，用户确认发送；首次导入说明随任务提供。
- **评估记录：** 展示各方向的验收重点和真实评估进度，旧版样本单独保留，不把历史结果当成新方法的成功率。
- **中文 / English：** 界面与制作任务可切换语言。

### 入口导航

| 入口 | 用途 |
| --- | --- |
| [动漫壁纸工作台](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=zh#studio) | 填写主题、选择风格，使用自己的图像 API |
| [动漫设计方法](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=zh#methods) | 查看 ROCC、七龙珠、火影、哆啦A梦四个方向 |
| [Codex / Claude Code 使用入口](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=zh#install) | 整理任务并交给你的 Agent；也可下载离线包 |
| [评估记录](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=zh#evaluation) | 查看当前评估状态与验收标准 |
| [English website](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=en#studio) | Open the studio in English |

网页适配 OpenAI GPT Image、Google Gemini / Nano Banana、豆包 Seedream、Qwen Image、Wan、Grok Imagine、FLUX、Stability 和 Ideogram。自动模式只在已配置服务中选择，支持手动覆盖；不自动重试或跨平台补单。各服务真实账号的权限、地区、额度与生成质量需自行验证。

Key 只在当前页临时保留；一次生成仅将所选 Key 经本站服务端转发至相应服务，不写入保存的配方或数据库。模型费用由使用者自己的账号承担。网站不会获得你的 Codex / Claude 订阅额度。

## 最简单：把这段话发给你的 AI

```text
请读取 https://github.com/rocc94/rocc-wallpaper-studio 。
把其中适用于当前工具的 rocc-wallpaper-studio Skill 安装到我选择的项目；保留已有文件。
这次直接读取 Skill，使用 ROCC 风格，制作一张原创屋顶信使的动漫壁纸，比例2:3，纸本暖色。
先检查可用图像工具；有能力再出图，没有就明确交付未执行的制作单。不在聊天中索要 Key。
```

也可以在网站的“使用 Skill”页填写主题，再点击打开 Codex / Claude Code。按钮会预填任务，**不会替你自动发送、安装或执行**。首次导入仍遵守工具权限；Codex 需要桌面应用，Claude Code 云端需要登录并选择自己有权限的 GitHub 仓库，可先 [Fork 本项目](https://github.com/rocc94/rocc-wallpaper-studio/fork)。

### 克隆项目后使用

```bash
git clone https://github.com/rocc94/rocc-wallpaper-studio.git
cd rocc-wallpaper-studio
```

在 Codex 或 Claude Code 中打开该文件夹：

- Codex：`$rocc-wallpaper-studio 帮我做一张动漫壁纸`
- Claude Code：`/rocc-wallpaper-studio 帮我做一张动漫壁纸`

首次未自动发现时，重新打开项目/重启工具，或让 Agent 直接读取对应 `SKILL.md` 执行本次任务。

| 工具 | 项目内 Skill 路径 |
| --- | --- |
| Codex | [`.agents/skills/rocc-wallpaper-studio`](.agents/skills/rocc-wallpaper-studio) |
| Claude Code | [`.claude/skills/rocc-wallpaper-studio`](.claude/skills/rocc-wallpaper-studio) |

两个目录由同一套源文件生成。安装 Skill 不会附送图像模型：Codex 可使用可用的会话内置 image 工具；Claude Code 需要已经配置的图像 MCP/API。没有出图能力时，交付制作单并如实说明。

## 原创示例

<img src="assets/rocc-example.webp" width="280" alt="ROCC 原创屋顶信使动漫壁纸示例 / Original rooftop-courier anime wallpaper example">

用于说明画面方向的原创主题示例，实际尺寸 1024 × 1536。它不是质量测评或效果保证。生成来源记录见 [provenance.json](assets/provenance.json)。

## English quick start

ROCC Wallpaper Studio combines a web workspace with an open-source Skill for **Codex and Claude Code**. Art directions: **ROCC signature · Dragon Ball · Naruto · Doraemon**. The web studio supports Chinese and English, your own image API keys, agent-task handoff and transparent evaluation status.

**Website:** [Open in English](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=en#studio) · [Use your agent](https://rocc-wallpaper-studio-lab.rocc94.chatgpt.site/?lang=en#install). The website remains owner-private; you can use the public Skill without website access.

Paste into your agent:

```text
Read https://github.com/rocc94/rocc-wallpaper-studio and install its ROCC Wallpaper Studio Skill for this tool into my selected project, preserving existing files.
Read the Skill directly for this task. Create one original rooftop-courier anime wallpaper using the ROCC recipe, 2:3, warm paper palette.
Check for a real image tool first. Generate only if capable and authorized; otherwise provide an explicitly unexecuted brief. Never ask for API keys in chat.
```

Open a clone in Codex or Claude Code to use the included standard project-level Skill folders. Website launch buttons prefill a task; **you review and send it in your own tool**. Claude Code cloud also needs a repository you can access. Installing this Skill does not supply an image model, API credits or a subscription.

This repository distributes the Skill, its helper scripts, documentation and original example. It does not currently contain the full web application source or the old wallpaper image library.

## 方法来源与使用边界 / Provenance & rights

ROCC 的一般设计方向来自成品观察推断（460份文件元数据、71张视觉抽样），历史提示词尚未提供。三个动漫专题是新增研究方向，尚未完成质量对照；没有训练模型，不承诺每次生成合格。

七龙珠 / Dragon Ball、火影 / Naruto、哆啦A梦 / Doraemon 是研究方向名称，不代表官方关联、角色授权或商业使用许可。请使用新构图，并核对实际用途所需权利。代码与说明采用 [MIT License](LICENSE)，第三方角色、作品和参考素材不包含在本项目许可中。示例采用原创主题，由会话图像工具生成，底层模型未公开。

## 官方能力参考 / Official references

核对日期 / Checked: 2026-10-26.

[Codex deep links](https://learn.chatgpt.com/docs/reference/commands#deep-links) · [Codex Skills](https://learn.chatgpt.com/docs/build-skills) · [Claude Code Skills](https://code.claude.com/docs/en/skills) · [Claude Code prefilled tasks](https://code.claude.com/docs/en/web-quickstart#pre-fill-sessions).
