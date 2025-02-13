<h1><p align='center' >LinguaGacha</p></h1>
<div align=center><img src="https://img.shields.io/github/v/release/neavo/LinguaGacha"/>   <img src="https://img.shields.io/github/license/neavo/LinguaGacha"/>   <img src="https://img.shields.io/github/stars/neavo/LinguaGacha"/></div>
<p align='center'>使用 AI 能力一键翻译 小说、游戏、字幕 等文本内容的次世代文本翻译器</p>


&ensp;
&ensp;


## 概述 📢
- [LinguaGacha](https://github.com/neavo/LinguaGacha) (/ˈlɪŋɡwə ˈɡɑːtʃə/)，简称 `LG`，使用 AI 技术次世代文本翻译器
- 支持 `中` `英` `日` `韩` `俄` 等多种语言的一键互译
- 支持 `小说`、`字幕`、`游戏文本` 等多种文本类型与文本格式
- 支持 `Claude`、`ChatGPT`、`DeepSeek`、`SakuraLLM` 等各种本地或在线接口
- Less is More，更少的设置选项，更好的默认设置，减少烧脑的功能逻辑与设置，开箱即用！

> ![QQ截图20250213112409](https://github.com/user-attachments/assets/202d43bf-e2dc-427b-9bad-c5701b57de7a)


## 特别说明 ⚠️
- 如您在翻译过程中使用了 [LinguaGacha](https://github.com/neavo/LinguaGacha) ，请在作品信息或发布页面的显要位置进行说明！
- 如您的项目涉及任何商业行为或者商业收益，在使用 [LinguaGacha](https://github.com/neavo/LinguaGacha)  前，请先与作者联系以获得授权！

## 功能优势 📌
- 极快的翻译速度，十秒钟一份字幕，一分钟一本小说，五分钟一部游戏
- 自动生成术语表，保证角色姓名等专有名词在整部作品中的译名统一  `独家绝技` 👈👈
- 最优的翻译质量，无论是 旗舰模型 `诸如 DeepSeek-R1` 还是 本地小模型 `诸如 Qwen2.5-7B` 
- 精确的格式与样式控制，`100%` 精确还原文本样式，显著减少游戏文本内嵌的工作量  `独家绝技` 👈👈

## 配置要求 🖥️
- 兼容 `OpenAI` `Google` `Anthropic` `SakuraLLM` 标准的 AI 大模型接口
- 兼容 [KeywordGacha](https://github.com/neavo/KeywordGacha) `使用 AI 能力一键生成术语表的次世代工具` 👈👈

## 使用流程 🛸
- 从 [发布页](https://github.com/neavo/LinguaGacha/releases) 下载应用
- 获取一个可靠的 AI 大模型接口，以下两种选择其一：
  - [本地接口 - 点击查看教程](https://github.com/neavo/OneClickLLAMA)，免费，需至少 8G 显存的独立显卡，Nvidia 显卡为佳
  - [DeepSeek - 点击查看教程](https://github.com/neavo/LinguaGacha/wiki/DeepSeek)，需付费但便宜，速度快，质量高，无显卡要求 `👈👈 推荐`
- 准备要翻译的文本
  - `字幕`、`电子书` 等一般不需要预处理
  - `游戏文本` 需要根据游戏引擎选择合适的工具进行提取
- 双击 `01_启动应用.bat` 启动应用
  - 在 `项目设置` 中设置原文语言、译文语言等必要信息
  - 将要翻译的文本文件复制到输入文件夹（默认为 `input` 文件夹），在 `开始翻译` 中点击开始翻译

## 文本格式 🏷️
- 在任务开始时，`LG` 将扫描输入文件夹及其子文件夹寻找目标文件，包括但是不限于：
  - 字幕（.srt .ass）
  - 电子书（.txt .epub）
  - [RenPy](https://www.renpy.org) 导出游戏文本（.rpy）
  - [MTool](https://afdian.com/a/AdventCirno) 导出游戏文本（.json）
  - [SExtractor](https://github.com/satan53x/SExtractor) 导出游戏文本（.txt .json .xlsx）
  - [Translator++](https://dreamsavior.net/translator-plusplus) 导出游戏文本（.xlsx）
- 更多格式将持续添加，你也可以在 [ISSUES](https://github.com/neavo/LinguaGacha/issues) 中提出你的需求

## 近期更新 📅
- 20250213 v0.4.5
  - 新增 自动术语表功能
  - 调整 支持更多种类的 XLSX 文件
  - 调整 EPUB、MESSAGEJSON 读写逻辑
  - 调整 优化 UTF8-BOM 文件的兼容性
  - 修正 .ass .epub 不能正确保存翻译结果的问题
  - 修正 返回结果数据结构错误时导致翻译卡死的问题

- 20250211 v0.3.4
  - 调整 优化漏翻检查规则

- 20250210 v0.3.3
  - 新增 支持火山引擎
  - 修正 正确的识别 R1 官方格式思考内容

- 20250210 v0.3.2
  - 调整 显著降低了漏翻情况的发生

- 20250210 v0.3.1
  - 新增 支持 [RenPy](https://www.renpy.org) 导出游戏文本（.rpy）

## 常见问题 📥
- [LinguaGacha](https://github.com/neavo/LinguaGacha) 与 [AiNiee](https://github.com/NEKOparapa/AiNiee) 的关系
  - `LinguaGacha` 是在 `AiNiee v5` 版本的基础上进行重构的全新 AI 翻译应用
    - 如果 `AiNiee v5` 是一台功能强大但是需要调教的安卓手机
    - 那么 `LinguaGacha` 就是一台的苹果手机，开箱即用，无需设置，快速更优质
  - `LinguaGacha` 的作者也是 `AiNiee v5` 的主要开发与维护者之一
