import re

from module.Cache.CacheItem import CacheItem
from module.TextHelper import TextHelper

class RuleFilter():

    PREFIX = (
        "MapData/",
        "SE/",
        "BGS",
        "0=",
        "BGM/",
        "FIcon/",
        "<input type=",
        "width:",
        "<div ",
        "EV0"
    )

    SUFFIX = (
        ".mp3",
        ".wav",
        ".ogg",
        ".png",
        ".jpg",
        ".gif",
        ".psd",
        ".webp",
        ".heif",
        ".heic",
        ".txt",
        ".7z",
        ".gz",
        ".rar",
        ".zip",
        ".json",
    )

    def __init__(self) -> None:
        super().__init__()

    def filter(item: CacheItem) -> bool:
        src: str = item.get_src()

        # 空字符串
        if src == "":
            return True

        # 仅包含空白符、数字字符、标点符号
        if all(c.isspace() or c.isnumeric() or TextHelper.is_punctuation(c) for c in src):
            return True

        # 以扩展名结尾
        if any(src.lower().endswith(suffix) for suffix in RuleFilter.SUFFIX):
            return True

        # 以常见代码开头
        if any(src.lower().startswith(suffix) for suffix in RuleFilter.PREFIX):
            return True