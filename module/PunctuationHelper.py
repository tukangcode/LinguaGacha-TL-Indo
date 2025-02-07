import re

class PunctuationHelper():

    # 检查项，主要是全半角标点之间的转换
    CHECK_ITEMS = (
        ("　", " "),                                        # 全角空格和半角空格之间的转换
        (" ", "　"),                                        # 全角空格和半角空格之间的转换
        ("：", ":"),
        (":", "："),
        ("·", "・"),
        ("・", "·"),
        ("?", "？"),
        ("？", "?"),
        ("!", "！"),
        ("！", "!"),
        ("\u002d", "\u2014", "\u2015"),                    # 破折号之间的转换，\u002d = - ，\u2014 = ― ，\u2015 = —
        ("\u2014", "\u002d", "\u2015"),                    # 破折号之间的转换，\u002d = - ，\u2014 = ― ，\u2015 = —
        ("\u2015", "\u002d", "\u2014"),                    # 破折号之间的转换，\u002d = - ，\u2014 = ― ，\u2015 = —
        ("<", "＜", "《"),
        (">", "＞", "》"),
        ("＜", "<", "《"),
        ("＞", ">", "》"),
        ("「", "‘", "“", "『"),
        ("」", "’", "”", "』"),
        ("『", "‘", "“", "「"),
        ("』", "’", "”", "」"),
        ("(", "（", "「", "‘", "“"),
        (")", "）", "」", "’", "”"),
        ("（", "(", "「", "‘", "“"),
        ("）", ")", "」", "’", "”"),
    )

    # 替换项
    REPLACE_ITEMS = (
        ("「", "‘", "“"),
        ("」", "’", "”"),
    )

    # 圆圈数字列表
    CIRCLED_NUMBERS = tuple(chr(i) for i in range(0x2460, 0x2474))                                      # ①-⑳
    CIRCLED_NUMBERS_CJK_01 = tuple(chr(i) for i in range(0x3251, 0x3260))                               # ㉑-㉟
    CIRCLED_NUMBERS_CJK_02 = tuple(chr(i) for i in range(0x32B1, 0x32C0))                               # ㊱-㊿
    CIRCLED_NUMBERS_ALL = ("",) + CIRCLED_NUMBERS + CIRCLED_NUMBERS_CJK_01 + CIRCLED_NUMBERS_CJK_02     # 开头加个空字符来对齐索引和数值

    # 预设编译正则
    PATTERN_ALL_NUM = re.compile(r"\d+|[①-⑳㉑-㉟㊱-㊿]", re.IGNORECASE)
    PATTERN_CIRCLED_NUM = re.compile(r"[①-⑳㉑-㉟㊱-㊿]", re.IGNORECASE)

    # 检查并替换
    def check_and_replace(src: str, dst: str) -> str:
        # 修复标点符号
        for target in PunctuationHelper.CHECK_ITEMS:
            if PunctuationHelper.check(src, dst, target) == True:
                dst = PunctuationHelper.replace(dst, target)

        # 修复圆圈数字
        dst = PunctuationHelper.fix_circled_numbers(src, dst)

        # 处理替换项目
        for target in PunctuationHelper.REPLACE_ITEMS:
            dst = PunctuationHelper.replace(dst, target)

        return dst

    # 检查
    def check(src: str, dst: str, target: tuple) -> tuple[str, bool]:
        num_s_x = src.count(target[0])
        num_s_y = sum(src.count(t) for t in target[1:])
        num_t_x = dst.count(target[0])
        num_t_y = sum(dst.count(t) for t in target[1:])

        # 首先，原文中的目标符号的数量应大于零，否则表示没有需要修复的标点
        # 然后，原文中目标符号和错误符号的数量不应相等，否则无法确定哪个符号是正确的
        # 然后，原文中的目标符号的数量应大于译文中的目标符号的数量，否则表示没有需要修复的标点
        # 最后，如果原文中目标符号的数量等于译文中目标符号与错误符号的数量之和，则判断为需要修复
        return num_s_x > 0 and num_s_x != num_s_y and num_s_x > num_t_x  and num_s_x == num_t_x + num_t_y

    # 替换
    def replace(dst: str, target: tuple) -> str:
        for t in target[1:]:
            dst = dst.replace(t, target[0])

        return dst

    # 安全转换字符串为整数
    def safe_int(s: str) -> int:
        result = -1

        try:
            result = int(s)
        except Exception:
            pass

        return result

    # 修复圆圈数字
    def fix_circled_numbers(src: str, dst: str) -> str:
        # 找出 src 与 dst 中的圆圈数字
        src_nums = PunctuationHelper.PATTERN_ALL_NUM.findall(src)
        dst_nums = PunctuationHelper.PATTERN_ALL_NUM.findall(dst)
        src_circled_nums = PunctuationHelper.PATTERN_CIRCLED_NUM.findall(src)
        dst_circled_nums = PunctuationHelper.PATTERN_CIRCLED_NUM.findall(dst)

        # 如果原文中没有圆圈数字，则跳过
        if len(src_circled_nums) == 0:
            return dst

        # 如果原文和译文中数字（含圆圈数字）的数量不一致，则跳过
        if len(src_nums) != len(dst_nums):
            return dst

        # 如果原文中的圆圈数字数量少于译文中的圆圈数字数量，则跳过
        if len(src_circled_nums) < len(dst_circled_nums):
            return dst

        # 遍历原文与译文中的数字（含圆圈数字），尝试恢复
        for i in range(len(src_nums)):
            src_num_srt = src_nums[i]
            dst_num_srt = dst_nums[i]
            dst_num_int = PunctuationHelper.safe_int(dst_num_srt)

            # 如果原文中该位置不是圆圈数字，则跳过
            if src_num_srt not in PunctuationHelper.CIRCLED_NUMBERS_ALL:
                continue

            # 如果译文中该位置数值不在有效范围，则跳过
            if dst_num_int < 0 or dst_num_int >= len(PunctuationHelper.CIRCLED_NUMBERS_ALL):
                continue

            # 如果原文、译文中该位置的圆圈数字不一致，则跳过
            if src_num_srt != PunctuationHelper.CIRCLED_NUMBERS_ALL[dst_num_int]:
                continue

            # 尝试恢复
            dst = PunctuationHelper.fix_circled_numbers_by_index(dst, i, src_num_srt)

        return dst

    # 通过索引修复圆圈数字
    def fix_circled_numbers_by_index(dst: str, target_i: int, target_str: str) -> str:
        # 用于标识目标位置
        i = [0]

        def repl(m: re.Match) -> str:
            if i[0] == target_i:
                i[0] = i[0] + 1
                return target_str
            else:
                i[0] = i[0] + 1
                return m.group(0)

        return PunctuationHelper.PATTERN_ALL_NUM.sub(repl, dst)