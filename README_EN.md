<div align=center><img src="https://github.com/user-attachments/assets/cdf990fb-cf03-4370-a402-844f87b2fab8" width="256px;"></div>
<div align=center><img src="https://img.shields.io/github/v/release/neavo/LinguaGacha"/>   <img src="https://img.shields.io/github/license/neavo/LinguaGacha"/>   <img src="https://img.shields.io/github/stars/neavo/LinguaGacha"/></div>
<p align='center'>Next-generation text translator utilizing AI capabilities for one-click translation of novels, games, subtitles, and more</p>

&ensp;
&ensp;

## README 🌍
- [ [中文](./README.md) ] | [ [English](./README_EN.md) ] | [ [日本語](./README_JA.md) ]

## Overview 📢
- [LinguaGacha](https://github.com/neavo/LinguaGacha) (/ˈlɪŋɡwə ˈɡɑːtʃə/), abbreviated as `LG`, is an AI-powered next-generation text translator
- Out of the box, (almost) no setup needed
- Supports one-click translation between 13 languages
  - including `Chinese`, `English`, `Japanese`, `Korean`, `Russian`, `German`, `French`, `Italian`, etc.
- Supports various text types and formats such as `subtitles`, `e-books`, and `game text`
- Supports both local and online interfaces such as `Claude`, `ChatGPT`, `DeepSeek`, `SakuraLLM`

> <img src="https://github.com/user-attachments/assets/859a7e32-bf35-4572-8460-4ecb11a8d20c" style="width: 80%;">

> <img src="https://github.com/user-attachments/assets/c0d7e898-f6fa-432f-a3cd-e231b657c4b5" style="width: 80%;">

## Special Notice ⚠️
- If you use [LinguaGacha](https://github.com/neavo/LinguaGacha) during translation, please include clear attribution in prominent locations of your work's information or release pages!
- For projects involving commercial activities or profits, please contact the author for authorization before using [LinguaGacha](https://github.com/neavo/LinguaGacha)!

## Key Features 📌
- Lightning-fast translation speed: 10 seconds for subtitles, 1 minute for novels, 5 minutes for games
- Automatic glossary generation ensuring consistent terminology (e.g., character names) throughout the work `👈👈 Exclusive Feature`
- Optimal translation quality from flagship models (e.g., DeepSeek-R1) to local small models (e.g., Qwen2.5-7B)
- `100%` accurate preservation of text formatting and embedded codes, significantly reducing post-processing work - ideal for embedded localization `👈👈 Exclusive Feature`

## System Requirements 🖥️
- Compatible with AI model interfaces following `OpenAI`, `Google`, `Anthropic`, `SakuraLLM` standards
- Compatible with [KeywordGacha](https://github.com/neavo/KeywordGacha) `👈👈 Next-generation tool for AI-powered glossary generation`

## Workflow 🛸
- Download application from [Releases page](https://github.com/neavo/LinguaGacha/releases)
- Obtain a reliable AI model interface (choose one):
  - [Local API - Tutorial](https://github.com/neavo/OneClickLLAMA) (Free, requires ≥8GB VRAM GPU, Nvidia recommended)
  - [DeepSeek - Tutorial](https://github.com/neavo/LinguaGacha/wiki/DeepSeek) (Paid, cost-effective, fast, high-quality, no GPU required) `👈👈 Recommended`
- Prepare source text:
  - `Subtitles`/`E-books` typically require no preprocessing
  - `Game texts` need extraction using appropriate tools for specific game engines
- Launch application via `app.exe`:
  - Configure essential settings (source/target languages) in `Project Settings`
  - Copy files to input folder (default: `input`), start translation in `Begin Translation`
- Visit [Wiki](https://github.com/neavo/LinguaGacha/wiki) for detailed guides or share experiences in [Discussions](https://github.com/neavo/LinguaGacha/discussions)

## Supported Formats 🏷️
- Processes all supported files in input folder (including subdirectories):
  - Subtitles (.srt .ass)
  - E-books (.txt .epub)
  - [RenPy](https://www.renpy.org) exports (.rpy)
  - [MTool](https://afdian.com/a/AdventCirno) exports (.json)
  - [SExtractor](https://github.com/satan53x/SExtractor) exports (.txt .json .xlsx)
  - [Translator++](https://dreamsavior.net/translator-plusplus) exports (.xlsx)
- See [Wiki - Supported Formats](https://github.com/neavo/LinguaGacha/wiki/%E6%94%AF%E6%8C%81%E7%9A%84%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F) for examples. Submit format requests via [ISSUES](https://github.com/neavo/LinguaGacha/issues)

## Recent Updates 📅
- 20250304 v0.9.2
  - OPT - Keep as much of the original style as possible for EPUB
  - Minor fix and update

- 20250302 v0.9.1
  - OPT - Significantly cut down on the number of rounds and time needed for translation.

- 20250302 v0.9.0
 - Internationalization Language Special
   - Added support for `German`, `French`, `Spanish`, `Italian`, `Portuguese`, `Thai`, `Indonesian` and `Vietnamese`
- Welcome to provide feedback on the translation quality and usage experience of these newly added languages
 - OPT - Support for list tags and EPUB3 table of contents.
 - OPT - Dynamically constructed translation commands currently only take effect for certain text types

- 20250228 v0.8.1
  - FIX - Minor issues with untranslated text and code detection logic

- 20250228 v0.8.0
  - NEW - Dynamic construction of translation instructions function
    - Engine dynamically analyzes the text of each task and generates corresponding instructions
    - Significantly improved the code retention rate for RenPy and RPGMaker engine games

## FAQ 📥
- Relationship between [LinguaGacha](https://github.com/neavo/LinguaGacha) and [AiNiee](https://github.com/NEKOparapa/AiNiee)
  - `LinguaGacha` is a complete rewrite incorporating lessons from `AiNiee`
  - `LinguaGacha`'s developer was a main contributor to `AiNiee v5`

## Support 😥
- Runtime logs are stored in `log` folder
- Please attach relevant logs when reporting issues
- You can also join our groups for discussion and feedback:
  - Discord - https://discord.gg/kX7UnxnKje
