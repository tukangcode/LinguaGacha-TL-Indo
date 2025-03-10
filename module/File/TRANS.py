import os
import re
import shutil

import rapidjson as json

from base.Base import Base
from module.Cache.CacheItem import CacheItem

class TRANS(Base):

    RM_EXCLUDED_TAG = (
        re.compile(r"\.js$", flags = re.IGNORECASE),
    )

    RM_EXCLUDED_RULE = (
        re.compile(r"/note/*", flags = re.IGNORECASE),
        re.compile(r"/script/*", flags = re.IGNORECASE),
        re.compile(r"/comment/*", flags = re.IGNORECASE),
        re.compile(r"animations/\d+/name/*", flags = re.IGNORECASE),
        re.compile(r"map\d+/events/\d+/name/*", flags = re.IGNORECASE),
    )

    WOLF_EXCLUDED_TAG = (
    )

    WOLF_EXCLUDED_RULE = (
        re.compile(r"/note/*", flags = re.IGNORECASE),
        re.compile(r"/script/*", flags = re.IGNORECASE),
        re.compile(r"/comment/*", flags = re.IGNORECASE),
    )

    def __init__(self, config: dict) -> None:
        super().__init__()

        # 初始化
        self.config: dict = config
        self.input_path: str = config.get("input_folder")
        self.output_path: str = config.get("output_folder")
        self.source_language: str = config.get("source_language")
        self.target_language: str = config.get("target_language")

    # 标签过滤
    def filter_by_tag(self, tag: str, re_tag: list[re.Pattern]) -> bool:
        return any(len(v.findall(tag)) > 0 for v in re_tag)

    # 规则过滤
    def filter_by_rule(self, context: list[str], re_rule: list[re.Pattern]) -> bool:
        context = "\n".join(context)
        for rule in re_rule:
            if len(rule.findall(context)) > 0:
                return True

        return False

    # 读取
    def read_from_path(self, abs_paths: list[str]) -> list[CacheItem]:
        items = []
        for abs_path in set(abs_paths):
            # 获取相对路径
            rel_path = os.path.relpath(abs_path, self.input_path)

            # 将原始文件复制一份
            os.makedirs(os.path.dirname(f"{self.output_path}/cache/temp/{rel_path}"), exist_ok = True)
            shutil.copy(abs_path, f"{self.output_path}/cache/temp/{rel_path}")

            # 数据处理
            with open(abs_path, "r", encoding = "utf-8-sig") as reader:
                json_data = json.load(reader)

                # 有效性校验
                if not isinstance(json_data, dict):
                    continue

                # 获取项目信息
                project: dict = json_data.get("project", {})
                engine: str = project.get("gameEngine", "")

                # 设置排除规则
                if engine in ("2k", "rmxp", "rmvx", "rmvxace", "rmmv", "rmmz"):
                    re_tag = TRANS.RM_EXCLUDED_TAG
                    re_rule = TRANS.RM_EXCLUDED_RULE
                    text_type = CacheItem.TextType.RPGMAKER
                elif engine in ("wolf", ""):
                    re_tag = TRANS.WOLF_EXCLUDED_TAG
                    re_rule = TRANS.WOLF_EXCLUDED_RULE
                    text_type = CacheItem.TextType.NONE
                else:
                    re_tag = ()
                    re_rule = ()
                    text_type = CacheItem.TextType.NONE

                # 处理数据
                for tag, entry in project.get("files", {}).items():
                    data: list[str] = []
                    context: list[str] = []
                    for data, context in zip(entry.get("data", []), entry.get("context", [])):
                        # 有效性校验
                        if not isinstance(data, list) or len(data) == 0 or not isinstance(data[0], str):
                            continue

                        if len(data) >= 2 and isinstance(data[1], str) and data[1].strip() != "":
                            items.append(
                                CacheItem({
                                    "src": data[0],
                                    "dst": data[1],
                                    "tag": tag,
                                    "row": len(items),
                                    "file_type": CacheItem.FileType.TRANS,
                                    "file_path": rel_path,
                                    "text_type": text_type,
                                    "status": Base.TranslationStatus.EXCLUDED,
                                })
                            )
                        elif self.filter_by_tag(tag, re_tag) or self.filter_by_rule(context, re_rule):
                            items.append(
                                CacheItem({
                                    "src": data[0],
                                    "dst": data[0],
                                    "tag": tag,
                                    "row": len(items),
                                    "file_type": CacheItem.FileType.TRANS,
                                    "file_path": rel_path,
                                    "text_type": text_type,
                                    "status": Base.TranslationStatus.EXCLUDED,
                                })
                            )
                        else:
                            items.append(
                                CacheItem({
                                    "src": data[0],
                                    "dst": data[0],
                                    "tag": tag,
                                    "row": len(items),
                                    "file_type": CacheItem.FileType.TRANS,
                                    "file_path": rel_path,
                                    "text_type": text_type,
                                    "status": Base.TranslationStatus.UNTRANSLATED,
                                })
                            )

        return items

    # 写入
    def write_to_path(self, items: list[CacheItem]) -> None:
        # 筛选
        target = [
            item for item in items
            if item.get_file_type() == CacheItem.FileType.TRANS
        ]

        # 按文件路径分组
        data: dict[str, list[str]] = {}
        for item in target:
            data.setdefault(item.get_file_path(), []).append(item)

        # 分别处理每个文件
        for rel_path, items in data.items():
            # 按行号排序
            items = sorted(items, key = lambda x: x.get_row())

            # 处理文件
            abs_path = f"{self.output_path}/{rel_path}"
            os.makedirs(os.path.dirname(abs_path), exist_ok = True)
            with open(abs_path, "w", encoding = "utf-8") as writer:
                with open(f"{self.output_path}/cache/temp/{rel_path}", "r", encoding = "utf-8-sig") as reader:
                    json_data = json.load(reader)

                    # 有效性校验
                    if not isinstance(json_data, dict):
                        continue

                    # 获取项目信息
                    project: dict = json_data.get("project", {})
                    files: dict = project.get("files", {})

                    # 处理数据
                    for tag in files.keys():
                        json_data["project"]["files"][tag]["data"] = [
                            [item.get_src(), item.get_dst()]
                            for item in items if item.get_tag() == tag
                        ]

                # 写入文件
                json.dump(json_data, writer, indent = 4, ensure_ascii = False)