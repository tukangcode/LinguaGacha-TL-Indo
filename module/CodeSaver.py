import re

from base.Base import Base

class CodeSaver(Base):

    # 可能存在的空字符
    SPACE = r"\s*"

    # 用于英文的代码段规则
    CODE_PATTERN_EN = (
        SPACE + r"if\(.{0,5}[vs]\[\d+\].{0,10}\)" + SPACE,            # if(!s[982]) if(s[1623]) if(v[982] >= 1)
        SPACE + r"en\(.{0,5}[vs]\[\d+\].{0,10}\)" + SPACE,            # en(!s[982]) en(v[982] >= 1)
        SPACE + r"[/\\][a-z]{1,5}<[\d]{0,10}>" + SPACE,               # /C<1> \FS<12>
        SPACE + r"[/\\][a-z]{1,5}\[[\d]{0,10}\]" + SPACE,             # /C[1] \FS[12]
        SPACE + r"[/\\][a-z]{1,5}(?=<[^\d]{0,10}>)" + SPACE,          # /C<非数字> \FS<非数字> 中的前半部分
        SPACE + r"[/\\][a-z]{1,5}(?=\[[^\d]{0,10}\])" + SPACE,        # /C[非数字] \FS[非数字] 中的前半部分
    )

    # 用于非英文的代码段规则
    CODE_PATTERN_NON_EN = (
        SPACE + r"if\(.{0,5}[vs]\[\d+\].{0,10}\)" + SPACE,            # if(!s[982]) if(v[982] >= 1) if(v[982] >= 1)
        SPACE + r"en\(.{0,5}[vs]\[\d+\].{0,10}\)" + SPACE,            # en(!s[982]) en(v[982] >= 1)
        SPACE + r"[/\\][a-z]{1,5}<[a-z\d]{0,10}>" + SPACE,            # /C<y> /C<1> \FS<xy> \FS<12>
        SPACE + r"[/\\][a-z]{1,5}\[[a-z\d]{0,10}\]" + SPACE,          # /C[x] /C[1] \FS[xy] \FS[12]
        SPACE + r"[/\\][a-z]{1,5}(?=<[^a-z\d]{0,10}>)" + SPACE,       # /C<非数字非字母> \FS<非数字非字母> 中的前半部分
        SPACE + r"[/\\][a-z]{1,5}(?=\[[^a-z\d]{0,10}\])" + SPACE,     # /C[非数字非字母] \FS[非数字非字母] 中的前半部分
    )

    # 同时作用于英文于非英文的代码段规则
    CODE_PATTERN_COMMON = (
        SPACE + r"\\fr" + SPACE,                                      # 重置文本的改变
        SPACE + r"\\fb" + SPACE,                                      # 加粗
        SPACE + r"\\fi" + SPACE,                                      # 倾斜
        SPACE + r"\\\{" + SPACE,                                      # 放大字体 \{
        SPACE + r"\\\}" + SPACE,                                      # 缩小字体 \}
        SPACE + r"\\g" + SPACE,                                       # 显示货币 \G
        SPACE + r"\\\$" + SPACE,                                      # 打开金币框 \$
        SPACE + r"\\\." + SPACE,                                      # 等待0.25秒 \.
        SPACE + r"\\\|" + SPACE,                                      # 等待1秒 \|
        SPACE + r"\\!" + SPACE,                                       # 等待按钮按下 \!
        SPACE + r"\\>" + SPACE,                                       # 在同一行显示文字 \>
        # SPACE + r"\\<" + SPACE,                                     # 取消显示所有文字 \<
        SPACE + r"\\\^" + SPACE,                                      # 显示文本后不需要等待 \^
        # SPACE + r"\\n" + SPACE,                                     # 换行符 \\n
        SPACE + r"\\\\<br>" + SPACE,                                  # 换行符 \\<br>
        SPACE + r"<br>" + SPACE,                                      # 换行符 <br>
    )

    # 空白符
    CODE_PATTERN_SPACE = (
        r"[\r\n\t]+",                                                   # 空白符
    )

    def __init__(self, config: dict) -> None:
        super().__init__()

        # 初始化
        self.config = config
        self.placeholders = set()
        self.prefix_codes = {}
        self.suffix_codes = {}

        # 根据原文语言生成正则表达式
        if config.get("source_language") not in (Base.Language.ZH, Base.Language.JA, Base.Language.KO):
            base_pattern = CodeSaver.CODE_PATTERN_EN + CodeSaver.CODE_PATTERN_COMMON + CodeSaver.CODE_PATTERN_SPACE
            check_pattern = CodeSaver.CODE_PATTERN_EN + CodeSaver.CODE_PATTERN_COMMON
        else:
            base_pattern = CodeSaver.CODE_PATTERN_NON_EN + CodeSaver.CODE_PATTERN_COMMON + CodeSaver.CODE_PATTERN_SPACE
            check_pattern = CodeSaver.CODE_PATTERN_NON_EN + CodeSaver.CODE_PATTERN_COMMON
        self.base_pattern = re.compile(rf"(?:{"|".join(base_pattern)})+", re.IGNORECASE)
        self.check_pattern = re.compile(rf"(?:{"|".join(check_pattern)})+", re.IGNORECASE)
        self.prefix_pattern = re.compile(rf"^(?:{"|".join(base_pattern)})+", re.IGNORECASE)
        self.suffix_pattern = re.compile(rf"(?:{"|".join(base_pattern)})+$", re.IGNORECASE)

    # 预处理
    def preprocess(self, data: dict[str, str]) -> dict[str, str]:
        for k in data.keys():
            # 查找与替换前缀代码段
            self.prefix_codes[k] = self.prefix_pattern.findall(data.get(k))
            data[k] = self.prefix_pattern.sub("", data.get(k))

            # 查找与替换后缀代码段
            self.suffix_codes[k] = self.suffix_pattern.findall(data.get(k))
            data[k] = self.suffix_pattern.sub("", data.get(k))

            # 如果处理后的文本为空，则记录 ID，并将文本替换为占位符
            if data[k] == "":
                data[k] = "[占位符]"
                self.placeholders.add(k)

        return data

    # 后处理
    def postprocess(self, data: dict[str, str]) -> dict[str, str]:
        for k in data.keys():
            # 如果 ID 在占位符集合中，则将文本置为空
            if k in self.placeholders:
                data[k] = ""

            # 移除模型可能额外添加的头尾空白符
            data[k] = data.get(k).strip()

            # 还原前缀代码段
            data[k] = "".join(self.prefix_codes.get(k)) + data.get(k)

            # 还原后缀代码段
            data[k] = data.get(k) + "".join(self.suffix_codes.get(k))

        return data

    # 检查代码段
    def check(self, src: str, dst: str) -> None:
        return len(self.check_pattern.findall(src)) == len(self.check_pattern.findall(dst))