<h1><p align='center' >LinguaGacha</p></h1>
<div align=center><img src="https://img.shields.io/github/v/release/neavo/LinguaGacha"/>   <img src="https://img.shields.io/github/license/neavo/LinguaGacha"/>   <img src="https://img.shields.io/github/stars/neavo/LinguaGacha"/></div>
<p align='center'>使用 AI 能力一键翻译 小说、游戏、字幕 等文本内容的次世代文本翻译器</p>


&ensp;
&ensp;


## 概述 📢
- [LinguaGacha](https://github.com/neavo/LinguaGacha) (/ˈlɪŋɡwə ˈɡɑːtʃə/)，简称 `LG`，使用 AI 技术次世代文本翻译器
- 支持 `中` `英` `日` `韩` `俄` 等多种语言的一键互译
- 支持 纯文本、小说、字幕、游戏文本 等多种文本格式
- 支持 `Claude`、`ChatGTP`、`DeepSeek`、`SakuraLLM` 等各种本地或在线接口
- Less is More，更少的设置选项，更好的默认设置，减少烧脑的功能逻辑与设置，开箱即用！

## 特别说明 ⚠️
- 如您在翻译过程中使用了 [LinguaGacha](https://github.com/neavo/LinguaGacha) ，请在作品信息或发布页面的显要位置进行说明！
- 如您的项目涉及任何商业行为或者商业收益，在使用 [LinguaGacha](https://github.com/neavo/LinguaGacha)  前，请先与作者联系以获得授权！

## 配置要求 🖥️
- 任意兼容 `OpenAI` `Google` `Anthropic` `SakuraLLM` 标准的 AI 大模型接口
- 也可以使用 [本地模型一键包](https://github.com/neavo/OneClickLLAMA) 来获取完全免费的服务（需至少 8G 显存的独立显卡，Nvidia 显卡最佳）

## 使用流程 🛸
- 从 [发布页](https://github.com/neavo/LinguaGacha/releases) 下载应用
- 双击 `01_启动应用.bat` 启动应用
  - 在 `接口管理` 中添加接口信息并激活接口
  - 在 `项目设置` 中设置原文语言、译文语言等必要信息
  - 将要翻译的文本文件拷入输入文件夹，在 `开始翻译` 中点击开始翻译

## 文本格式 🏷️
- `LG` 将在任务开始时扫描输入文件夹及其子文件夹找到所有支持格式的文件
- 大部分主流的 `小说` 和 `游戏脚本` 数据格式都可以直接或者通过转换被 `LG` 识别
  - 包括但是不限于
    - 纯文本（.txt）
    - SRT 字幕（.srt）
    - [MTool](https://afdian.com/a/AdventCirno) 导出游戏文本（.json）
    - [SExtractor](https://github.com/satan53x/SExtractor) 导出游戏文本（.txt .json .xlsx）
    - [Translator++](https://dreamsavior.net/translator-plusplus/) 导出游戏文本（.xlsx）
  - 更多格式将持续添加，你也可以在 [ISSUES](https://github.com/neavo/LinguaGacha/issues) 中提出你的需求

## 近期更新 📅
- 20250207 v0.1.3
  - 多处 `UI` 与 `交互` 逻辑优化，包括但是不限于：
    - 支持混合文件格式翻译
    - 支持同时创建多个相同平台接口
    - 支持直接在 `译前替换` 页面导入 `Actor.json` 文件
  - 显著提升了 `换行符` 与 `代码段` 的保留率
    - 得以于此，`翻译速度` 和 `Token 消耗` 也得到了优化
  - 显著提升了思考模型（如 `DeepSeek-R1` ）的翻译效果
  - 显著提升了本地通用小模型（如 `Qwen2.5-14B` ）的翻译效果
 
## 常见问题 📥
- [LinguaGacha](https://github.com/neavo/LinguaGacha) 与 [AiNiee](https://github.com/NEKOparapa/AiNiee) 的关系
  - `LinguaGacha` 是在 `AiNiee v5` 版本的基础上进行重构的全新翻译器应用
    - 如果说 `AiNiee v5` 是一台功能强大但是需要调教的安卓手机
    - 那么 `LinguaGacha` 就是一台的苹果手机，开箱即用，无需设置，快速且优质
  - `LinguaGacha` 诞生的初衷就是希望可以满足不同用户的需求
  - `LinguaGacha` 的作者也是 `AiNiee v5` 的主要开发与维护者之一

## 开发计划 📈
- [ ] 简繁转换
- [x] 支持 .srt 等字幕文件
- [ ] 支持 .epub 等电子书文件
