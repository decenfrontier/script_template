# 标准库
import copy
from threading import Thread
import requests

# 第三方库
from PySide2.QtWidgets import (
    QMainWindow,
    QLabel,
    QComboBox,
    QMenu,
    QTableWidgetItem,
    QDialog,
    QTextBrowser,
    QHBoxLayout,
    QMessageBox,
    QSystemTrayIcon,
    QAction,
    QPushButton,
    QSlider,
    QFileDialog,
    QSpinBox,
)
from PySide2.QtGui import QCursor, QIcon, QTextCursor, QCloseEvent, QColor

from PySide2.QtCore import Signal, QTimer, Qt, QEvent

# 本地库
from ui.wnd_main import Ui_WndMain
import common
from threads import *
from utils import *
from const.const import *
import settings
from biz.task import *

requests.packages.urllib3.disable_warnings()

class WndMain(QMainWindow, Ui_WndMain):
    sig_cell = Signal(int, int, str)
    sig_info = Signal(str)
    sig_close = Signal()
    sig_arrange = Signal()
    sig_rights = Signal(str, bool)

    def __init__(self):
        super().__init__()
        # 安装界面
        self.setupUi(self)
        # 初始化自定义信号槽
        self.init_custom_sig_slot()
        # 初始化实例属性
        self.init_instance_field()
        # 初始化界面控件
        self.init_widgets()
        # 初始化菜单
        self.init_menus()
        # 初始化信号槽
        self.init_sig_slot()
        # 设置为首页
        self.stack_widget.setCurrentIndex(0)
        # 显示欢迎信息
        self.show_info("初始化完成, 欢迎使用!")
        # 开启热键线程
        Thread(target=self.thd_hotkey, daemon=True).start()
        # 开启心跳线程
        Thread(target=self.thd_heart_beat, daemon=True).start()
        # 安装事件过滤器
        for obj in self.findChildren(QSpinBox):
            obj.installEventFilter(self)
        for obj in self.findChildren(QComboBox):
            obj.installEventFilter(self)

    def closeEvent(self, event: QCloseEvent):
        self.timer_cur.stop()
        self.timer_ds.stop()
        self.timer_info.stop()
        self.diag.close()
        def thd_stop(wk: common.Worker):
            wk.record("被强制终止")
            wk.thread.end()
        thd_list = []
        for wk in settings.worker_list:
            if wk and not wk.is_end:
                t = Thread(target=thd_stop, args=(wk,), daemon=True)
                t.start()
                thd_list.append(t)
        for t in thd_list:
            t.join()
        time.sleep(0.5)
        if len(thd_list):
            self.show_info("等待所有线程结束...")
            time.sleep(1)
            self.show_info("所有线程已结束")
            
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel:
            if obj.inherits("QSpinBox") or obj.inherits("QComboBox"):
                return True
        return super().eventFilter(obj, event)

    # 最小化到托盘区
    def changeEvent(self, event: QEvent):
        if event.type() == QEvent.WindowStateChange and self.isMinimized():
            self.hide()
            event.ignore()

    # 读取配置（文件到控件）
    def common_cfg_read(self):
        dir_create(PATH_SOFTWARE_CONFIG)
        # 先读文件
        read_common_cfg = json_file_to_dict(PATH_SOFTWARE_COMMON)
        settings.cfg_common = copy.deepcopy(settings.default_cfg_common)
        for key, value in read_common_cfg.items():
            if key not in settings.cfg_common:
                continue
            if key == "游戏账号信息":
                for idx, account_info in enumerate(read_common_cfg[key]):
                    if idx >= TBE_CONSOLE_ROW:
                        break
                    settings.cfg_common[key][idx] = account_info
            else:  # 其它的都逐key更新就好
                settings.cfg_common[key] = value
        for cfg_account in settings.cfg_common["游戏账号信息"]:
            if not cfg_account:
                continue
            row = cfg_account["row"]
            self.tbe_console.item(row, COL_NAME).setText(
                cfg_account.get("player_name", "")
            )
            self.tbe_console.item(row, COL_ACCOUNT).setText(
                decrypt(cfg_account["account"])
            )
            self.tbe_console.item(row, COL_PASSWORD).setText(
                decrypt(cfg_account["password"])
            )
            self.tbe_console.cellWidget(row, COL_SERVER).setCurrentText(
                cfg_account["server"]
            )
        self.cmb_arrange_get_wnd.setCurrentIndex(
            settings.cfg_common["获取窗口后排列方式"]
        )
        self.cmb_set_plan_get_wnd.setCurrentIndex(
            settings.cfg_common["获取窗口后设置方案"]
        )
        self.cmb_set_plan_db_col.setCurrentIndex(
            settings.cfg_common["双击方案列设置方案"]
        )
        self.chk_arrange_get_wnd.setChecked(settings.cfg_common["获取窗口后是否排列"])
        self.chk_set_plan_get_wnd.setChecked(
            settings.cfg_common["获取窗口后是否设置"]
        )
        self.chk_on_time.setChecked(settings.cfg_common["定时"])
        self.chk_on_time_run_all.setChecked(settings.cfg_common["定时运行全部窗口"])
        self.chk_on_time_shut_down.setChecked(settings.cfg_common["定时关闭计算机"])
        self.tmedt_on_time_run_all.setTime(QTime.fromString(settings.cfg_common["定时运行全部窗口时间"], "HH:mm"))
        self.tmedt_on_time_shut_down.setTime(QTime.fromString(settings.cfg_common["定时关闭计算机时间"], "HH:mm"))
        self.edt_game_path.setText(settings.cfg_common["游戏路径"])
        self.edt_card_key.setText(decrypt(settings.cfg_common["卡密"]))

    # 保存配置（控件到文件）
    def common_cfg_save(self):
        self.show_info("开始保存通用配置...")
        # 基本配置
        settings.cfg_common["卡密"] = (
            encrypt(self.edt_card_key.text())
        )
        settings.cfg_common["获取窗口后排列方式"] = (
            self.cmb_arrange_get_wnd.currentIndex()
        )
        settings.cfg_common["获取窗口后设置方案"] = (
            self.cmb_set_plan_get_wnd.currentIndex()
        )
        settings.cfg_common["双击方案列设置方案"] = (
            self.cmb_set_plan_db_col.currentIndex()
        )
        settings.cfg_common["游戏路径"] = self.edt_game_path.text()
        settings.cfg_common["获取窗口后是否排列"] = self.chk_arrange_get_wnd.isChecked()
        settings.cfg_common["获取窗口后是否设置"] = self.chk_set_plan_get_wnd.isChecked()
        settings.cfg_common["定时"] = self.chk_on_time.isChecked()
        settings.cfg_common["定时运行全部窗口"] = self.chk_on_time_run_all.isChecked()
        settings.cfg_common["定时关闭计算机"] = self.chk_on_time_shut_down.isChecked()
        settings.cfg_common["定时运行全部窗口时间"] = self.tmedt_on_time_run_all.time().toString("HH:mm")
        settings.cfg_common["定时关闭计算机时间"] = self.tmedt_on_time_shut_down.time().toString("HH:mm")
        # 表格-账号角色名配置
        for row in range(TBE_CONSOLE_ROW):
            item_name = self.tbe_console.item(row, COL_NAME).text()
            item_account = self.tbe_console.item(row, COL_ACCOUNT).text()
            item_password = self.tbe_console.item(row, COL_PASSWORD).text()
            item_server = self.tbe_console.cellWidget(
                row, COL_SERVER).currentText()
            settings.cfg_common["游戏账号信息"][row] = {
                "row": row,
                "player_name": item_name,
                "account": encrypt(item_account),
                "password": encrypt(item_password),
                "server": item_server,
            }
        # 最后写入到文件
        dict_to_json_file(settings.cfg_common, PATH_SOFTWARE_COMMON)
        self.show_info("通用配置保存完成")

    def plan_cfg_read(self):  # 文件 -> 控件
        dir_create(PATH_SOFTWARE_CONFIG)
        self.cmb_set_plan_db_col.blockSignals(True)
        self.cmb_set_plan_get_wnd.blockSignals(True)
        # 先把空方案设置到各个cmb_plan中
        empty_plan_name = ""
        self.cmb_set_plan_db_col.addItem(empty_plan_name)  # 添加到 双击方案列下拉框 中
        self.cmb_set_plan_get_wnd.addItem(empty_plan_name)  # 添加到 获取窗口后设置方案下拉框 中
        for cmb_plan in settings.cmb_plan_list:
            ori_index = cmb_plan.currentIndex()
            cmb_plan.addItem(empty_plan_name)
            cmb_plan.setCurrentIndex(ori_index)
        # 读取所有方案
        settings.cfg_plan_dict = json_file_to_dict(PATH_SOFTWARE_PLAN)
        # 若一个方案都没有, 帮他添加一个
        if not settings.cfg_plan_dict:
            settings.cfg_plan_dict["1单人任务"] = {
                "执行列表": ["内功闭关", "经脉贯通", "四象跑环", "挂机刷野"],
            }
            settings.cfg_plan_dict["2队员挂机"] = {
                "执行列表": ["队员挂机"],
            }
            settings.cfg_plan_dict["3队长日常"] = {
                "执行列表": ["带队平乱", "带队威望", "带队刷野", "购买物品", "带队打虎", "带队打酒"],
            }
            
        # 每一个方案 都应该先设置为默认方案，再用读取到的配置来更新
        for plan_name, plan_setting_dict in settings.cfg_plan_dict.items():
            settings.cfg_plan_dict[plan_name] = copy.deepcopy(
                settings.default_cfg_plan
            )
            settings.cfg_plan_dict[plan_name].update(
                plan_setting_dict
            )
        # 添加到方案列表 和 下拉框中
        for plan_name, _ in settings.cfg_plan_dict.items():
            self.show_info(f"读取方案 {plan_name}...")
            self.lst_plan.addItem(plan_name)  # 添加到 方案列表 中
            self.cmb_set_plan_db_col.addItem(plan_name)  # 添加到 双击方案列下拉框 中
            self.cmb_set_plan_get_wnd.addItem(plan_name)  # 添加到 获取窗口后设置方案下拉框 中
            # 添加到方案下拉列表中
            for cmb_plan in settings.cmb_plan_list:
                if cmb_plan.findText(plan_name) == -1:
                    ori_index = cmb_plan.currentIndex()
                    cmb_plan.addItem(plan_name)  # 添加到方案下拉列表中
                    cmb_plan.setCurrentIndex(ori_index)
        self.cmb_set_plan_db_col.blockSignals(False)
        self.cmb_set_plan_get_wnd.blockSignals(False)

    def plan_cfg_save(self):  # 控件 -> 文件
        cur_item = self.lst_plan.currentItem()
        if not cur_item:
            self.show_info("请选择一个方案!")
            return
        plan_name = cur_item.text()
        # 保存基本配置
        settings.cfg_plan_dict[plan_name] = copy.deepcopy(
            settings.default_cfg_plan)
        settings.cfg_plan_dict[plan_name].update(
            self.get_basic_plan_setting_dict())
        # 保存各个业务任务的配置
        self.save_biz_task_setting_dict_from_control(plan_name)
        # 保存到文件
        dict_to_json_file(settings.cfg_plan_dict, PATH_SOFTWARE_PLAN)
        # 刷新所有cmb_plan的toolTip
        for row, cmb_plan in enumerate(settings.cmb_plan_list):
            if cmb_plan.currentText() == plan_name:
                wk = settings.worker_list[row]
                if wk is None:
                    continue
                self.update_worker_plan_info(wk, row, plan_name)
        self.show_info(f"方案配置-{plan_name} 保存成功")

    def init_custom_sig_slot(self):
        self.sig_cell.connect(
            lambda row, col, info: self.tbe_console.item(
                row, col).setText(info)
        )
        self.sig_info.connect(lambda info: self.show_info(info))
        self.sig_close.connect(lambda: self.close())
        self.sig_arrange.connect(lambda: self.after_get_wnd_arrange())
        self.sig_rights.connect(
            lambda rights, is_free: self.set_card_rights(rights, is_free))

    def init_instance_field(self):
        # 定时器
        self.timer_cur = QTimer()  # 每隔1秒获取当前时间格式串
        self.timer_info = QTimer()  # 每隔10秒刷新小贴士信息
        self.timer_ds = QTimer()  # 每隔60秒检查是否到启动或定时的时间
        # info标签
        self.lbe_1 = QLabel("<提示>: ")
        self.lbe_info = QLabel("窗口初始化完成")
        # 执行速率标签
        self.lbe_2 = QLabel("执行速率:")
        self.lbe_exec_rate = QLabel("1.00")
        # 滑动条
        self.exec_rate_slider = QSlider(Qt.Horizontal)
        self.exec_rate_slider.setMinimum(50)
        self.exec_rate_slider.setMaximum(200)
        self.exec_rate_slider.setSingleStep(10)
        self.exec_rate_slider.setValue(100)
        self.exec_rate_slider.setTickPosition(
            QSlider.TicksAbove
        )  # 设置刻度在滑块下方显示
        self.exec_rate_slider.setTickInterval(10)  # 设置刻度间隔
        self.exec_rate_slider.setFixedWidth(150)
        # 按钮
        self.btn_cfg_save = QPushButton("保存")
        # 日志窗口
        self.diag = QDialog(self)
        self.tbr_log = QTextBrowser(self.diag)
        self.form_lot = QHBoxLayout(self.diag)
        # 更新窗口
        self.wnd_update = WndUpdateSoftware(parent=self, 
                                            client_version=CLIENT_VERSION,
                                            patcher_save_path=PATCHER_SAVE_PATH)

    def init_widgets(self):
        # ------------------------- 窗口 -------------------------
        w, h = get_main_screen_wh()
        pos_x, pos_y = w - self.width(), h - self.height() - 80
        self.move(pos_x, pos_y)
        self.setWindowTitle(f"{APP_NAME}{CLIENT_VERSION}-单开免费版")
        # ------------------------- 日志窗口 -------------------------
        self.diag.resize(460, 480)
        self.form_lot.addWidget(self.tbr_log)
        self.form_lot.setMargin(4)
        # ------------------------- 树列表 -------------------------
        self.tre_all.expandAll()
        # ------------------------- 方案列表 -------------------------
        self.lst_plan.__class__ = CustomListWidget
        # ------------------------- 下拉框 -------------------------
        self.cmb_set_plan_db_col.__class__ = CustomComboBox
        self.cmb_set_plan_get_wnd.__class__ = CustomComboBox
        # ------------------------- 选项卡 -------------------------
        self.tab_set.setCurrentIndex(0)
        # ------------------------- 状态栏 -------------------------
        self.status_bar.addWidget(self.lbe_1)
        self.status_bar.addWidget(self.lbe_info)
        self.status_bar.addPermanentWidget(self.lbe_2)
        self.status_bar.addPermanentWidget(self.lbe_exec_rate)
        self.status_bar.addPermanentWidget(self.exec_rate_slider)
        self.status_bar.addPermanentWidget(self.btn_cfg_save)
        # ------------------------- 托盘区 -------------------------
        self.tray_icon = QSystemTrayIcon(QIcon(":/xxx.ico"), parent=self)
        self.tray_icon.show()
        # ------------------------- 表 格 -------------------------
        tbe_console = self.tbe_console
        self.account_delegate = AccountDelegate()
        self.password_delegate = PasswordDelegate()
        tbe_console.setItemDelegateForColumn(
            COL_ACCOUNT, self.account_delegate)
        tbe_console.setItemDelegateForColumn(
            COL_PASSWORD, self.password_delegate)
        
        h_header = tbe_console.horizontalHeader()
        v_header = tbe_console.verticalHeader()
        # 显示表头
        h_header.setVisible(True)
        v_header.setVisible(True)
        # 设置表格各列宽度
        h_header.resizeSection(COL_HWND, 80)
        h_header.resizeSection(COL_PLAN, 88)
        h_header.resizeSection(COL_RUN, 32)
        h_header.resizeSection(COL_PAUSE, 32)
        h_header.resizeSection(COL_END, 32)
        h_header.resizeSection(COL_LOG, 330)
        h_header.resizeSection(COL_NAME, 110)
        h_header.resizeSection(COL_ACCOUNT, 120)
        h_header.resizeSection(COL_PASSWORD, 120)
        h_header.resizeSection(COL_SERVER, 80)
        # 逐行添加项
        for row in range(TBE_CONSOLE_ROW):
            # 窗口句柄
            item = QTableWidgetItem()
            item.setFlags(
                Qt.ItemIsEnabled | Qt.ItemIsSelectable
            )  # 设置为不可编辑，可选择
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_HWND, item)
            # 方案选择
            item = QTableWidgetItem()
            item.setFlags(
                Qt.ItemIsEnabled | Qt.ItemIsSelectable
            )  # 设置为不可编辑，可选择
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_PLAN, item)
            cmb_plan = CustomComboBox(self.tbe_console)
            settings.cmb_plan_list[row] = cmb_plan
            tbe_console.setCellWidget(row, COL_PLAN, cmb_plan)
            cmb_plan.setEnabled(False)
            # 运行
            item = QTableWidgetItem()
            item.setFlags(
                Qt.ItemIsEnabled | Qt.ItemIsSelectable
            )  # 设置为不可编辑，可选择
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_RUN, item)
            # 暂停
            item = QTableWidgetItem()
            item.setFlags(
                Qt.ItemIsEnabled | Qt.ItemIsSelectable
            )  # 设置为不可编辑，可选择
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_PAUSE, item)
            # 终止
            item = QTableWidgetItem()
            item.setFlags(
                Qt.ItemIsEnabled | Qt.ItemIsSelectable
            )  # 设置为不可编辑，可选择
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_END, item)
            # 日志
            item = QTableWidgetItem()
            item.setFlags(
                Qt.ItemIsEnabled | Qt.ItemIsSelectable
            )  # 设置为不可编辑，可选择
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_LOG, item)
            # 角色名
            item = QTableWidgetItem(Qt.ItemIsSelectable)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_NAME, item)
            # 账号
            item = QTableWidgetItem(Qt.ItemIsSelectable)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_ACCOUNT, item)
            # 密码
            item = QTableWidgetItem(Qt.ItemIsSelectable)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_PASSWORD, item)
            # 服务器
            item = QTableWidgetItem(Qt.ItemIsSelectable)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            tbe_console.setItem(row, COL_SERVER, item)
            cmb_server = QComboBox()
            settings.cmb_server_list[row] = cmb_server
            tbe_console.setCellWidget(row, COL_SERVER, cmb_server)
            # 设置颜色
            if 0 <= row % 10 < 5:
                color = QColor(230, 255, 245)
            else:
                color = QColor(230, 245, 255)
            for col in range(TBE_CONSOLE_COL):
                tbe_console.item(row, col).setBackgroundColor(color)
        # ------------------------- 下拉框 -------------------------
        plan_list = settings.cfg_plan_dict.keys()
        for cmb_plan in settings.cmb_plan_list:
            cmb_plan.addItems(plan_list)
            cmb_plan.setCurrentIndex(-1)
        server_list = ["默认", "一线", "二线", "三线", "四线", "五线", "六线"]
        for cmb_server in settings.cmb_server_list:
            cmb_server.addItems(server_list)
            cmb_server.setCurrentIndex(0)

    def init_menus(self):
        # ------------------- tbe_console设置右键菜单 -------------------
        self.tbe_console.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_console = QMenu()
        self.action_five_game_control = QAction("一键控五")
        # -------
        self.action_get_all_wnd = QAction("获取所有窗口")
        self.action_arrange_all_wnd = QAction("排列所有窗口")  # 有二级菜单
        # -------
        self.action_login_sel_wnd = QAction("登录选中窗口")
        self.action_hide_show_sel_wnd = QAction("隐藏/显示选中窗口")
        self.action_clear_sel_wnd = QAction("清除选中窗口")
        self.action_force_exit_sel_wnd = QAction("强制退出选中窗口")
        self.menu_tbe_console.addAction(self.action_five_game_control)
        self.menu_tbe_console.addSeparator()
        self.menu_tbe_console.addAction(self.action_get_all_wnd)
        self.menu_tbe_console.addAction(self.action_arrange_all_wnd)
        self.menu_tbe_console.addSeparator()
        self.menu_tbe_console.addAction(self.action_login_sel_wnd)
        self.menu_tbe_console.addAction(self.action_hide_show_sel_wnd)
        self.menu_tbe_console.addAction(self.action_clear_sel_wnd)
        self.menu_tbe_console.addAction(self.action_force_exit_sel_wnd)
        # ----------------------- 添加二级菜单 -----------------------
        self.sub_menu_arrange_wnd = QMenu()
        self.sub_action_method0 = QAction("0垂直紧密")
        self.sub_action_method1 = QAction("1垂直扩展")
        self.sub_action_method2 = QAction("2平铺4K")
        self.sub_action_method3 = QAction("3对角紧密")
        self.sub_menu_arrange_wnd.addActions(
            [
                self.sub_action_method0,
                self.sub_action_method1,
                self.sub_action_method2,
                self.sub_action_method3,
            ]
        )
        # 添加子菜单
        self.action_arrange_all_wnd.setMenu(self.sub_menu_arrange_wnd)
        
        self.tbe_console.customContextMenuRequested.connect(
            self.on_custom_context_menu_requested
        )
        # 连接信号槽
        self.action_five_game_control.triggered.connect(
            self.on_action_five_game_control_triggered
        )
        self.action_get_all_wnd.triggered.connect(
            self.one_key_get_wnd
        )
        self.action_clear_sel_wnd.triggered.connect(
            self.on_action_clear_sel_wnd_triggered
        )
        self.action_hide_show_sel_wnd.triggered.connect(
            self.on_action_hide_show_sel_wnd_triggered
        )
        self.action_force_exit_sel_wnd.triggered.connect(
            self.on_action_force_exit_sel_wnd_triggered
        )
        self.action_login_sel_wnd.triggered.connect(
            self.on_action_login_sel_wnd_triggered
        )

        # 子菜单action信号槽
        self.sub_action_method0.triggered.connect(
            lambda: arrange_all_wnd(
                0, W_GAME, H_GAME, settings.SCREEN_W, settings.SCREEN_H)
        )
        self.sub_action_method1.triggered.connect(
            lambda: arrange_all_wnd(
                1, W_GAME, H_GAME, settings.SCREEN_W, settings.SCREEN_H)
        )
        self.sub_action_method2.triggered.connect(
            lambda: arrange_all_wnd(
                2, W_GAME, H_GAME, settings.SCREEN_W, settings.SCREEN_H)
        )
        self.sub_action_method3.triggered.connect(
            lambda: arrange_all_wnd(
                3, W_GAME, H_GAME, settings.SCREEN_W, settings.SCREEN_H)
        )

        # ------------------- lst_exec设置右键菜单 -------------------
        self.lst_exec.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_lst_exec = QMenu()
        self.action_lst_exec_clear = QAction("清空执行列表(&C)")
        self.action_copy_exec_list = QAction("复制执行列表")
        self.action_paste_exec_list = QAction("粘贴执行列表")
        self.action_paste_exec_list.setEnabled(False)
        # 添加菜单项
        self.menu_lst_exec.addAction(self.action_lst_exec_clear)
        self.menu_lst_exec.addAction(self.action_copy_exec_list)
        self.menu_lst_exec.addAction(self.action_paste_exec_list)
        # 连接信号槽
        self.lst_exec.customContextMenuRequested.connect(
            lambda: self.menu_lst_exec.exec_(QCursor.pos())
        )
        self.action_lst_exec_clear.triggered.connect(
            lambda: self.lst_exec.clear())
        self.action_copy_exec_list.triggered.connect(
            lambda: self.on_action_copy_exec_list_triggered())
        self.action_paste_exec_list.triggered.connect(
            lambda: self.on_action_paste_exec_list_triggered())

        # ------------------- tray_icon设置右键菜单 -------------------
        self.menu_tray_icon = QMenu()
        # 创建菜单项
        self.action_kill_all_wnd = QAction("强制退出所有游戏窗口(&K)")
        self.action_hide_show_all_wnd = QAction("隐藏/显示所有游戏窗口(&H)")
        self.action_quit = QAction("退出本软件(&Q)")
        # 添加菜单项
        self.menu_tray_icon.addAction(self.action_kill_all_wnd)
        self.menu_tray_icon.addSeparator()
        self.menu_tray_icon.addAction(self.action_hide_show_all_wnd)
        self.menu_tray_icon.addSeparator()
        self.menu_tray_icon.addAction(self.action_quit)
        # 为图标设置菜单
        self.tray_icon.setContextMenu(self.menu_tray_icon)
        # 连接信号槽
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        self.action_kill_all_wnd.triggered.connect(
            self.on_action_kill_all_wnd_triggered
        )
        self.action_hide_show_all_wnd.triggered.connect(
            self.on_action_hide_show_all_wnd_triggered
        )
        self.action_quit.triggered.connect(self.on_action_quit_triggered)

        # ------------------- lst_plan设置右键菜单 -------------------
        self.lst_plan.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_lst_plan = QMenu()
        self.action_lst_plan_del = QAction("删除此方案(&D)")
        self.action_lst_plan_cancel = QAction("取消选中")
        # 添加菜单项
        self.menu_lst_plan.addAction(self.action_lst_plan_del)
        self.menu_lst_plan.addAction(self.action_lst_plan_cancel)
        self.lst_plan.customContextMenuRequested.connect(
            lambda: self.menu_lst_plan.exec_(QCursor.pos())
        )
        self.action_lst_plan_del.triggered.connect(
            self.on_action_lst_plan_del_triggered
        )
        self.action_lst_plan_cancel.triggered.connect(
            lambda: self.lst_plan.setCurrentItem(None)
        )

    def init_sig_slot(self):
        # ------------------- 时钟 -------------------
        self.timer_cur.timeout.connect(self.on_timer_cur_timeout)
        self.timer_cur.start(1000)
        self.timer_info.timeout.connect(self.on_timer_info_timeout)
        self.timer_info.start(1000 * 10)
        self.timer_ds.timeout.connect(self.on_timer_ds_timeout)
        self.timer_ds.start(1000 * 60)
        # ------------------- 工具栏 -------------------
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.tool_bar.orientationChanged.connect(
            self.on_tool_bar_orientationChanged)
        # ------------------- 卡密相关 -------------------
        self.edt_card_key.editingFinished.connect(self.on_edt_card_key_editingFinished)
        self.btn_card_unbind.clicked.connect(self.on_btn_card_unbind_clicked)
        self.btn_card_buy.clicked.connect(self.on_btn_card_buy_clicked)
        # ------------------- 检查更新 -------------------
        self.btn_check_update.clicked.connect(self.on_btn_check_update_clicked)
        # ------------------- 中控台表格 -------------------
        h_header = self.tbe_console.horizontalHeader()
        v_header = self.tbe_console.verticalHeader()
        h_header.sectionDoubleClicked.connect(self.on_h_header_double_clicked)
        v_header.sectionDoubleClicked.connect(self.on_v_header_double_clicked)
        self.tbe_console.cellClicked.connect(self.on_tbe_console_cellClicked)
        self.tbe_console.cellDoubleClicked.connect(
            self.on_tbe_console_cellDoubleClicked
        )
        self.tbe_console.itemChanged.connect(self.on_tbe_console_itemChanged)
        # cmb_plan添加currentTextChanged信号槽
        for idx in range(len(settings.cmb_plan_list)):
            cmb_plan = settings.cmb_plan_list[idx]
            cmb_plan.currentTextChanged.connect(
                self.on_cmb_plan_cur_text_changed)
        # ------------------- 选项卡-设置 -------------------
        self.tab_set.currentChanged.connect(self.on_tab_set_currentChanged)
        # ------------------- 方案设置 -------------------
        # tre_all双击添加
        self.tre_all.itemDoubleClicked.connect(
            self.on_tre_all_item_double_clicked)
        # lst_exec双击删除
        self.lst_exec.itemDoubleClicked.connect(
            self.on_lst_exec_item_double_clicked)
        # lst_plan单击读取配置
        self.lst_plan.itemClicked.connect(
            self.on_lst_plan_item_clicked)
        # lst_plan当前项改变时设置编辑框内容
        self.lst_plan.currentTextChanged.connect(
            self.on_lst_plan_currentTextChanged)
        # btn_plan_create点击新建配置文件
        self.btn_plan_create.clicked.connect(self.on_btn_plan_create_clicked)
        # btn_plan_rename点击重命名配置文件
        self.btn_plan_rename.clicked.connect(self.on_btn_plan_rename_clicked)
        # chk_shuaye_terse_bb弹窗
        self.chk_shuaye_terse_bb.stateChanged.connect(
            self.on_chk_shuaye_terse_bb_stateChanged
        )
        # ------------------- 通用设置 -------------------
        self.cmb_set_plan_db_col.currentIndexChanged.connect(
            self.on_cmb_set_plan_db_col_cur_index_changed
        )
        self.cmb_arrange_get_wnd.currentIndexChanged.connect(
            self.on_cmb_arrange_get_wnd_cur_index_changed
        )
        self.cmb_set_plan_get_wnd.currentIndexChanged.connect(
            self.on_cmb_set_plan_get_wnd_cur_index_changed
        )
        self.btn_cfg_save.clicked.connect(self.on_btn_cfg_save_clicked)
        self.btn_start_auto_login.clicked.connect(
            self.on_btn_start_auto_login_clicked)
        self.btn_stop_auto_login.clicked.connect(
            self.on_btn_stop_auto_login_clicked)
        self.btn_open_folder_game_path.clicked.connect(
            self.on_btn_open_folder_game_path_clicked
        )
        self.btn_open_game.clicked.connect(
            self.on_btn_open_game_clicked
        )
        self.exec_rate_slider.valueChanged.connect(
            self.on_exec_rate_slider_value_changed
        )

    def show_info(self, info: str):
        self.lbe_info.setText(info)
        log.info(info)

    def show_tip(self, tip: str):
        self.lbe_info.setText(tip)

    def get_basic_plan_setting_dict(self):
        return {
            # 人物战斗
            "人物战斗救人": self.groupBox_people_save_people.isChecked(),
            "人物战斗救人比例": self.spin_count_people_save_people.value(),
            "人物战斗救BB": self.groupBox_people_save_bb.isChecked(),
            "人物战斗救BB比例": self.spin_count_people_save_bb.value(),
            "人物使用技能": self.groupBox_people_use_skill.isChecked(),
            "人物技能使用频率": self.spin_count_skill_frequency.value(),
            "人物护心百分比": self.spin_count_huxin_percent.value(),
            "人物未命中继续刺": self.chk_people_skill_continue_cixue.isChecked(),
            "人物刺怪比例": self.spin_count_people_skill_continue_cixue.value(),
            "人物刺穴F7": self.chk_people_skill_cixue.isChecked(),
            "人物护心F6": self.chk_people_skill_huxin.isChecked(),
            "人物五行克制F1": self.chk_people_skill_single.isChecked(),
            "人物战斗": get_checked_radio_text_in_groupbox(self.groupBox_people),
            "人物战后补充": self.chk_after_fight_people_supply.isChecked(),
            "人物战后补充比例": self.spin_count_after_fight_people_supply.value(),
            "人物切回首发BB": self.chk_people_switch_primary_bb.isChecked(),
            "唤出BB": self.groupBox_call_bb.isChecked(),
            "唤出BB血内比例": self.spin_count_call_bb_blood.value(),
            "唤出BB回合数": self.spin_count_call_bb_round.value(),
            "唤出BB名字": self.edt_call_bb_name.text(),
            # BB战斗
            "进攻类BB战斗救人": self.groupBox_fight_bb_save_people.isChecked(),
            "进攻类BB战斗救人比例": self.spin_count_fight_bb_save_people.value(),
            "进攻类BB战斗救BB": self.groupBox_fight_bb_save_bb.isChecked(),
            "进攻类BB战斗救BB比例": self.spin_count_fight_bb_save_bb.value(),
            "防守类BB战斗救人": self.groupBox_defend_bb_save_people.isChecked(),
            "防守类BB战斗救人比例": self.spin_count_defend_bb_save_people.value(),
            "防守类BB战斗救BB": self.groupBox_defend_bb_save_bb.isChecked(),
            "防守类BB战斗救BB比例": self.spin_count_defend_bb_save_bb.value(),
            "BB使用技能": self.groupBox_bb_use_skill.isChecked(),
            "BB厚积": self.chk_fight_bb_hj.isChecked(),
            "BB激将": self.chk_fight_bb_jj.isChecked(),
            "BB破釜": self.chk_fight_bb_pf.isChecked(),
            "BB乱神隔世": self.chk_fight_bb_lsgs.isChecked(),
            "BB金钟罩": self.chk_fight_bb_jzz.isChecked(),
            "BB铁布衫": self.chk_fight_bb_tbs.isChecked(),
            "BB破釜回合数": self.spin_count_fight_bb_pf_round.value(),
            # 战斗通用配置
            "拉药怪数目开关": self.chk_fight_save_enemy_less.isChecked(),
            "拉药怪数目": self.spin_count_fight_save_enemy_less.value(),
            # 其它
            "执行列表": [
                self.lst_exec.item(idx).text() for idx in range(self.lst_exec.count())
            ],
            "出城": get_checked_radio_text_in_groupbox(self.groupBox_go),
            "回城": get_checked_radio_text_in_groupbox(self.groupBox_back),
            "BB攻防": get_checked_radio_text_in_groupbox(self.groupBox_bb_fight_defend),
            "人宠使用技能": self.cmb_people_bb_use_skill.currentText(),
        }

    def read_basic_plan_setting_dict_to_control(self, update_plan_setting_dict: dict):
        if update_plan_setting_dict is None:
            return
        plan_setting_dict = copy.deepcopy(settings.default_cfg_plan)
        plan_setting_dict.update(update_plan_setting_dict)
        # 人物战斗
        self.groupBox_people_save_people.setChecked(
            plan_setting_dict["人物战斗救人"])
        self.spin_count_people_save_people.setValue(
            plan_setting_dict["人物战斗救人比例"]
        )
        self.groupBox_people_save_bb.setChecked(plan_setting_dict["人物战斗救BB"])
        self.spin_count_people_save_bb.setValue(plan_setting_dict["人物战斗救BB比例"])
        self.groupBox_people_use_skill.setChecked(plan_setting_dict["人物使用技能"])
        self.spin_count_skill_frequency.setValue(plan_setting_dict["人物技能使用频率"])
        self.spin_count_huxin_percent.setValue(plan_setting_dict["人物护心百分比"])
        self.chk_people_skill_continue_cixue.setChecked(plan_setting_dict["人物未命中继续刺"])
        self.spin_count_people_skill_continue_cixue.setValue(plan_setting_dict["人物刺怪比例"])
        self.chk_people_skill_cixue.setChecked(plan_setting_dict["人物刺穴F7"])
        self.chk_people_skill_huxin.setChecked(plan_setting_dict["人物护心F6"])
        self.chk_people_skill_single.setChecked(plan_setting_dict["人物五行克制F1"])
        set_checked_radio_text_in_groupbox(
            self.groupBox_people, plan_setting_dict["人物战斗"]
        )
        self.chk_after_fight_people_supply.setChecked(
            plan_setting_dict["人物战后补充"]
        )
        self.spin_count_after_fight_people_supply.setValue(
            plan_setting_dict["人物战后补充比例"]
        )
        self.chk_people_switch_primary_bb.setChecked(
            plan_setting_dict["人物切回首发BB"])
        self.groupBox_call_bb.setChecked(plan_setting_dict["唤出BB"])
        self.spin_count_call_bb_blood.setValue(plan_setting_dict["唤出BB血内比例"])
        self.spin_count_call_bb_round.setValue(plan_setting_dict["唤出BB回合数"])
        self.edt_call_bb_name.setText(plan_setting_dict["唤出BB名字"])
        # BB战斗
        self.groupBox_fight_bb_save_people.setChecked(
            plan_setting_dict["进攻类BB战斗救人"])
        self.spin_count_fight_bb_save_people.setValue(
            plan_setting_dict["进攻类BB战斗救人比例"])
        self.groupBox_fight_bb_save_bb.setChecked(
            plan_setting_dict["进攻类BB战斗救BB"])
        self.spin_count_fight_bb_save_bb.setValue(
            plan_setting_dict["进攻类BB战斗救BB比例"])
        self.groupBox_defend_bb_save_people.setChecked(
            plan_setting_dict["防守类BB战斗救人"])
        self.spin_count_defend_bb_save_people.setValue(
            plan_setting_dict["防守类BB战斗救人比例"])
        self.groupBox_defend_bb_save_bb.setChecked(
            plan_setting_dict["防守类BB战斗救BB"])
        self.spin_count_defend_bb_save_bb.setValue(
            plan_setting_dict["防守类BB战斗救BB比例"])
        self.groupBox_bb_use_skill.setChecked(plan_setting_dict["BB使用技能"])
        self.chk_fight_bb_lsgs.setChecked(
            plan_setting_dict.get("BB乱神隔世", False)
        )
        self.chk_fight_bb_hj.setChecked(plan_setting_dict["BB厚积"])
        self.chk_fight_bb_jj.setChecked(plan_setting_dict["BB激将"])
        self.chk_fight_bb_pf.setChecked(plan_setting_dict["BB破釜"])
        self.spin_count_fight_bb_pf_round.setValue(
            plan_setting_dict["BB破釜回合数"]
        )
        # 战斗通用配置
        self.chk_fight_save_enemy_less.setChecked(plan_setting_dict["拉药怪数目开关"])
        self.spin_count_fight_save_enemy_less.setValue(plan_setting_dict["拉药怪数目"])
        # 其它
        self.lst_exec.clear()
        self.lst_exec.addItems(plan_setting_dict["执行列表"])
        set_checked_radio_text_in_groupbox(
            self.groupBox_go, plan_setting_dict["出城"])
        set_checked_radio_text_in_groupbox(
            self.groupBox_back, plan_setting_dict["回城"]
        )
        set_checked_radio_text_in_groupbox(
            self.groupBox_bb_fight_defend, plan_setting_dict["BB攻防"])
        self.cmb_people_bb_use_skill.setCurrentText(
            plan_setting_dict["人宠使用技能"])

    def read_biz_task_setting_dict_to_control(self, plan_name: str):
        # 配置文件 到 当前控件
        for _, task_cls in settings.task_dict.items():
            task_cls.cfg_read(plan_name)

    def save_biz_task_setting_dict_from_control(self, plan_name: str):
        # 当前控件 到 全局变量(用来存储到配置文件)
        for _, task_cls in settings.task_dict.items():
            task_cls.cfg_save(plan_name)

    def thd_hotkey(self):
        print("鼠标监听开始...")
        from pynput import mouse

        def on_click(x, y, button, pressed):
            if not pressed:
                return
            if button != mouse.Button.middle:
                return
            hwnd = settings.com_obj.get_mouse_point_window()
            print(f"点击了中键, 坐标: {x}, {y}, 窗口句柄: {hwnd}")
            for wk in settings.worker_list:
                if wk is None:
                    continue
                if wk.hwnd != hwnd:
                    continue
                if wk.is_run:  # 如果在运行，就终止
                    wk.record(f"点击了中键, 窗口终止")
                    self.tbe_console.item(wk.row, COL_END).setText(SELECTED)
                else:  # 其它情况下直接运行
                    wk.record(f"点击了中键, 窗口运行")
                    self.tbe_console.item(wk.row, COL_RUN).setText(SELECTED)
                return

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        print("鼠标监听结束")

    def thd_heart_beat(self):
        self.heart_fail_count = 0
        self.last_heart_stamp = settings.cur_time_stamp
        while True:
            time.sleep(60*10)  # 每10分钟心跳一次
            self.last_heart_stamp = settings.cur_time_stamp
            self.send_request_heart()

    def one_key_get_wnd(self):
        hwnd_list = find_windows_by_name(WND_TITLE)
        if hwnd_list == []:
            self.show_info("未发现游戏窗口,请打开游戏后再试")
            return
        log.info(f"获取到的窗口句柄:{hwnd_list}")
        # 获取 用户设定的方案索引
        plan_idx = settings.cfg_common["获取窗口后设置方案"]
        # 这个用来保存每个窗口对应的行号，要一一匹配, 如果是之前设置过的窗口, 则row设为None，后面就不再创建wk
        row_list = []
        for hwnd in hwnd_list:
            row = self.add_hwnd(hwnd)
            if row == -1:
                row_list.append(None)
            else:
                row_list.append(row)
        # 下面的操作创建一个线程来做
        self.thd_get_wnd_list = []
        for hwnd, row in zip(hwnd_list, row_list):
            if row is None:
                continue
            t = Thread(target=self.thd_create_wk_for_hwnd, args=(hwnd, row, plan_idx), daemon=True)
            t.start()
            self.thd_get_wnd_list.append(t)
        if self.chk_arrange_get_wnd.isChecked():
            self.sig_arrange.emit()

    def add_hwnd(self, hwnd) -> int:
        # 若窗口已经存在, 则跳过下面步骤
        if hwnd in settings.hwnd_list:
            return -1
        # 找一个空位填充
        row = settings.hwnd_list.index(None)
        self.tbe_console.item(row, COL_HWND).setText(str(hwnd))
        settings.hwnd_list[row] = hwnd
        return row
    
    def locate_hwnd(self, hwnd: int, row: int):
        # 若窗口已经存在, 则跳过下面步骤
        if hwnd in settings.hwnd_list:
            return -1
        # 把窗口放到指定行
        self.tbe_console.item(row, COL_HWND).setText(str(hwnd))
        settings.hwnd_list[row] = hwnd
        return row
    
    def thd_create_wk_for_hwnd(self, hwnd, row, plan_idx=0):
        pythoncom.CoInitialize()
        # 创建com对象
        wnd_com_obj = create_com_obj()
        # 创建worker对象
        wk = common.Worker(hwnd, wnd_com_obj, row, TaskBase.get_team(row))
        # 把wk添加到列表中
        settings.worker_list[row] = wk
        # 清空之前的日志内容
        row_num = row + 1
        file_clear_content(f"{PATH_SOFTWARE_LOG}\\wnd_{row_num}.txt")
        # 激活cmb_plan,  并设置方案
        cmb_plan = settings.cmb_plan_list[row]
        cmb_plan.setEnabled(True)
        cmb_plan.setCurrentIndex(plan_idx)
        # 获取窗口位置
        x, y = get_wnd_pos(hwnd)
        if x != HIDE_X:
            wk.x, wk.y = x, y
        wk.record(f"窗口{row_num}获取成功, 并自动设置为{plan_idx}号方案")

    def after_get_wnd_arrange(self):
        log.info("开始等待所有线程")
        if getattr(self, "thd_get_wnd_list", None):
            for thd in self.thd_get_wnd_list:
                thd.join()
            self.thd_get_wnd_list = []
        log.info("结束等待所有线程")
        log.info("开始排列窗口")
        mode = settings.cfg_common["获取窗口后排列方式"]
        print(f"排列方式：{mode}")
        arrange_all_wnd(mode, W_GAME, H_GAME,
                        settings.SCREEN_W, settings.SCREEN_H)
        self.show_info(f"获取所有游戏窗口成功, 并按方式{mode}排列")

    def set_card_rights(self, rights="One", is_free=True):
        resp_card_rights = {
            "One": 1,
            "Five": 5,
            "Ten": 10,
            "Twenty": 20,
            "Thirty": 30,
            "Sixty": 60,
        }.get(rights, 1)
        if resp_card_rights < settings.card_rights:
            settings.user_info['extra_info'] = "CHEAT"
            is_free = True
            resp_card_rights = 1
        settings.card_rights = resp_card_rights
        settings.is_free = is_free
        soft_type = "免费" if is_free else "VIP"
        multi = "单" if settings.card_rights == 1 else str(settings.card_rights)
        self.setWindowTitle(f"{APP_NAME}{CLIENT_VERSION}-{multi}开{soft_type}版")

    def check_game_path(self):
        game_path = self.edt_game_path.text()
        print('game_path:', game_path)
        if (
            game_path == ""
            or not game_path.endswith("update.exe")
            or not os.path.exists(game_path)
        ):
            self.show_info("请先设置游戏路径!")
            return ""
        return game_path

    def on_btn_start_auto_login_clicked(self):
        game_path = self.check_game_path()
        if not game_path:
            return
        self.btn_start_auto_login.setEnabled(False)
        self.game_login_thread = ThreadLogin(game_path)
        self.game_login_thread.start()
        self.btn_stop_auto_login.setEnabled(True)

    def on_btn_stop_auto_login_clicked(self):
        locker = QMutexLocker(settings.global_wk.mutex)
        self.btn_stop_auto_login.setEnabled(False)
        self.game_login_thread.terminate()
        self.game_login_thread.wait()
        settings.global_wk.hwnd = 0
        settings.global_wk.unbind_window()
        self.btn_start_auto_login.setEnabled(True)

    def one_key_set_plan(self, idx):
        for wk in settings.worker_list:
            if wk is None:
                continue
            self.set_plan(wk.row, idx)

    def set_plan(self, row, plan_idx):
        cmb_plan = settings.cmb_plan_list[row]
        if not cmb_plan.isEnabled() or cmb_plan.count() < plan_idx:
            return
        cmb_plan.setCurrentIndex(plan_idx)

    def rmv_wnd_from_console(self, wk: common.Worker):
        row = wk.row
        # 先把工人停止
        if wk and not wk.is_end:
            wk.thread.end()
        # 移除此工人
        settings.worker_list[row] = None
        settings.hwnd_list[row] = None
        wk = None
        # 清空此行内容
        for col in range(COL_LOG + 1):
            item = self.tbe_console.item(row, col)
            if item:
                item.setText("")
        # 禁用cmb_plan
        cmb_plan = settings.cmb_plan_list[row]
        cmb_plan.setEnabled(False)
        cmb_plan.setCurrentIndex(-1)

    def update_cmb_plan_tooltip(self, row):
        wk = settings.worker_list[row]
        cmb_plan = settings.cmb_plan_list[row]
        tooltip = "-".join(wk.cfg_plan["执行列表"])
        cmb_plan.setToolTip(tooltip)

    # ---------------------- 自定义槽函数 -----------------------
    def on_custom_context_menu_requested(self):
        self.selected_rows = list(
            {index.row() for index in self.tbe_console.selectedIndexes()}
        )
        sel_row = self.selected_rows[0]
        self.start_row = (
            15
            if sel_row / 15 >= 1
            else 10 if sel_row / 10 >= 1 else 5 if sel_row / 5 >= 1 else 0
        )
        self.start_col = self.tbe_console.currentColumn()
        self.menu_tbe_console.exec_(QCursor.pos())

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isHidden():
                self.showNormal()
                self.activateWindow()
            else:
                self.hide()

    def on_action_kill_all_wnd_triggered(self):
        ret = QMessageBox.warning(
            self,
            "警告",
            "是否要强制结束所有游戏窗口?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if ret != QMessageBox.Yes:
            return
        for wk in settings.worker_list:
            if wk is None:
                continue
            self.rmv_wnd_from_console(wk)
            terminate_wnd(wk.hwnd)

    def on_action_hide_show_all_wnd_triggered(self):
        # 先找出第一个不为None的窗口，决定所有的窗口是显示还是隐藏
        action_show = False
        for wk in settings.worker_list:
            if wk:
                x, _ = get_wnd_pos(wk.hwnd)
                action_show = True if x == HIDE_X else False
                break
        for wk in settings.worker_list:
            if wk is None:
                continue
            Thread(target=self.thd_hide_show, args=(
                wk, action_show), daemon=True).start()

    def thd_hide_show(self, wk: common.Worker, show: bool):
        x, y = get_wnd_pos(wk.hwnd)
        if show:
            wk.show_wnd()
        else:
            wk.hide_wnd(x, y)

    def on_action_quit_triggered(self):
        ret = QMessageBox.warning(
            self, "警告", "是否要退出本软件?", QMessageBox.Yes | QMessageBox.No
        )
        if ret != QMessageBox.Yes:
            return
        self.sig_close.emit()

    def on_timer_cur_timeout(self):
        settings.cur_time_fmt = datetime.now().strftime("%H:%M:%S")
        settings.cur_time_stamp += 1

    def on_timer_info_timeout(self):
        tip_list = [
            "如果你需要自动上号和掉线重连，才需要配置账号密码",
            "游戏窗口不要最小化，会导致读取图像失败，如有需要可右键菜单隐藏",
            "表格菜单中的一键控五在不同列有不同效果哦，快去试试吧~",
            "单开可以免费使用所有功能, 若需要控制多个窗口需购买卡密",
            "执行速率调到2.0会导致cpu升高, 卡点几率上升, 只建议用在虎酒,百战,边关",
            "如果出现卡点, 一般是执行速率的问题, 恢复到1.0一切正常",
            "简单无脑的任务可适当提高脚本执行速率, 不建议复杂任务在2.0速率下运行",
            "如果你发现技能打不到自己身上, 说明角色名跟窗口不匹配, 请自动修正角色名",
        ]
        tip = tip_list[rnd(0, len(tip_list) - 1)]
        self.show_tip(tip)

    def on_timer_ds_timeout(self):        
        #  若距离上次心跳过去15分钟, 则退出软件
        if utils.delta_minute(self.last_heart_stamp, settings.cur_time_stamp) >= 15:
            self.show_info("与服务器断开连接...")
            self.sig_close.emit()
        if not self.chk_on_time.isChecked():
            return
        if self.chk_on_time_run_all.isChecked() and settings.cur_time_fmt[
            :5
        ] == self.tmedt_on_time_run_all.time().toString("HH:mm"):
            self.show_info("定时运行开始执行!")
            # 依次运行
            for wk in settings.worker_list:
                if wk:
                    self.tbe_console.item(wk.row, COL_RUN).setText(const.SELECTED)
        if self.chk_on_time_shut_down.isChecked() and settings.cur_time_fmt[:5]\
              == self.tmedt_on_time_shut_down.time().toString("HH:mm"):
            self.show_info("定时关机开始执行!")
            # 依次终止
            for wk in settings.worker_list:
                if wk:
                    self.tbe_console.item(wk.row, COL_END).setText(const.SELECTED)
            # 弹框提示
            msg_box = TimeMsgBox("提示", "定时关机时间到, 是否关机?", timeout=10, parent=self)
            msg_box.exec_()
            if msg_box.clickedButton() != msg_box.btn_accept:
                self.show_info("已取消关机")
                return
            # 确定关机
            settings.com_obj.exit_os()

    def on_tre_all_item_double_clicked(self, item, col):
        item_text = item.text(col)
        if item_text in ("单人任务", "团队任务", "免费功能"):
            return
        self.lst_exec.addItem(item_text)

    def on_lst_exec_item_double_clicked(self, item):
        row = self.lst_exec.row(item)
        self.lst_exec.takeItem(row)

    # 读取方案 (文件到控件)
    def on_lst_plan_item_clicked(self):
        curItem = self.lst_plan.currentItem()
        if curItem is None:
            self.show_info("失败,请选择要读取的配置文件!")
            return
        plan_name = curItem.text()
        # 读取方案配置
        cfg_plan = copy.deepcopy(settings.default_cfg_plan)
        cfg_plan.update(settings.cfg_plan_dict.get(plan_name, {}))
        # 设置到控件中
        self.read_basic_plan_setting_dict_to_control(cfg_plan)
        self.read_biz_task_setting_dict_to_control(plan_name)
        self.tab_set.setCurrentIndex(0)
        self.show_info(f"方案配置-{plan_name}, 读取完成")

    def on_lst_plan_currentTextChanged(self, cur_text):
        self.edt_plan_new_name.setText(cur_text)

    # 新建方案
    def on_btn_plan_create_clicked(self):
        plan_name = self.edt_plan_new_name.text()
        if plan_name == "":
            self.show_info("失败, 请先输入新方案名")
            return
        # 这个方案前面的数字要是之前没有的
        plan_name_digits = [
            get_start_digit(self.lst_plan.item(i).text())
            for i in range(self.lst_plan.count())
        ]
        if get_start_digit(plan_name) in plan_name_digits:
            self.show_info("失败, 方案名前面必须有数字且不能重复")
            return
        if plan_name in settings.cfg_plan_dict:  # 保存方案配置
            settings.cfg_plan_dict[plan_name] = self.get_basic_plan_setting_dict(
            )
            dict_to_json_file(settings.cfg_plan_dict, PATH_SOFTWARE_PLAN)
            return
        # 没有出现的方案，才创建
        settings.cfg_plan_dict[plan_name] = self.get_basic_plan_setting_dict()
        self.read_biz_task_setting_dict_to_control(plan_name)
        # 要保存到文件里
        dict_to_json_file(settings.cfg_plan_dict, PATH_SOFTWARE_PLAN)
        # 在lst_plan里添加方案名, 并排序
        self.lst_plan.addItem(plan_name)
        # 在每个cmb_plan里添加方案名的选项
        for row, cmb_plan in enumerate(settings.cmb_plan_list):
            cmb_plan.addItem(plan_name)
            if (
                not cmb_plan.isEnabled()
            ):  # 这里有两种情况，一种是没有woker的，一种是有worker在运行被禁用的
                wk = settings.worker_list[row]
                if not wk:
                    cmb_plan.setCurrentIndex(-1)
        # 保存到json文件
        dict_to_json_file(settings.cfg_plan_dict, PATH_SOFTWARE_PLAN)
        self.cmb_set_plan_get_wnd.addItem(plan_name)
        self.cmb_set_plan_db_col.addItem(plan_name)
        self.show_info("新建方案成功!")

    # 重命名方案
    def on_btn_plan_rename_clicked(self):
        curItem = self.lst_plan.currentItem()
        if curItem is None:
            self.show_info("失败, 请先选择要重命名哪个方案!")
            return
        old_plan_name = curItem.text()
        new_plan_name = self.edt_plan_new_name.text()
        if new_plan_name == "":
            self.show_info("请先输入新方案名")
            return
        # 重命名key
        settings.cfg_plan_dict[new_plan_name] = settings.cfg_plan_dict.pop(
            old_plan_name
        )
        dict_to_json_file(settings.cfg_plan_dict, PATH_SOFTWARE_PLAN)
        # 在lst_plan里修改方案名
        self.lst_plan.takeItem(self.lst_plan.row(curItem))
        self.lst_plan.addItem(new_plan_name)
        # 在cmb_plan里修改方案名
        for cmb_plan in settings.cmb_plan_list:
            idx = cmb_plan.findText(old_plan_name)
            if idx != -1:
                cmb_plan.removeItem(idx)
                cmb_plan.addItem(new_plan_name)
        idx = self.cmb_set_plan_get_wnd.findText(old_plan_name)
        if idx != -1:
            self.cmb_set_plan_get_wnd.removeItem(idx)
            self.cmb_set_plan_get_wnd.addItem(new_plan_name)
        idx = self.cmb_set_plan_db_col.findText(old_plan_name)
        if idx != -1:
            self.cmb_set_plan_db_col.removeItem(idx)
            self.cmb_set_plan_db_col.addItem(new_plan_name)
        self.show_info("重命名方案成功!")

    # 删除方案
    def on_action_lst_plan_del_triggered(self):
        cur_item = self.lst_plan.currentItem()
        if cur_item is None:
            self.show_info("请先选中你要删除的方案")
            return
        plan_name = cur_item.text()
        # 从 方案配置字典中移除该方案
        settings.cfg_plan_dict.pop(plan_name)
        dict_to_json_file(settings.cfg_plan_dict, PATH_SOFTWARE_PLAN)
        # 删除 方案列表中的对应项
        row = self.lst_plan.row(cur_item)
        self.lst_plan.takeItem(row)
        # 删除 所有方案选择下拉框中的对应项
        for cmb_plan in settings.cmb_plan_list:
            cur_idx = cmb_plan.findText(plan_name)
            if cur_idx >= 0:  # 找到才删
                cmb_plan.removeItem(cur_idx)
        idx = self.cmb_set_plan_get_wnd.findText(plan_name)
        if idx != -1:
            self.cmb_set_plan_get_wnd.removeItem(idx)
        idx = self.cmb_set_plan_db_col.findText(plan_name)
        if idx != -1:
            self.cmb_set_plan_db_col.removeItem(idx)
        self.show_info("方案删除成功")
        
    def on_chk_shuaye_terse_bb_stateChanged(self, state):
        if state != Qt.Checked:
            return
        # 获取当前的焦点控件
        focus_widget = QApplication.focusWidget()
        if focus_widget != self.chk_shuaye_terse_bb:
            return
        TimeMsgBox("注意", "精炼BB会把所有 白色麒麟 精炼 \n请务必把所有重要BB:\n改名 或 转金麒麟!!!\n", parent=self).exec_()

    def on_btn_cfg_save_clicked(self):
        idx = self.stack_widget.currentIndex()
        if idx in [0, 1]:
            self.common_cfg_save()
        elif idx == 2:
            self.plan_cfg_save()

    def on_btn_open_folder_game_path_clicked(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec_():
            file_paths = dialog.selectedFiles()
            if not (file_paths and file_paths[0].endswith("update.exe")):
                self.show_info("请选择游戏根目录下的update.exe!")
                return
            exe_path = file_paths[0]
            self.edt_game_path.setText(exe_path)

    def on_btn_open_game_clicked(self):
        game_path = self.edt_game_path.text()
        if not game_path:  # 如果没有输入路径
            self.show_info("请先输入游戏根目录下的update.exe!")
            return
        settings.global_wk.run_app(game_path, mode=1)

    def on_exec_rate_slider_value_changed(self, value):
        settings.exec_rate = value / 100  # 在0.2 - 3之间
        self.lbe_exec_rate.setText("{:.2f}".format(settings.exec_rate))

    def on_h_header_double_clicked(self, col):
        log.info(f"第{col}列双击了")
        if col == COL_HWND:
            self.show_info("双击 [窗口句柄] 表头, 一键获取所有窗口")
            self.one_key_get_wnd()

        elif col == COL_PLAN:
            plan_idx = int(settings.cfg_common["双击方案列设置方案"])
            self.show_info(f"双击 [方案选择] 表头, 一键设置为{plan_idx}号方案")
            self.one_key_set_plan(plan_idx)

        elif col == COL_RUN:
            self.show_info("双击 [运行] 表头, 一键运行表格上的所有窗口")
            for wk in settings.worker_list:
                if wk is None:
                    continue
                self.tbe_console.item(wk.row, col).setText(SELECTED)

        elif col == COL_PAUSE:
            self.show_info("双击 [暂停] 表头, 一键暂停表格上的所有窗口")
            for wk in settings.worker_list:
                if wk is None:
                    continue
                if self.tbe_console.item(wk.row, COL_RUN).text():
                    self.tbe_console.item(wk.row, col).setText(SELECTED)

        elif col == COL_END:
            self.show_info("双击 [终止] 表头, 一键终止表格上的所有窗口")
            for wk in settings.worker_list:
                if wk is None:
                    continue
                if (
                    self.tbe_console.item(wk.row, COL_RUN).text()
                    or self.tbe_console.item(wk.row, COL_PAUSE).text()
                ):
                    self.tbe_console.item(wk.row, col).setText(SELECTED)

        elif col == COL_LOG:
            self.show_info("双击 [日志] 表头, 获取软件日志记录")
            # 读取内容, 设置内容
            content = file_read_content(os.path.join(PATH_SOFTWARE_LOG, 'info.log'))
            self.tbr_log.setText(content)
            # 设置标题, 将光标移到文档末, 显示
            self.diag.setWindowTitle(f"日志-本软件")
            self.tbr_log.moveCursor(QTextCursor.End)
            self.diag.show()
            self.diag.activateWindow()

    def on_v_header_double_clicked(self, row):
        log.info(f"第{row}行双击了")
        wk = settings.worker_list[row]
        if not wk:
            return
        self.show_info("双击 垂直 表头, 显示/隐藏该窗口")
        self.do_hide_show(wk)

    def on_tbe_console_cellClicked(self, row, col):
        log.info(f"第{row}行, 第{col}列单元格被双击!")
        row_num = row + 1
        if col == COL_HWND:  # 若双击"窗口"列
            self.show_info(f"单击 [窗口] 列,第{row_num}行, 显示/隐藏该窗口")
            wk = settings.worker_list[row]
            self.do_hide_show(wk)

    def on_tbe_console_cellDoubleClicked(self, row, col):
        # 若双击的列不是日志列, 且还没获取窗口
        if col != COL_LOG and not self.tbe_console.item(row, COL_HWND).text():
            self.show_info("无效操作, 请先双击 [窗口句柄] 表头获取游戏窗口")
            return
        log.info(f"第{row}行, 第{col}列单元格被双击!")
        row_num = row + 1
        if col == COL_HWND:  # 若双击"窗口"列
            self.show_info(f"双击 [窗口] 列,第{row_num}行, 显示该窗口")
            wk = settings.worker_list[row]
            wk.show_wnd()
            activate_wnd(wk.hwnd)

        elif col == COL_RUN:  # 若双击"运行"列
            self.show_info(f"双击 [运行] 列,第{row_num}行, 运行该窗口")
            self.tbe_console.currentItem().setText(SELECTED)

        elif col == COL_PAUSE:  # 若双击"暂停"列
            self.show_info(f"双击 [暂停] 列,第{row_num}行, 暂停该窗口")
            self.tbe_console.currentItem().setText(SELECTED)

        elif col == COL_END:  # 若双击"终止"列
            self.show_info(f"双击 [终止] 列,第{row_num}行, 终止该窗口")
            self.tbe_console.currentItem().setText(SELECTED)

        elif col == COL_LOG:  # 若双击"日志"列
            self.show_info(f"双击 [日志] 列,第{row_num}行, 显示该窗口的执行日志")
            # 先清除当前tbr日志的内容
            self.tbr_log.clear()
            # 读取内容, 设置内容
            content = file_read_content(
                f"{PATH_SOFTWARE_LOG}\\wnd_{row_num}.txt")
            self.tbr_log.setText(content)
            # 设置标题, 将光标移到文档末, 显示
            self.diag.setWindowTitle(f"日志-窗口{row_num}")
            self.tbr_log.moveCursor(QTextCursor.End)
            self.diag.show()
            self.diag.activateWindow()

    def do_hide_show(self, wk: common.Worker):
        if not wk:
            return
        try:
            x, y = get_wnd_pos(wk.hwnd)
        except:
            wk.record("窗口已不存在")
            self.rmv_wnd_from_console(wk)
            return
        if x != HIDE_X:
            wk.hide_wnd(x, y)
        else:
            wk.show_wnd()
            activate_wnd(wk.hwnd)

    def on_tbe_console_itemChanged(self, item):
        col = item.column()
        if col > COL_END or col < COL_RUN or item.text() == "":
            return
        row = item.row()
        
        wk = settings.worker_list[row]
        if not wk:
            self.tbe_console.item(row, col).setText("")
            return
                
        info = base64.b64decode("6LaF5Ye65Y2h5a+G5p2D55uKLCDlkK/liqjnqpflj6PlpLHotKU=")  # "超出卡密权益, 启动窗口失败"
        info = info.decode("utf-8")
        if col == COL_RUN:
            if self.count_run_num() > settings.card_rights:
                wk.record(info)
                self.show_info(info)
                self.tbe_console.item(row, col).setText("")
                return
            self.tbe_console.item(row, COL_PAUSE).setText("")
            self.tbe_console.item(row, COL_END).setText("")
            Thread(target=self.thread_run, args=(wk,), daemon=True).start()

        elif col == COL_PAUSE:
            if self.tbe_console.item(row, COL_RUN).text():  # 运行中才能暂停
                self.tbe_console.item(row, COL_RUN).setText("")
                self.tbe_console.item(row, COL_END).setText("")
                Thread(target=self.thread_pause, args=(wk,), daemon=True).start()
            else:
                self.tbe_console.item(row, COL_PAUSE).setText("")

        elif col == COL_END:
            if (
                self.tbe_console.item(row, COL_RUN).text()
                or self.tbe_console.item(row, COL_PAUSE).text()
            ):  # 运行或暂停中才能终止
                self.tbe_console.item(row, COL_RUN).setText("")
                self.tbe_console.item(row, COL_PAUSE).setText("")
                Thread(target=self.thread_end, args=(wk,), daemon=True).start()
            else:
                self.tbe_console.item(row, COL_END).setText("")

    def count_run_num(self):
        count = 0
        for wk in settings.worker_list:
            if wk is None:
                continue
            if self.tbe_console.item(wk.row, COL_RUN).text():
                count += 1
        return count

    # 方案改变
    def on_cmb_plan_cur_text_changed(self, plan_name):
        cmb_plan = self.sender()
        row = settings.cmb_plan_list.index(cmb_plan)
        wk: common.Worker = settings.worker_list[row]
        if wk is None:
            return
        self.update_worker_plan_info(wk, row, plan_name)

    def on_cmb_set_plan_db_col_cur_index_changed(self, idx):
        settings.cfg_common["双击方案列设置方案"] = idx
        self.show_info(f"双击方案列设置方案{idx}, 临时设置成功！")

    def on_cmb_arrange_get_wnd_cur_index_changed(self, idx):
        settings.cfg_common["获取窗口后排列方式"] = idx
        self.show_info(f"获取窗口后排列方式{idx}, 临时设置成功！")

    def on_cmb_set_plan_get_wnd_cur_index_changed(self, idx):
        settings.cfg_common["获取窗口后设置方案"] = idx
        self.show_info(f"获取窗口后设置方案{idx}, 临时设置成功！")

    def on_tab_set_currentChanged(self, idx):
        map_dict = {0: "基本设置", 1: "单人配置1", 2: "单人配置2", 3: "组队配置1"}
        self.show_tip(f"切换到 {map_dict[idx]} 窗口")

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        self.show_tip(f"切换到 {action_name} 窗口")
        if action is self.action_readme:
            self.stack_widget.setCurrentIndex(0)
            self.action_console.setChecked(False)
            self.action_plan.setChecked(False)
        if action is self.action_console:
            self.stack_widget.setCurrentIndex(1)
            self.action_readme.setChecked(False)
            self.action_plan.setChecked(False)
        if action is self.action_plan:
            self.stack_widget.setCurrentIndex(2)
            self.action_readme.setChecked(False)
            self.action_console.setChecked(False)

    def on_tool_bar_orientationChanged(self, orientation):
        if orientation == Qt.Horizontal:
            self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        else:
            self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

    def on_action_copy_exec_list_triggered(self):
        self.exec_list_copy = [
            self.lst_exec.item(idx).text() for idx in range(self.lst_exec.count())
        ]
        if self.exec_list_copy:
            self.show_info("执行列表复制成功")
            self.action_paste_exec_list.setEnabled(True)

    def on_action_paste_exec_list_triggered(self):
        self.lst_exec.clear()
        self.lst_exec.addItems(self.exec_list_copy)
        self.show_info("执行列表粘贴成功")

    def send_request_heart(self, is_first=False):
        path = '/api/netauth/v1/card/get_info'
        url = settings.protocal + settings.server_host_name + path
        req_ts = str(settings.cur_time_stamp)
        body = {
            'card_number': settings.card_number,
            'machine_code': settings.machine_code,
            'user_info': json.dumps(settings.user_info),
            'req_ts': req_ts,
        }
        headers = {
            'X-Check-Sum': get_check_sum(settings.machine_code, settings.server_host_name+body["req_ts"]),
        }
        self.thd_heart_beat = ThreadSendRequestHeartBeat(url, body, headers, is_first=is_first, req_ts=req_ts)
        self.thd_heart_beat.sig_resp_heart_done.connect(self.on_resp_heart)
        self.thd_heart_beat.start()
    
    def on_resp_heart(self, is_first, req_ts, status_code, json_resp):
        if status_code == 200:
            self.heart_fail_count = 0
            server_check_sum = json_resp.get("check_sum", "")
            if self.verify_server_check_sum(server_check_sum, req_ts):
                # 正常则刷新权益
                due_ts = int(json_resp.get("due_ts", "0"))
                self.sig_rights.emit(json_resp.get("card_rights", "One"), due_ts == 0)
                if is_first:
                    if due_ts == 0:
                        self.show_info(f"欢迎使用{APP_NAME}-单开免费版")
                    elif due_ts == -1:
                        self.show_info(f"欢迎使用{APP_NAME}-单开VIP版")
                    else:
                        time_str = time_stamp_to_time_str(due_ts)
                        self.show_info(f"卡密到期时间:{time_str}")
                return True
        elif status_code >= 500:
            if is_first:
                self.show_info("卡密使用失败，请稍后再试")
            else:
                log.warn("与服务器通信异常...")
            self.heart_fail_count += 1
            if self.heart_fail_count >= 5:
                self.sig_rights.emit(1, True)
                self.show_info("服务器繁忙!")
            return False
        msg = json_resp.get("message", "校验和错误")
        self.show_info(f"卡密使用失败，原因：{msg}")
        if is_first:
            msg_box = TimeMsgBox("提示", f"卡密使用失败,原因:{msg}", timeout=3, parent=self)
            msg_box.exec_()
            self.sig_close.emit()
        return False
    
    def send_unbind_request(self):
        path = '/api/netauth/v1/card/unbind'
        url = settings.protocal + settings.server_host_name + path
        body = {
            "card_number": settings.card_number,
            "machine_code": settings.machine_code,
        }
        self.thd_unbind = ThreadSendRequestUnBind(url, body)
        self.thd_unbind.sig_resp_unbind_done.connect(self.on_resp_unbind)
        self.thd_unbind.start()
        
    def on_resp_unbind(self, status_code, json_resp):
        if status_code == 200:
            msg_box = TimeMsgBox("提示", "解绑成功, 即将退出...", timeout=2, parent=self)
            msg_box.exec_()
            self.sig_close.emit()
        elif 400 <= status_code < 500:
            reason = json_resp.get("message", "未知错误")
            msg_box = TimeMsgBox("提示", f"解绑失败,原因:{reason}", parent=self)
            msg_box.exec_()
        else:
            self.show_info("解绑失败，服务器异常，稍后再试")
            
    def send_request_get_update_info(self):
        path = '/api/netauth/v1/get_update_info'
        url = settings.protocal + settings.server_host_name + path
        body = {
            'card_number': settings.card_number,
            'machine_code': settings.machine_code,
            'client_version': CLIENT_VERSION,
        }
        self.thd_check_update = ThreadCheckUpdate(url, body)
        self.thd_check_update.sig_get_download_info_finish.connect(lambda data: self.wnd_update.on_resp_update(data))
        self.thd_check_update.start()

    
    def verify_server_check_sum(self, server_check_sum, req_ts):
        # 服务端的校验和: key机器码 value=请求时间+域名
        key = settings.machine_code
        value = req_ts+settings.server_host_name
        # print(f"key:{key}, value:{value}")
        client_check_sum = get_check_sum(key, value)
        # print(f"server_check_sum:{server_check_sum}, client_check_sum:{client_check_sum}")
        return client_check_sum == server_check_sum

    def on_edt_card_key_editingFinished(self):
        settings.card_rights = 1
        settings.is_free = True
        settings.card_number = self.edt_card_key.text()
        self.send_request_heart(is_first=True)

    def on_btn_card_unbind_clicked(self):
        self.send_unbind_request()
        
    def on_btn_card_buy_clicked(self):
        self.show_info("发卡网暂未开放, 购买卡密请进Q群389026984联系群主")
        # webbrowser.open(settings.fa_ka_wang_url)

    def on_btn_check_update_clicked(self):
        self.wnd_update.show()
        self.send_request_get_update_info()

    def on_action_five_game_control_triggered(self):
        start_row = self.start_row
        start_col = self.start_col
        if start_col == COL_HWND:  # 显示/隐藏
            self.show_info("窗口列控五，自动显示/隐藏此区域五窗口")
            action_show = False
            for row in range(start_row, start_row + 5):
                wk = settings.worker_list[row]
                if wk is None:
                    continue
                x, _ = get_wnd_pos(wk.hwnd)
                action_show = True if x == HIDE_X else False
                break
            for row in range(start_row, start_row + 5):
                wk = settings.worker_list[row]
                if wk is None:
                    continue
                Thread(target=self.thd_hide_show, args=(
                    wk, action_show), daemon=True).start()
        elif start_col == COL_PLAN:  # 设置方案
            self.show_info("方案列控五，一键设置方案")
            for row in range(start_row, start_row + 5):
                self.set_plan(row, int(settings.cfg_common["双击方案列设置方案"]))
        elif start_col == COL_RUN:  # 运行
            self.show_info("运行列控五，自动运行此区域五窗口")
            for row in range(start_row, start_row + 5):
                self.tbe_console.item(row, COL_RUN).setText(SELECTED)
        elif start_col == COL_PAUSE:  # 暂停
            self.show_info("暂停列控五，自动暂停此区域五窗口")
            for row in range(start_row, start_row + 5):
                self.tbe_console.item(row, COL_PAUSE).setText(SELECTED)
        elif start_col == COL_END:  # 终止
            self.show_info("终止列控五，自动终止此区域五窗口")
            for row in range(start_row, start_row + 5):
                self.tbe_console.item(row, COL_END).setText(SELECTED)
        elif start_col == COL_LOG:  # 强制退出
            self.show_info("日志列控五，自动强退此区域五窗口")
            ret = QMessageBox.warning(
                self,
                "警告",
                "是否要强制结束此区域五窗口?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if ret != QMessageBox.Yes:
                return
            for row in range(start_row, start_row + 5):
                wk = settings.worker_list[row]
                if not wk:
                    continue
                self.rmv_wnd_from_console(wk)
                terminate_wnd(wk.hwnd)
        elif start_col in [COL_NAME, COL_ACCOUNT]:  # 自动登录
            self.show_info("账号列控五，自动登录此区域五窗口")
            self.login_specified_game_wnd(start_row, start_row + 5)

    def login_specified_game_wnd(self, start_row, end_row):
        game_path = self.check_game_path()
        if not game_path:
            return
        self.btn_start_auto_login.setEnabled(False)
        self.game_login_thread = ThreadLogin(
            game_path, start_row, end_row)
        self.game_login_thread.start()
        self.btn_stop_auto_login.setEnabled(True)

    def on_action_clear_sel_wnd_triggered(self):
        for row in self.selected_rows:
            wk = settings.worker_list[row]
            if not wk:
                continue
            self.rmv_wnd_from_console(wk)

    def on_action_hide_show_sel_wnd_triggered(self):
        action_show = False
        for row in self.selected_rows:
            wk = settings.worker_list[row]
            if wk is None:
                continue
            x, _ = get_wnd_pos(wk.hwnd)
            action_show = True if x == HIDE_X else False
            break
        for row in self.selected_rows:
            wk = settings.worker_list[row]
            if wk is None:
                continue
            Thread(target=self.thd_hide_show, args=(
                wk, action_show), daemon=True).start()

    def on_action_force_exit_sel_wnd_triggered(self):
        ret = QMessageBox.warning(
            self,
            "警告",
            "是否要强制结束选中游戏窗口?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if ret != QMessageBox.Yes:
            return
        for row in self.selected_rows:
            wk = settings.worker_list[row]
            if not wk:
                continue
            self.rmv_wnd_from_console(wk)
            terminate_wnd(wk.hwnd)

    def on_action_login_sel_wnd_triggered(self):
        start_row = self.selected_rows[0]
        end_row = self.selected_rows[-1]
        self.login_specified_game_wnd(start_row, end_row+1)

    def on_action_five_hide_show_triggered(self):
        start_row = self.start_row
        for row in range(start_row, start_row + 5):
            wk = settings.worker_list[row]
            if not wk:
                continue
            x, y = get_wnd_pos(wk.hwnd)
            if x != HIDE_X:  # 在显示则隐藏
                wk.hide_wnd(x, y)
            else:  # 在隐藏则显示
                wk.show_wnd()

    def update_worker_plan_info(self, wk: common.Worker, row: int, plan_name: str):
        old_plan_name = wk.plan_name
        wk.plan_name = plan_name
        wk.cfg_plan = copy.deepcopy(settings.default_cfg_plan)
        wk.cfg_plan.update(settings.cfg_plan_dict.get(plan_name, {}))
        if wk.cur_task:
            wk.cfg_plan_task = wk.cfg_plan[wk.cur_task]
        TaskBase.update_wk_fight_pb_info(wk)
        self.update_cmb_plan_tooltip(row)
        if old_plan_name != plan_name:
            wk.record(f"窗口已更换为方案:{plan_name}")
        else:
            wk.record(f"当前方案更新已生效")

    def thread_run(self, wk: common.Worker):
        if wk.is_pause:  # 若暂停, 则恢复
            if wk.thread:
                wk.thread.resume()
            wk.record("窗口已恢复运行")
        elif wk.is_end:  # 若结束, 才运行
            if wk.bind_window():
                wk.record("窗口开始运行")
                wk.thread = ThreadExec(wk)
                wk.thread.start()

    def thread_pause(self, wk: common.Worker):
        wk.record("窗口即将暂停...")
        if wk.thread:
            wk.thread.pause()
        wk.record("窗口已暂停运行")

    def thread_end(self, wk: common.Worker):
        wk.record("窗口即将终止...")
        if wk.thread:
            wk.thread.end()
        # 启用cmb_plan
        cmb_plan = settings.cmb_plan_list[wk.row]
        cmb_plan.setEnabled(True)
        wk.cur_task = ""
        wk.unbind_window()
        wk.record("窗口已终止运行")
