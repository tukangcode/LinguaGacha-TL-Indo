from base.Base import Base
from module.TextHelper import TextHelper

class ResponseChecker(Base):

    class Error():

        UNKNOWN: str = "未知"
        NONE: str = "数据解析错误"
        LINE: str = "未通过行数检查"
        ORGINAL: str = "部分译文未得到翻译"

    def __init__(self, config: dict) -> None:
        super().__init__()

        # 初始化
        self.config = config

    def check(self, src_dict: dict[str, str], dst_dict: dict[str, str]) -> str:
        # 数据解析错误
        if len(dst_dict) == 0:
            return ResponseChecker.Error.NONE

        # 未通过行数检查
        if not (
            len(src_dict) == len(dst_dict) # 原文与译文行数一致
            and all(str(key) in dst_dict for key in range(len(dst_dict))) # 译文的 Key 的值为从 0 开始的连续数值字符
        ):
            return ResponseChecker.Error.LINE

        # 部分译文未得到翻译
        # result = False
        # for src, dst in zip(src_dict.values(), dst_dict.values()):
        #     x = []
        #     for char in src:
        #         if not TextHelper.is_punctuation(char):
        #             x.append(char)
        #     x = "".join(x)
        #     y = []
        #     for char in dst:
        #         if not TextHelper.is_punctuation(char):
        #             y.append(char)
        #     y = "".join(y)
        #     if not TextHelper.is_all_cjk(x) and x == y:
        #         result = True
        # if result == True:
        #     return ResponseChecker.Error.ORGINAL

        # if any("[占位符]" != src_dict.get(k) and v.strip() == src_dict.get(k).strip() for k, v in dst_dict.items()):
        #     return ResponseChecker.Error.ORGINAL

        return None