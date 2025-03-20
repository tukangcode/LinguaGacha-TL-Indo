import time
import threading
from typing import Callable

from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from qfluentwidgets import Action
from qfluentwidgets import TimeEdit
from qfluentwidgets import FluentIcon
from qfluentwidgets import FlowLayout
from qfluentwidgets import MessageBox
from qfluentwidgets import MessageBoxBase
from qfluentwidgets import FluentWindow
from qfluentwidgets import ProgressRing
from qfluentwidgets import CaptionLabel
from qfluentwidgets import StrongBodyLabel
from qfluentwidgets import IndeterminateProgressRing

from base.Base import Base
from module.Localizer.Localizer import Localizer
from widget.DashboardCard import DashboardCard
from widget.WaveformWidget import WaveformWidget
from widget.CommandBarCard import CommandBarCard

class TimerMessageBox(MessageBoxBase):

    def __init__(self, parent, title: str, message_box_close: Callable = None) -> None:
        super().__init__(parent=parent)

        # 初始化
        self.delay = 0
        self.message_box_close = message_box_close

        # 设置框体
        self.yesButton.setText(Localizer.get().confirm)
        self.cancelButton.setText(Localizer.get().cancel)

        # 设置主布局
        self.viewLayout.setContentsMargins(16, 16, 16, 16)  # 左、上、右、下

        # 标题
        self.title_label = StrongBodyLabel(title, self)
        self.viewLayout.addWidget(self.title_label)

        # 输入框
        self.time_edit = TimeEdit(self)
        self.time_edit.setMinimumWidth(256)
        self.time_edit.setTimeRange(QTime(0, 0), QTime(23, 59))
        self.time_edit.setTime(QTime(2, 0))
        self.viewLayout.addWidget(self.time_edit)

    # 重写验证方法
    def validate(self) -> bool:
        if callable(self.message_box_close):
            self.message_box_close(self, self.time_edit.time())

        return True

class TranslationPage(QWidget, Base):

    def __init__(self, text: str, window: FluentWindow) -> None:
        super().__init__(window)
        self.setObjectName(text.replace(" ", "-"))

        # 初始化
        self.data = {}
        self.status_text = {
            Base.Status.IDLE: Localizer.get().translation_page_status_idle,
            Base.Status.TESTING: Localizer.get().translation_page_status_testing,
            Base.Status.TRANSLATING: Localizer.get().translation_page_status_translating,
            Base.Status.STOPPING: Localizer.get().translation_page_status_stopping,
        }

        # 载入配置文件
        config = self.load_config()

        # 设置主容器
        self.container = QVBoxLayout(self)
        self.container.setSpacing(8)
        self.container.setContentsMargins(24, 24, 24, 24)  # 左、上、右、下

        # 添加控件
        self.add_widget_head(self.container, config, window)
        self.add_widget_body(self.container, config, window)
        self.add_widget_foot(self.container, config, window)

        # 注册事件
        self.subscribe(Base.Event.PLATFORM_TEST_DONE, lambda event, data: self.update_button_status(event, data))
        self.subscribe(Base.Event.PLATFORM_TEST_START, lambda event, data: self.update_button_status(event, data))
        self.subscribe(Base.Event.TRANSLATION_START, lambda event, data: self.update_button_status(event, data))
        self.subscribe(Base.Event.TRANSLATION_STOP, lambda event, data: self.update_button_status(event, data))
        self.subscribe(Base.Event.TRANSLATION_STOP_DONE, self.translation_stop_done)
        self.subscribe(Base.Event.TRANSLATION_UPDATE, self.translation_update)
        self.subscribe(Base.Event.CACHE_FILE_AUTO_SAVE, self.cache_file_auto_save)
        self.subscribe(Base.Event.PROJECT_STATUS_CHECK_DONE, lambda event, data: self.update_button_status(event, data))
        self.subscribe(Base.Event.APP_SHUT_DOWN, self.app_shut_down)

        # 定时器
        self.ui_update_timer = QTimer(self)
        self.ui_update_timer.timeout.connect(self.update_ui_tick)
        self.ui_update_timer.start(500)

    # 页面显示事件
    def showEvent(self, event) -> None:
        super().showEvent(event)

        # 重置 frontend 状态
        self.action_continue.setEnabled(False)

        # 触发事件
        self.emit(Base.Event.PROJECT_STATUS, {})

    # 应用关闭事件
    def app_shut_down(self, event: int, data: dict) -> None:
        self.app_shut_down_flag = True

    # 更新 frontend 定时器
    def update_ui_tick(self) -> None:
        self.update_time(self.data)
        self.update_line(self.data)
        self.update_token(self.data)
        self.update_task(self.data)
        self.update_status(self.data)

        # 接收到退出信号则停止
        if getattr(self, "app_shut_down_flag", False) == True:
            self.ui_update_timer.stop()

    # 更新按钮状态事件
    def update_button_status(self, event: int, data: dict) -> None:
        if Base.WORK_STATUS == Base.Status.IDLE:
            self.indeterminate_hide()
            self.action_start.setEnabled(True)
            self.action_stop.setEnabled(False)
            self.action_export.setEnabled(False)
        elif Base.WORK_STATUS == Base.Status.TESTING:
            self.action_start.setEnabled(False)
            self.action_stop.setEnabled(False)
            self.action_export.setEnabled(False)
        elif Base.WORK_STATUS == Base.Status.TRANSLATING:
            self.action_start.setEnabled(False)
            self.action_stop.setEnabled(True)
            self.action_export.setEnabled(True)
        elif Base.WORK_STATUS == Base.Status.STOPPING:
            self.action_start.setEnabled(False)
            self.action_stop.setEnabled(False)
            self.action_export.setEnabled(False)

        if Base.WORK_STATUS == Base.Status.IDLE and data.get("status") == Base.TranslationStatus.TRANSLATING:
            self.action_continue.setEnabled(True)
        else:
            self.action_continue.setEnabled(False)

    # 翻译更新事件
    def translation_update(self, event: int, data: dict) -> None:
        self.data = data

    # 翻译停止完成事件
    def translation_stop_done(self, event: int, data: dict) -> None:
        # 更新按钮状态
        self.update_button_status(event, data)

        # 更新继续翻译按钮状态
        self.emit(Base.Event.PROJECT_STATUS, {})

    # 更新时间
    def update_time(self, data: dict) -> None:
        if Base.WORK_STATUS not in (Base.Status.STOPPING, Base.Status.TRANSLATING):
            return None

        if self.data.get("start_time", 0) == 0:
            total_time = 0
        else:
            total_time = int(time.time() - self.data.get("start_time", 0))

        if total_time < 60:
            self.time.set_unit("S")
            self.time.set_value(f"{total_time}")
        elif total_time < 60 * 60:
            self.time.set_unit("M")
            self.time.set_value(f"{(total_time / 60):.2f}")
        else:
            self.time.set_unit("H")
            self.time.set_value(f"{(total_time / 60 / 60):.2f}")

        remaining_time = int(total_time / max(1, self.data.get("line", 0)) * (self.data.get("total_line", 0) - self.data.get("line", 0)))
        if remaining_time < 60:
            self.remaining_time.set_unit("S")
            self.remaining_time.set_value(f"{remaining_time}")
        elif remaining_time < 60 * 60:
            self.remaining_time.set_unit("M")
            self.remaining_time.set_value(f"{(remaining_time / 60):.2f}")
        else:
            self.remaining_time.set_unit("H")
            self.remaining_time.set_value(f"{(remaining_time / 60 / 60):.2f}")

    # 更新行数
    def update_line(self, data: dict) -> None:
        if Base.WORK_STATUS not in (Base.Status.STOPPING, Base.Status.TRANSLATING):
            return None

        line = self.data.get("line", 0)
        if line < 1000:
            self.line_card.set_unit("Line")
            self.line_card.set_value(f"{line}")
        elif line < 1000 * 1000:
            self.line_card.set_unit("KLine")
            self.line_card.set_value(f"{(line / 1000):.2f}")
        else:
            self.line_card.set_unit("MLine")
            self.line_card.set_value(f"{(line / 1000 / 1000):.2f}")

        remaining_line = self.data.get("total_line", 0) - self.data.get("line", 0)
        if remaining_line < 1000:
            self.remaining_line.set_unit("Line")
            self.remaining_line.set_value(f"{remaining_line}")
        elif remaining_line < 1000 * 1000:
            self.remaining_line.set_unit("KLine")
            self.remaining_line.set_value(f"{(remaining_line / 1000):.2f}")
        else:
            self.remaining_line.set_unit("MLine")
            self.remaining_line.set_value(f"{(remaining_line / 1000 / 1000):.2f}")

    # 更新实时任务数
    def update_task(self, data: dict) -> None:
        task = sum(1 for t in threading.enumerate() if "translator" in t.name)
        if task < 1000:
            self.task.set_unit("Task")
            self.task.set_value(f"{task}")
        else:
            self.task.set_unit("KTask")
            self.task.set_value(f"{(task / 1000):.2f}")

    # 更新 Token 数据
    def update_token(self, data: dict) -> None:
        if Base.WORK_STATUS not in (Base.Status.STOPPING, Base.Status.TRANSLATING):
            return None

        token = self.data.get("token", 0)
        if token < 1000:
            self.token.set_unit("Token")
            self.token.set_value(f"{token}")
        elif token < 1000 * 1000:
            self.token.set_unit("KToken")
            self.token.set_value(f"{(token / 1000):.2f}")
        else:
            self.token.set_unit("MToken")
            self.token.set_value(f"{(token / 1000 / 1000):.2f}")

        speed = self.data.get("total_completion_tokens", 0) / max(1, time.time() - self.data.get("start_time", 0))
        self.waveform.add_value(speed)
        if speed < 1000:
            self.speed.set_unit("T/S")
            self.speed.set_value(f"{speed:.2f}")
        else:
            self.speed.set_unit("KT/S")
            self.speed.set_value(f"{(speed / 1000):.2f}")

    # 更新进度环
    def update_status(self, data: dict) -> None:
        if Base.WORK_STATUS == Base.Status.STOPPING:
            percent = self.data.get("line", 0) / max(1, self.data.get("total_line", 0))
            self.ring.setValue(int(percent * 10000))
            self.ring.setFormat(f"{Localizer.get().translation_page_status_stopping}\n{percent * 100:.2f}%")
        elif Base.WORK_STATUS == Base.Status.TRANSLATING:
            percent = self.data.get("line", 0) / max(1, self.data.get("total_line", 0))
            self.ring.setValue(int(percent * 10000))
            self.ring.setFormat(f"{Localizer.get().translation_page_status_translating}\n{percent * 100:.2f}%")
        else:
            self.ring.setValue(0)
            self.ring.setFormat(Localizer.get().translation_page_status_idle)

    # 缓存文件自动保存事件
    def cache_file_auto_save(self, event: int, data: dict) -> None:
        if self.indeterminate.isHidden():
            self.indeterminate_show(Localizer.get().translation_page_indeterminate_saving)

            # 延迟关闭
            QTimer.singleShot(1500, lambda: self.indeterminate_hide())

    # 头部
    def add_widget_head(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.head_hbox_container = QWidget(self)
        self.head_hbox = QHBoxLayout(self.head_hbox_container)
        parent.addWidget(self.head_hbox_container)

        # 波形图
        self.waveform = WaveformWidget()
        self.waveform.set_matrix_size(100, 20)

        waveform_vbox_container = QWidget()
        waveform_vbox = QVBoxLayout(waveform_vbox_container)
        waveform_vbox.addStretch(1)
        waveform_vbox.addWidget(self.waveform)

        # 进度环
        self.ring = ProgressRing()
        self.ring.setRange(0, 10000)
        self.ring.setValue(0)
        self.ring.setTextVisible(True)
        self.ring.setStrokeWidth(12)
        self.ring.setFixedSize(140, 140)
        self.ring.setFormat(Localizer.get().translation_page_status_idle)

        ring_vbox_container = QWidget()
        ring_vbox = QVBoxLayout(ring_vbox_container)
        ring_vbox.addStretch(1)
        ring_vbox.addWidget(self.ring)

        # 添加控件
        self.head_hbox.addWidget(ring_vbox_container)
        self.head_hbox.addSpacing(8)
        self.head_hbox.addStretch(1)
        self.head_hbox.addWidget(waveform_vbox_container)
        self.head_hbox.addStretch(1)

    # 中部
    def add_widget_body(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.flow_container = QWidget(self)
        self.flow_layout = FlowLayout(self.flow_container, needAni=False)
        self.flow_layout.setSpacing(8)
        self.flow_layout.setContentsMargins(0, 0, 0, 0)

        self.add_time_card(self.flow_layout, config, window)
        self.add_remaining_time_card(self.flow_layout, config, window)
        self.add_line_card(self.flow_layout, config, window)
        self.add_remaining_line_card(self.flow_layout, config, window)
        self.add_speed_card(self.flow_layout, config, window)
        self.add_token_card(self.flow_layout, config, window)
        self.add_task_card(self.flow_layout, config, window)

        self.container.addWidget(self.flow_container, 1)

    # 底部
    def add_widget_foot(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.command_bar_card = CommandBarCard()
        parent.addWidget(self.command_bar_card)

        # 添加命令
        self.command_bar_card.set_minimum_width(640)
        self.add_command_bar_action_start(self.command_bar_card, config, window)
        self.add_command_bar_action_pause(self.command_bar_card, config, window)  # Add pause action
        self.add_command_bar_action_stop(self.command_bar_card, config, window)
        self.command_bar_card.add_separator()
        self.add_command_bar_action_continue(self.command_bar_card, config, window)
        self.command_bar_card.add_separator()
        self.add_command_bar_action_export(self.command_bar_card, config, window)
        self.command_bar_card.add_separator()
        self.add_command_bar_action_timer(self.command_bar_card, config, window)

        # 添加信息条
        self.indeterminate = IndeterminateProgressRing()
        self.indeterminate.setFixedSize(16, 16)
        self.indeterminate.setStrokeWidth(3)
        self.indeterminate.hide()
        self.info_label = CaptionLabel(Localizer.get().translation_page_indeterminate_saving, self)
        self.info_label.setTextColor(QColor(96, 96, 96), QColor(160, 160, 160))
        self.info_label.hide()

        self.command_bar_card.add_stretch(1)
        self.command_bar_card.add_widget(self.info_label)
        self.command_bar_card.add_spacing(4)
        self.command_bar_card.add_widget(self.indeterminate)

    # 累计时间
    def add_time_card(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.time = DashboardCard(
            title=Localizer.get().translation_page_card_time,
            value=Localizer.get().none,
            unit="",
        )
        self.time.setFixedSize(204, 204)
        parent.addWidget(self.time)

    # 剩余时间
    def add_remaining_time_card(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.remaining_time = DashboardCard(
            title=Localizer.get().translation_page_card_remaining_time,
            value=Localizer.get().none,
            unit="",
        )
        self.remaining_time.setFixedSize(204, 204)
        parent.addWidget(self.remaining_time)

    # 翻译行数
    def add_line_card(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.line_card = DashboardCard(
            title=Localizer.get().translation_page_card_line,
            value=Localizer.get().none,
            unit="",
        )
        self.line_card.setFixedSize(204, 204)
        parent.addWidget(self.line_card)

    # 剩余行数
    def add_remaining_line_card(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.remaining_line = DashboardCard(
            title=Localizer.get().translation_page_card_remaining_line,
            value=Localizer.get().none,
            unit="",
        )
        self.remaining_line.setFixedSize(204, 204)
        parent.addWidget(self.remaining_line)

    # 平均速度
    def add_speed_card(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.speed = DashboardCard(
            title=Localizer.get().translation_page_card_speed,
            value=Localizer.get().none,
            unit="",
        )
        self.speed.setFixedSize(204, 204)
        parent.addWidget(self.speed)

    # 累计消耗
    def add_token_card(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.token = DashboardCard(
            title=Localizer.get().translation_page_card_token,
            value=Localizer.get().none,
            unit="",
        )
        self.token.setFixedSize(204, 204)
        parent.addWidget(self.token)

    # 并行任务
    def add_task_card(self, parent: QLayout, config: dict, window: FluentWindow) -> None:
        self.task = DashboardCard(
            title=Localizer.get().translation_page_card_task,
            value=Localizer.get().none,
            unit="",
        )
        self.task.setFixedSize(204, 204)
        parent.addWidget(self.task)

    # 开始
    def add_command_bar_action_start(self, parent: CommandBarCard, config: dict, window: FluentWindow) -> None:
        def triggered() -> None:
            if self.action_continue.isEnabled():
                message_box = MessageBox(Localizer.get().alert, Localizer.get().alert_reset_translation, window)
                message_box.yesButton.setText(Localizer.get().confirm)
                message_box.cancelButton.setText(Localizer.get().cancel)

                # 点击取消，则不触发开始翻译事件
                if not message_box.exec():
                    return

            self.emit(Base.Event.TRANSLATION_START, {
                "status": Base.TranslationStatus.UNTRANSLATED,
            })

        self.action_start = parent.add_action(
            Action(FluentIcon.PLAY, Localizer.get().start, parent, triggered=triggered)
        )

    # 暂停
    def add_command_bar_action_pause(self, parent: CommandBarCard, config: dict, window: FluentWindow) -> None:
        """
        Adds a pause action to the command bar.
        Allows the user to set a pause duration and pause the translation operation in a loop until the task is finished.
        """
        pause_duration = None  # Stores the pause duration in seconds
        pause_start_time = None  # Stores the time when the pause started
        is_pause_loop_active = False  # Tracks whether the pause loop is active

        def format_time(seconds: int) -> str:
            """Formats time in seconds to HH:MM:SS."""
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            return f"{hours:02}:{minutes:02}:{seconds:02}"

        def pause_timer_interval() -> None:
            """
            Timer callback to check if the pause duration has elapsed.
            If the pause is over, resumes the translation operation.
            If the pause loop is active, it will pause again after the translation resumes.
            """
            nonlocal pause_duration, pause_start_time, is_pause_loop_active

            if pause_start_time is not None and pause_duration is not None:
                elapsed_time = time.time() - pause_start_time
                if elapsed_time >= pause_duration:
                    # Pause is over, resume translation
                    self.emit(Base.Event.TRANSLATION_START, {
                        "status": Base.TranslationStatus.TRANSLATING,
                    })
                    pause_start_time = None
                    self.action_pause.setText(Localizer.get().pause)  # Reset button text

                    # If the pause loop is active, pause again after resuming
                    if is_pause_loop_active and Base.WORK_STATUS == Base.Status.TRANSLATING:
                        self.emit(Base.Event.TRANSLATION_STOP, {})
                        pause_start_time = time.time()
                        self.action_pause.setText(format_time(pause_duration))  # Update button text

        def triggered() -> None:
            """
            Triggered when the pause button is clicked.
            Opens a dialog to set the pause duration and pauses the translation operation.
            If the pause loop is active, it will repeatedly pause and resume the translation.
            """
            nonlocal pause_duration, pause_start_time, is_pause_loop_active

            if pause_start_time is not None:
                # If already paused, do nothing
                return

            # Open a dialog to set the pause duration
            pause_dialog = TimerMessageBox(
                parent=window,
                title=Localizer.get().translation_page_pause_title,
                message_box_close=lambda widget, input_time: set_pause_duration(input_time),
            )
            if pause_dialog.exec():
                # Enable the pause loop
                is_pause_loop_active = True

                # Pause the translation operation
                self.emit(Base.Event.TRANSLATION_STOP, {})
                pause_start_time = time.time()
                self.action_pause.setText(format_time(pause_duration))  # Update button text

        def set_pause_duration(input_time: QTime) -> None:
            """
            Sets the pause duration based on user input.
            """
            nonlocal pause_duration
            pause_duration = input_time.hour() * 3600 + input_time.minute() * 60 + input_time.second()

        # Add the pause action to the command bar
        self.action_pause = parent.add_action(
            Action(FluentIcon.PAUSE, Localizer.get().pause, parent, triggered=triggered),
        )

        # Start a timer to check the pause duration
        pause_timer = QTimer(self)
        pause_timer.setInterval(1000)  # Check every second
        pause_timer.timeout.connect(pause_timer_interval)
        pause_timer.start()

    # 停止
    def add_command_bar_action_stop(self, parent: CommandBarCard, config: dict, window: FluentWindow) -> None:
        def triggered() -> None:
            message_box = MessageBox(Localizer.get().alert, Localizer.get().translation_page_alert_pause, window)
            message_box.yesButton.setText(Localizer.get().confirm)
            message_box.cancelButton.setText(Localizer.get().cancel)

            # 确认则触发停止翻译事件
            if message_box.exec():
                self.indeterminate_show(Localizer.get().translation_page_indeterminate_stoping)
                self.emit(Base.Event.TRANSLATION_STOP, {})

        self.action_stop = parent.add_action(
            Action(FluentIcon.CANCEL_MEDIUM, Localizer.get().stop, parent, triggered=triggered),
        )
        self.action_stop.setEnabled(False)

    # 继续翻译
    def add_command_bar_action_continue(self, parent: CommandBarCard, config: dict, window: FluentWindow) -> None:
        def triggered() -> None:
            self.emit(Base.Event.TRANSLATION_START, {
                "status": Base.TranslationStatus.TRANSLATING,
            })

        self.action_continue = parent.add_action(
            Action(FluentIcon.ROTATE, Localizer.get().translation_page_continue, parent, triggered=triggered),
        )
        self.action_continue.setEnabled(False)

    # 导出已完成的内容
    def add_command_bar_action_export(self, parent: CommandBarCard, config: dict, window: FluentWindow) -> None:
        def triggered() -> None:
            self.emit(Base.Event.TRANSLATION_MANUAL_EXPORT, {})
            self.emit(Base.Event.APP_TOAST_SHOW, {
                "type": Base.ToastType.SUCCESS,
                "message": Localizer.get().translation_page_export_toast,
            })

        self.action_export = parent.add_action(
            Action(FluentIcon.SHARE, Localizer.get().translation_page_export, parent, triggered=triggered),
        )
        self.action_export.setEnabled(False)

    # 定时器
    def add_command_bar_action_timer(self, parent: CommandBarCard, config: dict, window: FluentWindow) -> None:
        interval = 1
        delay_time = None

        def format_time(full: int) -> str:
            hours = int(full / 3600)
            minutes = int((full - hours * 3600) / 60)
            seconds = full - hours * 3600 - minutes * 60

            return f"{hours:02}:{minutes:02}:{seconds:02}"

        def timer_interval() -> None:
            nonlocal interval
            nonlocal delay_time

            if not isinstance(delay_time, int):
                return None

            if delay_time > 0:
                delay_time = delay_time - interval
                self.action_timer.setText(format_time(delay_time))
            else:
                self.emit(Base.Event.TRANSLATION_START, {
                    "status": Base.TranslationStatus.UNTRANSLATED,
                })

                delay_time = None
                self.action_timer.setText(Localizer.get().timer)

        def message_box_close(widget: TimerMessageBox, input_time: QTime) -> None:
            nonlocal delay_time

            delay_time = input_time.hour() * 3600 + input_time.minute() * 60 + input_time.second()

        def triggered() -> None:
            nonlocal delay_time

            if not isinstance(delay_time, int):
                TimerMessageBox(
                    parent=window,
                    title=Localizer.get().translation_page_timer,
                    message_box_close=message_box_close,
                ).exec()
            else:
                message_box = MessageBox(Localizer.get().alert, Localizer.get().alert_reset_timer, window)
                message_box.yesButton.setText(Localizer.get().confirm)
                message_box.cancelButton.setText(Localizer.get().cancel)

                # 点击取消，则不触发开始翻译事件
                if not message_box.exec():
                    return

                delay_time = None
                self.action_timer.setText(Localizer.get().timer)

        self.action_timer = parent.add_action(
            Action(FluentIcon.HISTORY, Localizer.get().timer, parent, triggered=triggered)
        )

        # 定时检查
        timer = QTimer(self)
        timer.setInterval(interval * 1000)
        timer.timeout.connect(timer_interval)
        timer.start()

    # 显示信息条
    def indeterminate_show(self, msg: str) -> None:
        self.indeterminate.show()
        self.info_label.show()
        self.info_label.setText(msg)

    # 隐藏信息条
    def indeterminate_hide(self) -> None:
        self.indeterminate.hide()
        self.info_label.hide()
        self.info_label.setText("")