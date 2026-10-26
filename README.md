# ROCC Wallpaper Studio

**让你的 Codex / Claude Code，用 ROCC 的经验创作动漫壁纸。**

Four directions: **ROCC signature · Dragon Ball · Naruto · Doraemon**. Bring your own image-capable agent. Free, bilingual, no extra ROCC account.

![ROCC original anime wallpaper example](assets/rocc-example.webp)

## 最简单：把这段话发给你的 AI

```text
请读取 https://github.com/rocc94/rocc-wallpaper-studio 。
把其中适用于当前工具的 rocc-wallpaper-studio Skill 安装到我选择的项目；保留已有文件。
这次直接读取 Skill，使用 ROCC 风格，制作一张原创屋顶信使的动漫壁纸，比例2:3，纸本暖色。
先检查可用图像工具；有能力再出图，没有就明确交付未执行的制作单。不在聊天中索要 Key。
```

Codex 使用 [`.agents/skills/rocc-wallpaper-studio`](.agents/skills/rocc-wallpaper-studio)；Claude Code 使用 [`.claude/skills/rocc-wallpaper-studio`](.claude/skills/rocc-wallpaper-studio)。本仓库提供两个工具各自的标准项目目录，两份由同一源文件生成。

也可以下载/克隆整个项目，在 Codex 或 Claude Code 中打开该文件夹：

```bash
git clone https://github.com/rocc94/rocc-wallpaper-studio.git
cd rocc-wallpaper-studio
```

Codex 输入 `$rocc-wallpaper-studio 帮我做一张动漫壁纸`，Claude Code 输入 `/rocc-wallpaper-studio 帮我做一张动漫壁纸`。如首次安装未自动发现，重新打开项目/重启工具，或让 Agent 直接读取对应 SKILL.md 执行本次任务。

## English quick start

Paste into your agent:

```text
Read https://github.com/rocc94/rocc-wallpaper-studio and install its ROCC Wallpaper Studio Skill for this tool into my selected project, preserving existing files.
Read the Skill directly for this task. Create one original rooftop-courier anime wallpaper using the ROCC recipe, 2:3, warm paper palette.
Check for a real image tool first. Generate only if capable and authorized; otherwise provide an explicitly unexecuted brief. Never ask for API keys in chat.
```

Open a clone of this project in Codex or Claude Code to use the included project-level Skill directly. The website can prepare a task and open Codex desktop or Claude Code cloud with a prefilled prompt. **You confirm and send the task in that tool**; the website cannot silently execute local software or borrow its subscriptions.

## What you get

- Four focused anime wallpaper methods, shared Chinese/English production briefs.
- Composition, hierarchy, material, coherence and screen-usability checks.
- A brief compiler and optional standalone Gemini helper; no Python third-party libraries.
- An original illustrative sample, not a quality benchmark or a guarantee of results.

Installing a Skill does **not** add an image model. Codex uses its session image tool when available. Claude Code needs a configured image MCP/API. Claude Code cloud also requires signing in and selecting a repository you can access; fork this project if needed. Subscription/model/provider availability depends on your own account.

## Provenance & rights

ROCC’s general direction is inferred from finished images (460 metadata records,71 visual samples); historical prompts were not provided. The three franchise studies are new and have not had comparative quality evaluation. No model was trained; the old wallpaper library is not included.

Dragon Ball, Naruto and Doraemon are study-direction names, not official affiliation or a character/commercial license. Use newly composed scenes and check rights for your intended use. Code and instructions are MIT; third-party characters and references are not covered. The included example uses an original subject generated with the session image tool, model undisclosed.

## Official capabilities checked 2026-10-26

[Codex deep links](https://learn.chatgpt.com/docs/reference/commands#deep-links) · [Codex Skills](https://learn.chatgpt.com/docs/build-skills) · [Claude Code Skills](https://code.claude.com/docs/en/skills) · [Claude Code prefilled tasks](https://code.claude.com/docs/en/web-quickstart#pre-fill-sessions).
