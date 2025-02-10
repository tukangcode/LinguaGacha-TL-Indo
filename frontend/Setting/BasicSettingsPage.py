from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLayout
from PyQt5.QtWidgets import QVBoxLayout
from qfluentwidgets import FluentWindow

from base.Base import Base
from widget.SpinCard import SpinCard

class BasicSettingsPage(QWidget, Base):

    def __init__(self, text: str, window: FluentWindow) -> None:
        super().__init__(window)
        self.setObjectName(text.replace(" ", "-"))

        # 默认配置
        self.default = {
            "task_token_limit": 384,
            "batch_size": 0,
            "request_timeout": 120,
            "max_round": 16,
        }

        # 载入并保存默认配置
        config = self.save_config(self.load_config_from_default())

        # 设置容器
        self.vbox = QVBoxLayout(self)
        self.vbox.setSpacing(8)
        self.vbox.setContentsMargins(24, 24, 24, 24) # 左、上、右、下

        # 添加控件
        self.add_widget_batch_size(self.vbox, config, window)
        self.add_widget_task_token_limit(self.vbox, config, window)
        self.add_widget_request_timeout(self.vbox, config, window)
        self.add_widget_max_round(self.vbox, config, window)

        # 填充
        self.vbox.addStretch(1) # 确保控件顶端对齐

    # 并发任务数
    def add_widget_batch_size(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        def init(widget: SpinCard) -> None:
            widget.set_range(0, 9999999)
            widget.set_value(config.get("batch_size"))

        def value_changed(widget: SpinCard, value: int) -> None:
            config = self.load_config()
            config["batch_size"] = value
            self.save_config(config)

        parent.addWidget(
            SpinCard(
                "并发任务数",
                "同时执行的翻译任务的最大数量，合理设置可以极大的增加翻译速度，请参考接口平台的限制进行设置，本地接口无需设置",
                init = init,
                value_changed = value_changed,
            )
        )

    # 翻译任务长度阈值
    def add_widget_task_token_limit(self, parent: QLayout, config: dict, window: FluentWindow)-> None:
        def init(widget: SpinCard) -> None:
            widget.set_range(0, 9999999)
            widget.set_value(config.get("task_token_limit"))

        def value_changed(widget: SpinCard, value: int) -> None:
            config = self.load_config()
            config["task_token_limit"] = value
            self.save_config(config)

        parent.addWidget(
            SpinCard(
                "翻译任务长度阈值",
                "每个翻译任务一次性向模型发送的文本长度的最大值，单位为 Token",
                init = init,
                value_changed = value_changed,
            )
        )

    # 请求超时时间
    def add_widget_request_timeout(self, parent: QLayout, config: dict, window: FluentWindow)-> None:
        def init(widget: SpinCard) -> None:
            widget.set_range(0, 9999999)
            widget.set_value(config.get("request_timeout"))

        def value_changed(widget: SpinCard, value: int) -> None:
            config = self.load_config()
            config["request_timeout"] = value
            self.save_config(config)

        parent.addWidget(
            SpinCard(
                "请求超时时间",
                "翻译任务发起请求时等待模型回复的最长时间，超时仍未收到回复，则会判断为任务失败，单位为秒，不支持 Google 系列模型",
                init = init,
                value_changed = value_changed,
            )
        )

    # 翻译流程最大轮次
    def add_widget_max_round(self, parent: QLayout, config: dict, window: FluentWindow)-> None:
        def init(widget: SpinCard) -> None:
            widget.set_range(0, 9999999)
            widget.set_value(config.get("max_round"))

        def value_changed(widget: SpinCard, value: int) -> None:
            config = self.load_config()
            config["max_round"] = value
            self.save_config(config)

        parent.addWidget(
            SpinCard(
                "翻译流程最大轮次",
                "当完成一轮翻译后，如果还有未翻译的条目，将重新开始新的翻译流程，直到翻译完成或者达到最大轮次",
                init = init,
                value_changed = value_changed,
            )
        )