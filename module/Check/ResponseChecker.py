import math
from base.Base import Base

class ResponseChecker(Base):

    class Error():

        UNKNOWN: str = "未知"
        NONE: str = "没有有效数据"
        EMPTY_LINE: str = "译文包含空行"
        LINE_COUNT: str = "未通过行数检查"
        SIMILARITY: str = "部分条目中原文译文相似"

    def __init__(self, config: dict) -> None:
        super().__init__()

        # 初始化
        self.config = config

        # 计算轮数阈值，即在此轮次及后续轮次，任务一定是单条目任务
        self.round_threshold = math.ceil(math.log(config.get("task_token_limit"), 2))

    def check(self, src_dict: dict[str, str], dst_dict: dict[str, str], current_round: int) -> str:
        # 没有有效数据
        if len(dst_dict) == 0:
            return ResponseChecker.Error.NONE, None

        # 译文包含空行
        # if any(v == "" or v == None for v in dst_dict.values()):
        #     return ResponseChecker.Error.EMPTY_LINE, None

        # 未通过行数检查
        if not (
            len(src_dict) == len(dst_dict) # 原文与译文行数一致
            and all(str(key) in dst_dict for key in range(len(dst_dict))) # 译文的 Key 的值为从 0 开始的连续数值字符
        ):
            return ResponseChecker.Error.LINE_COUNT, None

        # 部分条目中原文译文相似
        if len(dst_dict) > 1 and current_round <= self.round_threshold:
            return self.chech_similarity(src_dict, dst_dict)

        return None, None

    # 部分条目中原文译文相似
    def chech_similarity(self, src_dict: dict[str, str], dst_dict: dict[str, str]) -> str:
        data = []
        for src, dst in zip(src_dict.values(), dst_dict.values()):
            if src == dst and "[占位符]" not in src:
                data.append(1)
            else:
                data.append(0)

        return ResponseChecker.Error.SIMILARITY if sum(data) >= 1 else None, data