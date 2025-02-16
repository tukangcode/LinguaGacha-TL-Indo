from typing import Literal, LiteralString
from base.Base import Base

class PromptBuilder(Base):

    def __init__(self, config: dict) -> None:
        super().__init__()

        # 初始化
        self.config = config
        self.target_language = config.get("target_language")
        self.auto_glossary_enable = config.get("auto_glossary_enable")
        self.glossary_data = config.get("glossary_data")

        self.base: str = None
        self.prefix: str = None
        self.suffix: str = None
        self.suffix_glossary: str = None

    def get_base(self, language: str) -> str:
        if self.base == None:
            with open(f"resource/prompt/{language.lower()}/base.txt", "r", encoding = "utf-8-sig") as reader:
                self.base = reader.read().strip()

        return self.base

    def get_prefix(self, language: str) -> str:
        if self.prefix == None:
            with open(f"resource/prompt/{language.lower()}/prefix.txt", "r", encoding = "utf-8-sig") as reader:
                self.prefix = reader.read().strip()

        return self.prefix

    def get_suffix(self, language: str) -> str:
        if self.suffix == None:
            with open(f"resource/prompt/{language.lower()}/suffix.txt", "r", encoding = "utf-8-sig") as reader:
                self.suffix = reader.read().strip()

        return self.suffix

    def get_suffix_glossary(self, language: str) -> str:
        if self.suffix_glossary == None:
            with open(f"resource/prompt/{language.lower()}/suffix_glossary.txt", "r", encoding = "utf-8-sig") as reader:
                self.suffix_glossary = reader.read().strip()

        return self.suffix_glossary

    # 获取主提示词
    def build_main(self) -> str:
        if self.target_language == Base.Language.ZH:
            target_language = "中文"
            prompt_language = Base.Language.ZH
        elif self.target_language == Base.Language.EN:
            target_language = "English"
            prompt_language = Base.Language.EN
        elif self.target_language == Base.Language.JA:
            target_language = "Japanese"
            prompt_language = Base.Language.EN
        elif self.target_language == Base.Language.KO:
            target_language = "Korean"
            prompt_language = Base.Language.EN
        elif self.target_language == Base.Language.RU:
            target_language = "Russian"
            prompt_language = Base.Language.EN

        if prompt_language == Base.Language.ZH:
            custom_prompt_enable = self.config.get("custom_prompt_zh_enable")
            custom_prompt_data = self.config.get("custom_prompt_zh_data")
        else:
            custom_prompt_enable = self.config.get("custom_prompt_en_enable")
            custom_prompt_data = self.config.get("custom_prompt_en_data")

        self.get_base(prompt_language)
        self.get_prefix(prompt_language)
        self.get_suffix(prompt_language)
        self.get_suffix_glossary(prompt_language)

        # 判断是否启用自定义提示词
        if custom_prompt_enable == False:
            base = self.base
        else:
            base = custom_prompt_data

        # 判断是否启用自动术语表
        if self.auto_glossary_enable == False:
            suffix = self.suffix
        else:
            suffix = self.suffix_glossary

        return (self.prefix + "\n" + base + "\n" + suffix).replace("{target_language}", target_language)

    # 构造术语表
    def build_glossary(self, input_dict: dict) -> str:
        # 将输入字典中的所有值转换为集合
        lines = set(line for line in input_dict.values())

        # 筛选在输入词典中出现过的条目
        result = [
            v for v in self.glossary_data
            if any(v.get("src") in lines for lines in lines)
        ]

        # 构建文本
        dict_lines = []
        for item in result:
            src = item.get("src", "")
            dst = item.get("dst", "")
            info = item.get("info", "")

            if info == "":
                dict_lines.append(f"{src} -> {dst}")
            else:
                dict_lines.append(f"{src} -> {dst} #{info}")

        # 返回结果
        if dict_lines == []:
            return ""
        else:
            return (
                "术语表："
                + "\n" + "\n".join(dict_lines)
            )

    # 构造术语表
    def build_glossary_sakura(self, input_dict: dict) -> str:
        # 将输入字典中的所有值转换为集合
        lines = set(line for line in input_dict.values())

        # 筛选在输入词典中出现过的条目
        result = [
            v for v in self.glossary_data
            if any(v.get("src") in lines for lines in lines)
        ]

        # 构建文本
        dict_lines = []
        for item in result:
            src = item.get("src", "")
            dst = item.get("dst", "")
            info = item.get("info", "")

            if info == "":
                dict_lines.append(f"{src}->{dst}")
            else:
                dict_lines.append(f"{src}->{dst} #{info}")

        # 返回结果
        if dict_lines == []:
            return ""
        else:
            return "\n".join(dict_lines)