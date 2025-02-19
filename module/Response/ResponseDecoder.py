import re

import json_repair as repair

from base.Base import Base
from module.Localizer.Localizer import Localizer

class ResponseDecoder(Base):

    # 前缀和后缀
    RE_STRIP_DICT = re.compile(r"^[^\{]*|[^\}]*$", flags = re.DOTALL)
    RE_STRIP_LIST = re.compile(r"^[^\[]*|[^\]]*$", flags = re.DOTALL)

    # 匹配翻译条目
    RE_TRANSLATION = re.compile(r"['\"‘“](\d+)['\"’”]\s*:\s*['\"‘“](.+?)['\"’”][,，\}\n]", flags = re.DOTALL)

    # 匹配术语条目
    RE_GLOSSARY = re.compile(r"\{[^:]+?:[^:]+?:[^:]+?:[^:]+?\}", flags = re.DOTALL)

    # 混合块分割
    RE_MIX_SPLIT = re.compile(r"['\"‘“]name['\"’”]\s*:", flags = re.DOTALL)

    # 翻译块识别
    RE_MIX_TRANSLATION = re.compile(r"['\"‘“]0['\"’”]\s*:", flags = re.DOTALL)

    def __init__(self) -> None:
        super().__init__()

    # 解析文本
    def decode(self, response: str) -> dict[str, str]:
        log = ""
        dst = None

        # 尝试反序列化
        dst = repair.loads(response)
        if isinstance(dst, dict) and isinstance(dst.get("0"), str):
            log = Localizer.get().response_decoder_translation_by_json.replace("{COUNT}", f"{len(dst)}")
        else:
            dst = None

        # 尝试规则解析
        if dst is None:
            dst = self.decode_translation_by_rule(response)
            if isinstance(dst, dict) and isinstance(dst.get("0"), str):
                log = Localizer.get().response_decoder_translation_by_rule.replace("{COUNT}", f"{len(dst)}")
            else:
                dst = None

        # 返回默认值
        return dst if dst is not None else {}, [], log

    # 解析混合文本
    def decode_mix(self, response: str) -> tuple[dict[str, str], list[dict[str, str]], str]:
        log = ""
        dst = None
        glossary = None

        # 尝试反序列化
        json_data = repair.loads(response)
        if isinstance(json_data, dict):
            dst = json_data.get("translation")
            glossary = json_data.get("name")

            # 有效性验证
            if isinstance(dst, dict) and isinstance(dst.get("0"), str):
                log = log + "\n" + Localizer.get().response_decoder_translation_by_json.replace("{COUNT}", f"{len(dst)}")
            else:
                dst = None
            if isinstance(glossary, list) and glossary != [] and isinstance(glossary[0], dict):
                log = log + "\n" + Localizer.get().response_decoder_glossary_by_json.replace("{COUNT}", f"{len(glossary)}")
            else:
                glossary = None

        if dst is None or glossary is None:
            chunks = ResponseDecoder.RE_MIX_SPLIT.split(response)
            chunk_dst = ""
            chunk_glossary = ""
            for chunk in chunks:
                if ResponseDecoder.RE_MIX_TRANSLATION.findall(chunk) != []:
                    chunk_dst = chunk
                else:
                    chunk_glossary = chunk

            # 尝试规则解析
            if dst is None:
                dst = self.decode_translation_by_rule(chunk_dst)
                if isinstance(dst, dict) and isinstance(dst.get("0"), str):
                    log = log + "\n" + Localizer.get().response_decoder_translation_by_rule.replace("{COUNT}", f"{len(dst)}")
                else:
                    dst = None
            if glossary is None:
                glossary = self.decode_glossary_by_rule(chunk_glossary)
                if isinstance(glossary, list) and glossary != [] and isinstance(glossary[0], dict):
                    log = log + "\n" + Localizer.get().response_decoder_glossary_by_rule.replace("{COUNT}", f"{len(glossary)}")
                else:
                    glossary = None

        # 返回默认值
        return dst if dst is not None else {}, glossary if glossary is not None else [], log

    # 解析翻译文本 - 通过规则解析
    def decode_translation_by_rule(self, response: str) -> dict[str, str]:
        if "{" in response and "}" in response:
            response = ResponseDecoder.RE_STRIP_DICT.sub("", response)

        return {k: v.replace("\\\"", "\"").replace("\\\'", "\'") for k, v in ResponseDecoder.RE_TRANSLATION.findall(response)}

    # 解析术语文本 - 通过规则解析
    def decode_glossary_by_rule(self, response: str) -> dict[str, str]:
        json_data = []

        if "[" in response and "]" in response:
            response = ResponseDecoder.RE_STRIP_LIST.sub("", response)

        for item in ResponseDecoder.RE_GLOSSARY.findall(response):
            json_data.append(repair.loads(item))

        return json_data