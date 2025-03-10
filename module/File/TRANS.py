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

    RM_EXCLUDED_ADDRESS = (
        re.compile(r"/note/*", flags = re.IGNORECASE),
        re.compile(r"/script/*", flags = re.IGNORECASE),
        re.compile(r"/comment/*", flags = re.IGNORECASE),
        re.compile(r"filename", flags = re.IGNORECASE),
        re.compile(r"Tilesets/\d+/name", flags = re.IGNORECASE),
        re.compile(r"MapInfos/\d+/name", flags = re.IGNORECASE),
        re.compile(r"Animations/\d+/name", flags = re.IGNORECASE),
        re.compile(r"Map\d+/events/\d+/name", flags = re.IGNORECASE),
    )

    WOLF_EXCLUDED_TAG = (
    )

    WOLF_EXCLUDED_ADDRESS = (
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
                if engine in ("2k", "RMJDB", "rmvx", "rmvxace", "rmmv", "rmmz"):
                    re_tag = TRANS.RM_EXCLUDED_TAG
                    re_address = TRANS.RM_EXCLUDED_ADDRESS
                    text_type = CacheItem.TextType.RPGMAKER
                elif engine in ("wolf", ""):
                    re_tag = TRANS.WOLF_EXCLUDED_TAG
                    re_address = TRANS.WOLF_EXCLUDED_ADDRESS
                    text_type = CacheItem.TextType.NONE
                else:
                    re_tag = ()
                    re_address = ()
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
                        elif self.filter_by_tag(tag, re_tag) or self.filter_by_rule(context, re_address):
                            items.append(
                                CacheItem({
                                    "src": data[0],
                                    "dst": data[0],
                                    "tag": tag,
                                    "row": len(items),
                                    "file_type": CacheItem.FileType.TRANS,
                                    "file_path": rel_path,
                                    "text_type": text_type,
                                    "extra_field": "gold",
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
                        target_items = [item for item in items if item.get_tag() == tag]

                        tags: list[str] = []
                        data: list[str] = []
                        for i, item in enumerate(target_items):
                            data.append((item.get_src(), item.get_dst()))
                            if i >= len(json_data["project"]["files"][tag]["tags"]):
                                t = set()
                            elif json_data["project"]["files"][tag]["tags"][i] is None:
                                t = set()
                            else:
                                t = set(json_data["project"]["files"][tag]["tags"][i])
                            if item.get_extra_field() != "":
                                t.add(item.get_extra_field())
                            tags.append(list(t))
                        json_data["project"]["files"][tag]["tags"] = tags
                        json_data["project"]["files"][tag]["data"] = data

                # 写入文件
                json.dump(json_data, writer, indent = 4, ensure_ascii = False)