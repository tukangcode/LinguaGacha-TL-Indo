import threading

from base.BaseData import BaseData

class Platform(BaseData):

    def __init__(self, args: dict) -> None:
        super().__init__()

        # 默认值
        self.id: int = ""                                   # ID
        self.name: str = ""                                 # 显示名称
        self.key: list[str] = ""                            # 密钥
        self.model: str = ""                                # 模型
        self.api_url: str = ""                              # 接口地址
        self.api_type: str = ""                             # 接口类型
        self.top_p: float = 0.95                            # 生成参数
        self.temperature: float = 0.5                       # 生成参数
        self.presence_penalty: float = 0.0                  # 生成参数
        self.frequency_penalty: float = 0.0                 # 生成参数

        # 初始化
        for k, v in args.items():
            setattr(self, k, v)

        # 线程锁
        self.lock = threading.Lock()

    # 获取 ID
    def get_id(self) -> int:
        with self.lock:
            return self.id

    # 设置 ID
    def set_id(self, id: int) -> None:
        with self.lock:
            self.id = id

    # 获取显示名称
    def get_name(self) -> str:
        with self.lock:
            return self.name

    # 设置显示名称
    def set_name(self, name: str) -> None:
        with self.lock:
            self.name = name

    # 获取密钥
    def get_key(self) -> list[str]:
        with self.lock:
            return self.key

    # 设置密钥
    def set_key(self, key: list[str]) -> None:
        with self.lock:
            self.key = key

    # 获取模型
    def get_model(self) -> str:
        with self.lock:
            return self.model

    # 设置模型
    def set_model(self, model: str) -> None:
        with self.lock:
            self.model = model

    # 获取接口地址
    def get_api_url(self) -> str:
        with self.lock:
            return self.api_url

    # 设置接口地址
    def set_api_url(self, api_url: str) -> None:
        with self.lock:
            self.api_url = api_url

    # 获取接口类型
    def get_api_type(self) -> str:
        with self.lock:
            return self.api_type

    # 设置接口类型
    def set_api_type(self, api_type: str) -> None:
        with self.lock:
            self.api_type = api_type

    # 获取 top_p
    def get_top_p(self) -> float:
        with self.lock:
            return self.top_p

    # 设置 top_p
    def set_top_p(self, top_p: float) -> None:
        with self.lock:
            self.top_p = top_p

    # 获取 temperature
    def get_temperature(self) -> float:
        with self.lock:
            return self.temperature

    # 设置 temperature
    def set_temperature(self, temperature: float) -> None:
        with self.lock:
            self.temperature = temperature

    # 获取 presence_penalty
    def get_presence_penalty(self) -> float:
        with self.lock:
            return self.presence_penalty

    # 设置 presence_penalty
    def set_presence_penalty(self, presence_penalty: float) -> None:
        with self.lock:
            self.presence_penalty = presence_penalty

    # 获取 frequency_penalty
    def get_frequency_penalty(self) -> float:
        with self.lock:
            return self.frequency_penalty