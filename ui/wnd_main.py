# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import wnd_main_rc

class Ui_WndMain(object):
    def setupUi(self, WndMain):
        if not WndMain.objectName():
            WndMain.setObjectName(u"WndMain")
        WndMain.resize(750, 464)
        WndMain.setMinimumSize(QSize(0, 0))
        WndMain.setMaximumSize(QSize(2000, 2000))
        icon = QIcon()
        icon.addFile(u":/xxx.ico", QSize(), QIcon.Normal, QIcon.Off)
        WndMain.setWindowIcon(icon)
        WndMain.setWindowOpacity(1.000000000000000)
        WndMain.setAutoFillBackground(False)
        WndMain.setStyleSheet(u"* {\n"
"    font-size: 11px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"}\n"
"QTableView {\n"
"    background: white;\n"
"    selection-color: #000000; \n"
"    gridline-color: rgb(213, 213, 213); \n"
"	selection-background-color: #a1b1c9;\n"
"    alternate-background-color: rgb(243, 246, 249);\n"
"}\n"
"")
        WndMain.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        WndMain.setDocumentMode(True)
        WndMain.setDockNestingEnabled(True)
        WndMain.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AnimatedDocks)
        self.action_console = QAction(WndMain)
        self.action_console.setObjectName(u"action_console")
        self.action_console.setCheckable(True)
        icon1 = QIcon()
        icon1.addFile(u":/control8.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_console.setIcon(icon1)
        self.action_plan = QAction(WndMain)
        self.action_plan.setObjectName(u"action_plan")
        self.action_plan.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(u":/plan7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_plan.setIcon(icon2)
        self.action_readme = QAction(WndMain)
        self.action_readme.setObjectName(u"action_readme")
        self.action_readme.setCheckable(True)
        self.action_readme.setChecked(True)
        icon3 = QIcon()
        icon3.addFile(u":/gnrl7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_readme.setIcon(icon3)
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.stack_widget = QStackedWidget(self.centralwidget)
        self.stack_widget.setObjectName(u"stack_widget")
        self.stack_widget.setFrameShape(QFrame.NoFrame)
        self.page_readme = QWidget()
        self.page_readme.setObjectName(u"page_readme")
        self.page_readme.setMinimumSize(QSize(0, 0))
        self.gridLayout_14 = QGridLayout(self.page_readme)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, -1, 2, -1)
        self.label_21 = QLabel(self.page_readme)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_29.addWidget(self.label_21)

        self.edt_card_key = QLineEdit(self.page_readme)
        self.edt_card_key.setObjectName(u"edt_card_key")
        self.edt_card_key.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_29.addWidget(self.edt_card_key)

        self.btn_card_unbind = QPushButton(self.page_readme)
        self.btn_card_unbind.setObjectName(u"btn_card_unbind")

        self.horizontalLayout_29.addWidget(self.btn_card_unbind)

        self.btn_card_buy = QPushButton(self.page_readme)
        self.btn_card_buy.setObjectName(u"btn_card_buy")

        self.horizontalLayout_29.addWidget(self.btn_card_buy)

        self.btn_check_update = QPushButton(self.page_readme)
        self.btn_check_update.setObjectName(u"btn_check_update")

        self.horizontalLayout_29.addWidget(self.btn_check_update)


        self.verticalLayout_14.addLayout(self.horizontalLayout_29)

        self.textBrowser = QTextBrowser(self.page_readme)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_14.addWidget(self.textBrowser)


        self.gridLayout_14.addLayout(self.verticalLayout_14, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_readme)
        self.page_console = QWidget()
        self.page_console.setObjectName(u"page_console")
        self.page_console.setMinimumSize(QSize(0, 0))
        self.gridLayout_5 = QGridLayout(self.page_console)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.page_console)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.tbe_console = QTableWidget(self.splitter)
        if (self.tbe_console.columnCount() < 10):
            self.tbe_console.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tbe_console.rowCount() < 60):
            self.tbe_console.setRowCount(60)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tbe_console.setVerticalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(10, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(11, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(12, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(13, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(14, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(15, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(16, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(17, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(18, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(19, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(20, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(21, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(22, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(23, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(24, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(25, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(26, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(27, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(28, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(29, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(30, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(31, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(32, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(33, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(34, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(35, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(36, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(37, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(38, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(39, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(40, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(41, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(42, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(43, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(44, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(45, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(46, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(47, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(48, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(49, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(50, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(51, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(52, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(53, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(54, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(55, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(56, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(57, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(58, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(59, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tbe_console.setItem(0, 0, __qtablewidgetitem70)
        self.tbe_console.setObjectName(u"tbe_console")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbe_console.sizePolicy().hasHeightForWidth())
        self.tbe_console.setSizePolicy(sizePolicy)
        self.tbe_console.setMaximumSize(QSize(16777215, 16777215))
        self.tbe_console.setFrameShadow(QFrame.Raised)
        self.tbe_console.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tbe_console.setEditTriggers(QAbstractItemView.CurrentChanged)
        self.tbe_console.setAlternatingRowColors(False)
        self.tbe_console.setShowGrid(True)
        self.tbe_console.setGridStyle(Qt.SolidLine)
        self.tbe_console.setCornerButtonEnabled(False)
        self.tbe_console.setRowCount(60)
        self.splitter.addWidget(self.tbe_console)
        self.tbe_console.horizontalHeader().setCascadingSectionResizes(True)
        self.tbe_console.horizontalHeader().setMinimumSectionSize(30)
        self.tbe_console.horizontalHeader().setStretchLastSection(True)
        self.tbe_console.verticalHeader().setVisible(False)
        self.tbe_console.verticalHeader().setMinimumSectionSize(22)
        self.tbe_console.verticalHeader().setDefaultSectionSize(22)
        self.tbe_console.verticalHeader().setStretchLastSection(False)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 140))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(3)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.edt_game_path = QLineEdit(self.groupBox_3)
        self.edt_game_path.setObjectName(u"edt_game_path")
        self.edt_game_path.setMinimumSize(QSize(0, 0))
        self.edt_game_path.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_35.addWidget(self.edt_game_path)

        self.btn_open_folder_game_path = QToolButton(self.groupBox_3)
        self.btn_open_folder_game_path.setObjectName(u"btn_open_folder_game_path")
        icon4 = QIcon()
        icon4.addFile(u":/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_folder_game_path.setIcon(icon4)
        self.btn_open_folder_game_path.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_35.addWidget(self.btn_open_folder_game_path)

        self.btn_open_game = QToolButton(self.groupBox_3)
        self.btn_open_game.setObjectName(u"btn_open_game")

        self.horizontalLayout_35.addWidget(self.btn_open_game)


        self.gridLayout_4.addLayout(self.horizontalLayout_35, 0, 0, 1, 2)

        self.groupBox_10 = QGroupBox(self.groupBox_3)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_3 = QGridLayout(self.groupBox_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.chk_arrange_get_wnd = QCheckBox(self.groupBox_10)
        self.chk_arrange_get_wnd.setObjectName(u"chk_arrange_get_wnd")

        self.gridLayout_3.addWidget(self.chk_arrange_get_wnd, 0, 0, 1, 1)

        self.cmb_arrange_get_wnd = QComboBox(self.groupBox_10)
        self.cmb_arrange_get_wnd.addItem("")
        self.cmb_arrange_get_wnd.addItem("")
        self.cmb_arrange_get_wnd.addItem("")
        self.cmb_arrange_get_wnd.addItem("")
        self.cmb_arrange_get_wnd.setObjectName(u"cmb_arrange_get_wnd")
        self.cmb_arrange_get_wnd.setMinimumSize(QSize(0, 20))
        self.cmb_arrange_get_wnd.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.cmb_arrange_get_wnd, 0, 1, 1, 1)

        self.chk_set_plan_get_wnd = QCheckBox(self.groupBox_10)
        self.chk_set_plan_get_wnd.setObjectName(u"chk_set_plan_get_wnd")
        self.chk_set_plan_get_wnd.setChecked(True)

        self.gridLayout_3.addWidget(self.chk_set_plan_get_wnd, 1, 0, 1, 1)

        self.cmb_set_plan_get_wnd = QComboBox(self.groupBox_10)
        self.cmb_set_plan_get_wnd.setObjectName(u"cmb_set_plan_get_wnd")
        self.cmb_set_plan_get_wnd.setMinimumSize(QSize(0, 20))
        self.cmb_set_plan_get_wnd.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.cmb_set_plan_get_wnd, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_10, 0, 2, 2, 1)

        self.chk_on_time = QGroupBox(self.groupBox_3)
        self.chk_on_time.setObjectName(u"chk_on_time")
        self.chk_on_time.setCheckable(True)
        self.chk_on_time.setChecked(False)
        self.gridLayout_18 = QGridLayout(self.chk_on_time)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.chk_on_time_run_all = QCheckBox(self.chk_on_time)
        self.chk_on_time_run_all.setObjectName(u"chk_on_time_run_all")
        self.chk_on_time_run_all.setChecked(True)

        self.gridLayout_18.addWidget(self.chk_on_time_run_all, 0, 0, 1, 1)

        self.tmedt_on_time_run_all = QTimeEdit(self.chk_on_time)
        self.tmedt_on_time_run_all.setObjectName(u"tmedt_on_time_run_all")
        self.tmedt_on_time_run_all.setMinimumSize(QSize(0, 22))
        self.tmedt_on_time_run_all.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_18.addWidget(self.tmedt_on_time_run_all, 0, 1, 1, 1)

        self.chk_on_time_shut_down = QCheckBox(self.chk_on_time)
        self.chk_on_time_shut_down.setObjectName(u"chk_on_time_shut_down")
        self.chk_on_time_shut_down.setChecked(True)

        self.gridLayout_18.addWidget(self.chk_on_time_shut_down, 1, 0, 1, 1)

        self.tmedt_on_time_shut_down = QTimeEdit(self.chk_on_time)
        self.tmedt_on_time_shut_down.setObjectName(u"tmedt_on_time_shut_down")
        self.tmedt_on_time_shut_down.setMinimumSize(QSize(0, 22))
        self.tmedt_on_time_shut_down.setMaximumSize(QSize(16777215, 22))
        self.tmedt_on_time_shut_down.setTime(QTime(3, 0, 0))

        self.gridLayout_18.addWidget(self.tmedt_on_time_shut_down, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.chk_on_time, 0, 3, 2, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_start_auto_login = QPushButton(self.groupBox_4)
        self.btn_start_auto_login.setObjectName(u"btn_start_auto_login")

        self.horizontalLayout_11.addWidget(self.btn_start_auto_login)

        self.btn_stop_auto_login = QPushButton(self.groupBox_4)
        self.btn_stop_auto_login.setObjectName(u"btn_stop_auto_login")
        self.btn_stop_auto_login.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.btn_stop_auto_login)


        self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_11 = QGroupBox(self.groupBox_3)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_2 = QGridLayout(self.groupBox_11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_55 = QLabel(self.groupBox_11)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_18.addWidget(self.label_55)

        self.cmb_set_plan_db_col = QComboBox(self.groupBox_11)
        self.cmb_set_plan_db_col.setObjectName(u"cmb_set_plan_db_col")
        self.cmb_set_plan_db_col.setMinimumSize(QSize(0, 20))
        self.cmb_set_plan_db_col.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_18.addWidget(self.cmb_set_plan_db_col)


        self.gridLayout_2.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_11, 1, 1, 1, 1)

        self.splitter.addWidget(self.groupBox_3)

        self.gridLayout_5.addWidget(self.splitter, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_console)
        self.page_plan = QWidget()
        self.page_plan.setObjectName(u"page_plan")
        self.page_plan.setMinimumSize(QSize(0, 0))
        self.gridLayout_21 = QGridLayout(self.page_plan)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_plan_list = QWidget(self.page_plan)
        self.widget_plan_list.setObjectName(u"widget_plan_list")
        self.widget_plan_list.setMinimumSize(QSize(95, 0))
        self.widget_plan_list.setMaximumSize(QSize(95, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_plan_list)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.widget_plan_list)
        self.label_53.setObjectName(u"label_53")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy1)
        self.label_53.setMinimumSize(QSize(95, 0))
        self.label_53.setMaximumSize(QSize(95, 16777215))
        self.label_53.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_53)

        self.lst_plan = QListWidget(self.widget_plan_list)
        self.lst_plan.setObjectName(u"lst_plan")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lst_plan.sizePolicy().hasHeightForWidth())
        self.lst_plan.setSizePolicy(sizePolicy2)
        self.lst_plan.setMinimumSize(QSize(95, 0))
        self.lst_plan.setMaximumSize(QSize(95, 16777215))
        self.lst_plan.setSortingEnabled(False)

        self.verticalLayout_3.addWidget(self.lst_plan)

        self.label_54 = QLabel(self.widget_plan_list)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(95, 0))
        self.label_54.setMaximumSize(QSize(95, 16777215))

        self.verticalLayout_3.addWidget(self.label_54)

        self.edt_plan_new_name = QLineEdit(self.widget_plan_list)
        self.edt_plan_new_name.setObjectName(u"edt_plan_new_name")
        sizePolicy1.setHeightForWidth(self.edt_plan_new_name.sizePolicy().hasHeightForWidth())
        self.edt_plan_new_name.setSizePolicy(sizePolicy1)
        self.edt_plan_new_name.setMinimumSize(QSize(95, 0))
        self.edt_plan_new_name.setMaximumSize(QSize(95, 16777215))
        self.edt_plan_new_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.edt_plan_new_name)

        self.widget = QWidget(self.widget_plan_list)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(95, 0))
        self.widget.setMaximumSize(QSize(95, 16777215))
        self.horizontalLayout_13 = QHBoxLayout(self.widget)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_plan_create = QPushButton(self.widget)
        self.btn_plan_create.setObjectName(u"btn_plan_create")
        sizePolicy1.setHeightForWidth(self.btn_plan_create.sizePolicy().hasHeightForWidth())
        self.btn_plan_create.setSizePolicy(sizePolicy1)
        self.btn_plan_create.setMinimumSize(QSize(45, 0))
        self.btn_plan_create.setMaximumSize(QSize(45, 45))

        self.horizontalLayout_13.addWidget(self.btn_plan_create)

        self.btn_plan_rename = QPushButton(self.widget)
        self.btn_plan_rename.setObjectName(u"btn_plan_rename")
        sizePolicy1.setHeightForWidth(self.btn_plan_rename.sizePolicy().hasHeightForWidth())
        self.btn_plan_rename.setSizePolicy(sizePolicy1)
        self.btn_plan_rename.setMinimumSize(QSize(45, 0))
        self.btn_plan_rename.setMaximumSize(QSize(45, 45))

        self.horizontalLayout_13.addWidget(self.btn_plan_rename)


        self.verticalLayout_3.addWidget(self.widget)


        self.gridLayout_21.addWidget(self.widget_plan_list, 0, 0, 1, 1)

        self.tab_set = QTabWidget(self.page_plan)
        self.tab_set.setObjectName(u"tab_set")
        self.tab_set.setMinimumSize(QSize(0, 0))
        self.tab_set.setMaximumSize(QSize(16777215, 16777215))
        self.tab_set.setStyleSheet(u"QScrollArea { background: transparent; }\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"QScrollArea > QWidget > QScrollBar { background: palette(base); }\n"
"QScrollArea{\n"
"border: 0px solid;\n"
"border-right-width: 1px;\n"
"border-right-color: #dcdbdc;\n"
"background-color: #fcfcfc;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
"background: #fcfcfc;\n"
"width: 10px;\n"
"margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: #b0b0b0;\n"
"min-height: 20px;\n"
"border-radius: 5px;\n"
"border: none;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"background: #a0a0a0;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBa"
                        "r::sub-page:vertical {\n"
"background: none;\n"
"width: 0px;\n"
"height: 0px;\n"
"}\n"
"")
        self.tab_set.setTabPosition(QTabWidget.North)
        self.tab_set.setTabShape(QTabWidget.Rounded)
        self.tab_set.setIconSize(QSize(32, 32))
        self.tab_basic = QWidget()
        self.tab_basic.setObjectName(u"tab_basic")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_basic)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_49 = QLabel(self.tab_basic)
        self.label_49.setObjectName(u"label_49")
        sizePolicy1.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy1)
        self.label_49.setMinimumSize(QSize(55, 17))
        self.label_49.setMaximumSize(QSize(55, 17))
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_49)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tre_all = QTreeWidget(self.tab_basic)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.tre_all.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.tre_all.setObjectName(u"tre_all")
        sizePolicy2.setHeightForWidth(self.tre_all.sizePolicy().hasHeightForWidth())
        self.tre_all.setSizePolicy(sizePolicy2)
        self.tre_all.setMinimumSize(QSize(84, 0))
        self.tre_all.setMaximumSize(QSize(84, 16777215))
        self.tre_all.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tre_all.setAutoExpandDelay(0)
        self.tre_all.setIndentation(7)
        self.tre_all.setAnimated(True)
        self.tre_all.header().setVisible(False)

        self.verticalLayout_4.addWidget(self.tre_all)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_52 = QLabel(self.tab_basic)
        self.label_52.setObjectName(u"label_52")
        sizePolicy1.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy1)
        self.label_52.setMinimumSize(QSize(55, 17))
        self.label_52.setMaximumSize(QSize(55, 17))
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_52)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.lst_exec = QListWidget(self.tab_basic)
        self.lst_exec.setObjectName(u"lst_exec")
        sizePolicy2.setHeightForWidth(self.lst_exec.sizePolicy().hasHeightForWidth())
        self.lst_exec.setSizePolicy(sizePolicy2)
        self.lst_exec.setMinimumSize(QSize(76, 0))
        self.lst_exec.setMaximumSize(QSize(76, 16777215))
        self.lst_exec.setDragEnabled(True)
        self.lst_exec.setDragDropMode(QAbstractItemView.DragDrop)
        self.lst_exec.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout_2.addWidget(self.lst_exec)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(self.tab_basic)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"border: 0px solid;\n"
"border-right-width: 1px;\n"
"border-right-color: #dcdbdc;\n"
"background-color: #fcfcfc;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
"background: #f5f5f7;\n"
"width: 10px;\n"
"margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: #b0b0b0;\n"
"min-height: 20px;\n"
"border-radius: 5px;\n"
"border: none;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"background: #909090;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"width: 0px;\n"
"height: 0px;\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 447, 800))
        self.gridLayout_26 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 6, 0)
        self.widget_config_basic = QWidget(self.scrollAreaWidgetContents)
        self.widget_config_basic.setObjectName(u"widget_config_basic")
        self.widget_config_basic.setMinimumSize(QSize(0, 800))

        self.gridLayout_26.addWidget(self.widget_config_basic, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_5.addWidget(self.scrollArea)

        self.tab_set.addTab(self.tab_basic, "")
        self.tab_single = QWidget()
        self.tab_single.setObjectName(u"tab_single")
        self.horizontalLayout_22 = QHBoxLayout(self.tab_single)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.tab_single)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollArea { background: transparent; }\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"QScrollArea > QWidget > QScrollBar { background: palette(base); }\n"
"QScrollArea{\n"
"border: 0px solid;\n"
"border-right-width: 1px;\n"
"border-right-color: #dcdbdc;\n"
"background-color: #fcfcfc;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
"background: #fcfcfc;\n"
"width: 10px;\n"
"margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: #b0b0b0;\n"
"min-height: 20px;\n"
"border-radius: 5px;\n"
"border: none;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"background: #a0a0a0;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBa"
                        "r::sub-page:vertical {\n"
"background: none;\n"
"width: 0px;\n"
"height: 0px;\n"
"}\n"
"")
        self.scrollArea_2.setFrameShape(QFrame.Box)
        self.scrollArea_2.setFrameShadow(QFrame.Raised)
        self.scrollArea_2.setMidLineWidth(0)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 623, 432))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_config_single = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_config_single.setObjectName(u"widget_config_single")
        self.widget_config_single.setMinimumSize(QSize(0, 432))

        self.gridLayout_7.addWidget(self.widget_config_single, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_22.addWidget(self.scrollArea_2)

        self.tab_set.addTab(self.tab_single, "")
        self.tab_team = QWidget()
        self.tab_team.setObjectName(u"tab_team")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_team)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.tab_team)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"QScrollArea { background: transparent; }\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"QScrollArea > QWidget > QScrollBar { background: palette(base); }\n"
"QScrollArea{\n"
"border: 0px solid;\n"
"border-right-width: 1px;\n"
"border-right-color: #dcdbdc;\n"
"background-color: #fcfcfc;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
"background: #fcfcfc;\n"
"width: 10px;\n"
"margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: #b0b0b0;\n"
"min-height: 20px;\n"
"border-radius: 5px;\n"
"border: none;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"background: #a0a0a0;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBa"
                        "r::sub-page:vertical {\n"
"background: none;\n"
"width: 0px;\n"
"height: 0px;\n"
"}\n"
"")
        self.scrollArea_3.setFrameShape(QFrame.Box)
        self.scrollArea_3.setFrameShadow(QFrame.Raised)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 623, 500))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_config_team = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_config_team.setObjectName(u"widget_config_team")
        self.widget_config_team.setMinimumSize(QSize(0, 500))

        self.gridLayout_8.addWidget(self.widget_config_team, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_3.addWidget(self.scrollArea_3)

        self.tab_set.addTab(self.tab_team, "")
        self.tab_other = QWidget()
        self.tab_other.setObjectName(u"tab_other")
        self.horizontalLayout_21 = QHBoxLayout(self.tab_other)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.tab_other)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"QScrollArea { background: transparent; }\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"QScrollArea > QWidget > QScrollBar { background: palette(base); }\n"
"QScrollArea{\n"
"border: 0px solid;\n"
"border-right-width: 1px;\n"
"border-right-color: #dcdbdc;\n"
"background-color: #fcfcfc;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
"background: #fcfcfc;\n"
"width: 10px;\n"
"margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: #b0b0b0;\n"
"min-height: 20px;\n"
"border-radius: 5px;\n"
"border: none;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"background: #a0a0a0;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"border: 0px solid grey;\n"
"background: #32CC99;\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBa"
                        "r::sub-page:vertical {\n"
"background: none;\n"
"width: 0px;\n"
"height: 0px;\n"
"}\n"
"")
        self.scrollArea_4.setFrameShape(QFrame.Box)
        self.scrollArea_4.setFrameShadow(QFrame.Raised)
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 623, 500))
        self.gridLayout_11 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_config_other = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_config_other.setObjectName(u"widget_config_other")
        self.widget_config_other.setMinimumSize(QSize(0, 500))

        self.gridLayout_11.addWidget(self.widget_config_other, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_21.addWidget(self.scrollArea_4)

        self.tab_set.addTab(self.tab_other, "")

        self.gridLayout_21.addWidget(self.tab_set, 0, 1, 1, 1)

        self.stack_widget.addWidget(self.page_plan)

        self.gridLayout_6.addWidget(self.stack_widget, 0, 0, 1, 1)

        WndMain.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(WndMain)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setSizeGripEnabled(False)
        WndMain.setStatusBar(self.status_bar)
        self.tool_bar = QToolBar(WndMain)
        self.tool_bar.setObjectName(u"tool_bar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tool_bar.sizePolicy().hasHeightForWidth())
        self.tool_bar.setSizePolicy(sizePolicy3)
        self.tool_bar.setMaximumSize(QSize(16777215, 16777215))
        self.tool_bar.setAutoFillBackground(True)
        self.tool_bar.setStyleSheet(u"* {\n"
"    font-size: 12px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"}\n"
"QTableView {\n"
"    background: white;\n"
"    selection-color: #000000; \n"
"    gridline-color: rgb(213, 213, 213); \n"
"	selection-background-color: #a1b1c9;\n"
"    alternate-background-color: rgb(243, 246, 249);\n"
"}\n"
"QTableView::item:hover	{\n"
"    background-color: #a1b1c9;\n"
"}\n"
"")
        self.tool_bar.setMovable(True)
        self.tool_bar.setAllowedAreas(Qt.AllToolBarAreas)
        self.tool_bar.setOrientation(Qt.Horizontal)
        self.tool_bar.setIconSize(QSize(16, 16))
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tool_bar.setFloatable(True)
        WndMain.addToolBar(Qt.BottomToolBarArea, self.tool_bar)

        self.tool_bar.addAction(self.action_readme)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.action_console)
        self.tool_bar.addAction(self.action_plan)

        self.retranslateUi(WndMain)

        self.stack_widget.setCurrentIndex(1)
        self.tab_set.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"\u5668\u7075", None))
        self.action_console.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u63a7\u5236", None))
#if QT_CONFIG(shortcut)
        self.action_console.setShortcut(QCoreApplication.translate("WndMain", u"Alt+2", None))
#endif // QT_CONFIG(shortcut)
        self.action_plan.setText(QCoreApplication.translate("WndMain", u"\u65b9\u6848\u914d\u7f6e", None))
#if QT_CONFIG(shortcut)
        self.action_plan.setShortcut(QCoreApplication.translate("WndMain", u"Alt+3", None))
#endif // QT_CONFIG(shortcut)
        self.action_readme.setText(QCoreApplication.translate("WndMain", u"\u4f7f\u7528\u8bf4\u660e", None))
#if QT_CONFIG(shortcut)
        self.action_readme.setShortcut(QCoreApplication.translate("WndMain", u"Alt+1", None))
#endif // QT_CONFIG(shortcut)
        self.label_21.setText(QCoreApplication.translate("WndMain", u"\u8f93\u5165\u5361\u5bc6\uff1a", None))
        self.btn_card_unbind.setText(QCoreApplication.translate("WndMain", u"\u89e3\u7ed1\u673a\u5668", None))
        self.btn_card_buy.setText(QCoreApplication.translate("WndMain", u"\u8d2d\u4e70\u5361\u5bc6", None))
        self.btn_check_update.setText(QCoreApplication.translate("WndMain", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.textBrowser.setHtml(QCoreApplication.translate("WndMain", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei'; font-size:11px; font-weight:400; font-style:normal;\">\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u672c\u8f6f\u4ef6\u91c7\u7528\u5b89\u88c5\u5305\u5f62\u5f0f, \u53ef\u4ee5\u6307\u5b9a\u5b89\u88c5\u76ee\u5f55, \u5b89\u88c5\u65f6\u52fe\u9009\u521b\u5efa\u684c\u9762\u5feb\u6377\u65b9\u5f0f, \u88c5\u5b8c\u540e\u53ef\u4ee5\u5220\u9664\u5b89\u88c5\u5305,  \u7136\u540e\u5bf9</span><span style=\" font-size:10pt; color:#ff0000;\">\u684c\u9762\u5feb\u6377\u65b9\u5f0f-\u53f3\u952e-\u5c5e\u6027-\u517c\u5bb9\u6027-\u52fe\u9009"
                        "\u4ee5\u7ba1\u7406\u5458\u8eab\u4efd\u8fd0\u884c\u6b64\u7a0b\u5e8f-\u786e\u5b9a</span><span style=\" font-size:10pt;\">, \u4ee5\u540e\u5c31\u53ef\u4ee5\u76f4\u63a5\u53cc\u51fb\u684c\u9762\u56fe\u6807\u542f\u52a8\u811a\u672c. \u5fc5\u987b\u7ba1\u7406\u5458\u6743\u9650 </span><span style=\" font-size:10pt; color:#ff0000;\">\u5426\u5219\u811a\u672c\u8fd0\u884c\u65f6\u6e38\u620f\u7a97\u53e3\u65e0\u53cd\u5e94</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u8bbe\u7f6e-</span><span style=\" font-size:11px; color:#ff0000;\">\u7f29\u653e\u5fc5\u987b\u8bbe\u7f6e\u4e3a100%</span><span style=\" font-size:11px;\">, \u6e38\u620f\u7a97\u53e3</span><span style=\" font-size:11px; color:#ff0000;\">\u4e0d\u80fd\u6700\u5c0f\u5316</span><span style=\" font-size:11px;\">\u8fd0\u884c\uff0c\u5982\u6709\u9700\u8981\u53ef\u4ee5\u4f7f\u7528\u672c</span><span style=\" font-size:11px; colo"
                        "r:#000000;\">\u8f6f\u4ef6\u53f3\u952e\u83dc\u5355\u7684\u9690\u85cf\u529f\u80fd</span></li>\n"
"<li style=\" font-size:10pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u5982\u679c\u6709360, \u6253\u5f00\u811a\u672c\u65f6\u5f39\u51fa\u7533\u8bf7\u7f51\u7edc\u8bbf\u95ee\u6743\u9650, \u8bf7\u653e\u884c, \u5426\u5219\u7f51\u7edc\u9a8c\u8bc1\u4e0d\u901a\u8fc7, \u65e0\u6cd5\u6b63\u5e38\u4f7f\u7528\u811a\u672c. </span><span style=\" font-size:11px; color:#ff0000;\">\u5efa\u8bae\u76f4\u63a5\u5378\u8f7d360</span><span style=\" font-size:11px;\">, \u88c5</span><span style=\" font-size:11px; color:#ff0000;\">\u817e\u8baf\u7535\u8111\u7ba1\u5bb6</span><span style=\" font-size:11px;\">, \u811a\u672c\u53d8\u4e3a\u514d\u8d39\u7248\u901a\u5e38\u662f\u8fd9\u4e2a\u539f\u56e0</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u4f7f\u7528\u65b9\u5f0f: \u70b9\u51fb \u7a97\u53e3\u63a7\u5236\uff0c </span><span style=\" font-size:11px; color:#ff0000;\">\u53cc\u51fb`\u7a97\u53e3`\u5217\u7684\u8868\u5934\u4e00\u952e\u83b7\u53d6\u6240\u6709\u7a97\u53e3(\u6216\u8005\u53f3\u952e\u83dc\u5355-\u83b7\u53d6\u6240\u6709\u7a97\u53e3)</span><span style=\" font-size:11px;\">\uff0c\u7136\u540e\u8fdb\u5230\u65b9\u6848\u914d\u7f6e\u9875\uff0c\u7136\u540e \u53cc\u51fb \u529f\u80fd\u5217\u8868 \u7684 \u529f\u80fd\u9879 \u6dfb\u52a0\u5230 \u6267\u884c\u5217\u8868\uff0c\u7136\u540e\u5207\u56de \u7a97\u53e3\u63a7\u5236\u9875\uff0c\u53cc\u51fb\u8fd0\u884c\u5217 \u5168\u90e8\u542f\u52a8\uff01\u4e5f\u53ef\u53cc\u51fb\u5355\u5143\u683c\u8fdb\u884c\u5355\u4e2a\u542f\u52a8 (\u5728\u6e38\u620f\u7a97\u53e3\u4e2d\u6309\u9f20\u6807\u4e2d\u952e\u4e5f\u80fd\u542f\u52a8)</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bloc"
                        "k-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u5728</span><span style=\" font-size:11px; color:#ff0000;\">\u7a7a\u65b9\u6848</span><span style=\" font-size:11px;\">\u6a21\u5f0f\u4e0b, \u662f\u8bfb\u53d6\u5f53\u524d\u63a7\u4ef6\u7684\u914d\u7f6e\u6765\u8fd0\u884c\u7684, \u6240\u4ee5\u4e0d\u9700\u8981\u70b9\u4fdd\u5b58, </span><span style=\" font-size:11px; color:#ff0000;\">\u540e\u7eed\u6539\u52a8\u63a7\u4ef6\u7684\u914d\u7f6e\u4e0d\u4f1a\u5f71\u54cd</span><span style=\" font-size:11px;\">\u6b63\u5728\u8fd0\u884c\u7684\u6e38\u620f\u7a97\u53e3</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u5728</span><span style=\" font-size:11px; color:#ff0000;\">\u6307\u5b9a\u65b9\u6848</span><span style=\" font-size:11px; color:#000000;\">\u6a21\u5f0f</span><span style=\" font-size:11px;\">\u4e0b, \u5728\u66f4\u6539\u63a7\u4ef6\u914d\u7f6e</span><span style"
                        "=\" font-size:11px; color:#ff0000;\">\u4fdd\u5b58</span><span style=\" font-size:11px;\">\u5230\u6307\u5b9a\u65b9\u6848\u540e, \u6240\u6709\u5728\u8fd0\u884c\u8be5\u65b9\u6848\u7684\u6e38\u620f\u7a97\u53e3\u4f1a</span><span style=\" font-size:11px; color:#ff0000;\">\u5b9e\u65f6\u751f\u6548</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">BB\u7684\u653b\u9632\u6709\u81ea\u52a8\u5224\u65ad\u6a21\u5f0f, \u662f\u8bc6\u522bBB\u5934\u50cf\u81ea\u52a8\u51b3\u5b9a\u7684\uff0c\u975e\u5e38\u9002\u5408\u9996\u53d1\u653b\u51fb\uff0c\u591aBB\u8fd0\u7b79 \u539a\u6fc0\u7834\u7684\u73a9\u5bb6\uff0c</span><span style=\" font-size:11px; color:#ff0000;\">\u4e0d\u7528\u4e2d\u9014\u6539\u653b\u9632\u4e86</span><span style=\" font-size:11px;\">\uff0c\u5bf9\u4e8e\u975e\u8981\u8ba9\u90fd\u7edf\u8fd9\u7c7bBB\u79d2\u4e94\u653b\u51fb\u7684\u975e\u4e3b\u6d41\u73a9\u5bb6\uff0c\u4e5f\u53ef\u4ee5"
                        "\u4fee\u6539\u914d\u7f6eBB\u653b\u9632\u7684\u9009\u9879</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u56de\u57ce\u8fd8\u6709 \u5f52\u9a6c \u548c F8\u6ca1\u5217\u51fa\u6765\uff0c\u662f\u56e0\u4e3a\u4e0d\u9700\u8981\u4f60\u8bbe\u7f6e\uff0c</span><span style=\" font-size:11px; color:#ff0000;\">\u6709\u5f52\u9a6c\u604b\u6808\u6280\u80fd\u5219\u81ea\u52a8\u4f18\u5148\u5f52\u9a6c, \u5355\u4eba\u4efb\u52a1\u6709\u6e38\u9a6c\u77e5\u5f52\u4f18\u5148</span><span style=\" font-size:11px; color:#000000;\">\u7528F8</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u6280\u80fd\u680f</span><span style=\" font-size:11px; color:#ff0000;\">F1-F5</span><span style=\" font-size:11px;\">\u4f9d\u6b21\u653e</span><span style=\" font-s"
                        "ize:11px; color:#ff0000;\">\u91d1\u6728\u571f\u6c34\u706b</span><span style=\" font-size:11px;\">\u5c5e\u6027\u79d2\u4e00\u62db(\u5982\u679c\u5c11\u4e00\u4e2a\u5c5e\u6027\u62db, \u6bd4\u5982\u5c11\u6797\u6ca1\u6709\u91d1\u62db, \u56e0\u4e3aF1\u91d1\u62db\u662f\u4e3a\u4e86\u514b\u6728\u7684, \u90a3\u4f60F1\u5c31\u968f\u4fbf\u653e\u4e00\u4e2a\u4e0d\u4f1a\u88ab\u6728\u514b\u7684\u5c5e\u6027\u5c31\u597d\u4e86)\uff0c</span><span style=\" font-size:11px; color:#ff0000;\">F6\u653e\u62a4\u5fc3\uff0cF7\u653e\u523a\u7a74\u6216\u8005\u72ee\u5b50\u543c</span><span style=\" font-size:11px;\">\uff0c\u8fd9\u6837\u624d\u80fd\u4fdd\u8bc1\u4eba\u7269\u4f7f\u7528\u6280\u80fd\u751f\u6548</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u8d85\u9041\u7684\u4f7f\u7528\u8981\u6dfb\u52a0\u6d3b\u52a8NPC, \u6bd4\u5982\u767e\u6218\u767e\u80dc\uff0c\u8bf7\u5728\u9041\u7532\u5929\u4e66\u9875\u9762"
                        "-\u6d3b\u52a8-</span><span style=\" font-size:11px; color:#ff0000;\">\u767e\u6218\u5c45\u58eb</span><span style=\" font-size:11px;\">-\u6dfb\u52a0\uff0c\u540d\u79f0\u4e00\u5b9a\u8981\u662f\u7cfb\u7edf\u4e0a\u5b9a\u4e49\u7684\u540d\u5b57, \u4e0d\u8981\u81ea\u5b9a\u4e49</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u8981\u6b63\u5e38\u4f7f\u7528\u7ec4\u961f\u529f\u80fd\uff0c</span><span style=\" font-size:11px; color:#ff0000;\">\u8bf7\u628a\u56db\u4e2a\u961f\u53cb\u5206\u7ec4\u5230\u597d\u53cb\u7b2c\u4e94\u9875</span><span style=\" font-size:11px;\">\uff0c\u4f1a\u81ea\u52a8\u9080\u8bf7\uff0c\u597d\u53cb\u7b2c\u4e94\u9875\u4e0d\u8981\u6709\u5176\u5b83\u4eba</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u526f\u672c"
                        "\u4e0d\u7528\u5403\u5fa1\u8d50\u91d1\u724c, </span><span style=\" font-size:11px; color:#ff0000;\">\u4e0d\u4f1a\u5361\u5947\u9047\u5bf9\u8bdd, </span><span style=\" font-size:11px; color:#000000;\">\u526f\u672c\u5185100%\u8fc7\u9a8c\u8bc1(\u8981\u501f\u52a9\u6218\u961f\u9875, \u8bb0\u5f97\u52a0\u6218\u961f)! \u62bc\u9556100%\u8fc7\u9a8c\u8bc1! \u5404\u79cd\u4efb\u52a1\u90fd\u80fd\u8fc7\u9a8c\u8bc1, \u4e5f\u662f100%\u8fc7!</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u6ce8\u610f</span><span style=\" font-size:11px; color:#ff0000;\">\u5e08\u95e8</span><span style=\" font-size:11px;\">\u9700\u8981\u5728\u80cc\u5305</span><span style=\" font-size:11px; color:#ff0000;\">\u81ea\u5907\u7269\u54c1</span><span style=\" font-size:11px;\">, \u4e00\u822c\u6839\u636e\u7b49\u7ea7\u6bb5\u4e0d\u540c, \u5c31\u90a3\u51e0\u6837\u6742\u7269\u548c\u836f\u54c1, \u5148\u51c6\u5907\u597d"
                        "\u518d\u8dd1</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u5168\u961f</span><span style=\" font-size:11px; color:#ff0000;\">\u81ea\u52a8\u8bc6\u522b\u6280\u80fd\u4f7f\u7528\u573a\u666f\uff0c\u53ea\u6709\u96be\u5ea6\u8f83\u9ad8\u7684\u4efb\u52a1\u624d\u4f1a\u7528\uff08\u5982\u8d85\u7ea7\u6311\u6218\uff0c\u6781\u9650\u6311\u6218\uff0c\u526f\u672c\uff09</span><span style=\" font-size:11px;\">\uff0c\u539a\u6fc0\u7834\u914d\u7f6e\u53ea\u7ba1\u6253\u5f00\uff0c\u65e0\u9700\u9891\u7e41\u6839\u636e\u4efb\u52a1\u8c03\u6574\u3002\u961f\u5458\u4f1a\u81ea\u52a8\u6839\u636e\u961f\u957f\u7684\u4efb\u52a1\u6765\u5224\u65ad\u662f\u5426\u4f7f\u7528\u6280\u80fd\u3002\u5982\u679c\u662f\u5355\u5f00\u7248\u73a9\u5bb6\uff0c\u4f7f\u7528\u6280\u80fd\u90a3\u91cc\u4e0d\u8981\u81ea\u52a8\u5224\u65ad\u4e86\uff0c\u8981\u9009\u5f3a\u5236\u4f7f\u7528\u624d\u4f1a\u7528\uff0c\u56e0\u4e3a\u8bfb"
                        "\u53d6\u4e0d\u5230\u961f\u957f\u7684\u6267\u884c\u4efb\u52a1</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u4f1a\u81ea\u52a8\u8865\u5145\u4f7f\u7528\u718a\u732b\u9999\uff0c\u82b1\u9732\u6c34\u3002\u8bf7\u63d0\u524d\u4e70\u597d\uff0c\u53ef\u4ee5\u4f7f\u7528 \u8d2d\u4e70\u7269\u54c1 \u529f\u80fd\u6765\u81ea\u52a8\u4e70</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u652f\u6301\u5168\u961f</span><span style=\" font-size:11px; color:#ff0000;\">\u6362\u7ebf\uff0c\u7ec4\u961f</span><span style=\" font-size:11px;\">\uff0c</span><span style=\" font-size:11px; color:#ff0000;\">\u961f\u957f\u8bbe\u7f6e\u8fd9\u4e24\u4e2a\u4efb\u52a1\u5373\u53ef</span><span style=\" font-size:11px;\">\uff0c \u5728\u6267\u884c \u961f\u5458\u6302"
                        "\u673a \u529f\u80fd\u7684\u961f\u5458\u4f1a\u8ddf\u968f\u961f\u957f \u9000\u961f\u6362\u7ebf\u540c\u610f\u7ec4\u961f\u7684</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u652f\u6301</span><span style=\" font-size:11px; color:#ff0000;\">\u8c03\u8282\u6267\u884c\u901f\u7387</span><span style=\" font-size:11px;\">\uff0c\u7535\u8111\u5feb\u6162\u90fd\u80fd\u7528</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u652f\u6301\u5b9a\u65f6\u542f\u52a8\uff0c\u6253\u725b\u4f1a\u8dd1\u56fe\uff08\u751a\u81f3\u652f\u6301\u53e4\u5893\u4e8c\u4e09\u5c42\uff0c\u79e6\u9675\u4e8c\u5c42\u54e6\uff09\uff0c</span><span style=\" font-size:11px; color:#ff0000;\">\u8d85\u5feb\u627e\u725b\u7b97\u6cd5</span><span style=\" font-size:11px;\">\uff0c"
                        "\u5230\u70b9\u81ea\u52a8\u505c\u6b62\u6267\u884c\u4e0b\u9762\u7684\u4efb\u52a1</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u4e00\u6761\u9f99\u76f4\u63a5\u8dd1\u5b8c\u6240\u6709\u4efb\u52a1\uff0c\u5148\u8dd1\u7ec4\u961f\u518d\u8dd1\u5355\u4eba\uff0c\u961f\u5458\u53f7\u8ddf\u968f\u961f\u957f\u81ea\u52a8\u79bb\u961f\u3002</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u901a\u5bb5\u5a01\u671b\u5e73\u4e71\uff0c\u4e0d\u5361\u70b9\uff0c\u88ab\u522b\u7684\u4efb\u52a1\u5e72\u6270\u4e5f\u4f1a\u81ea\u52a8\u5207\u56de\u539f\u4efb\u52a1\uff08\u4e0d\u7528\u62c5\u5fc3\u6709\u5409\u79be\u4efb\u52a1\u4e86\uff09</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u81ea\u52a8\u6279\u91cf\u4e0a\u53f7\uff0c\u81ea\u52a8\u91cd\u8fde</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u914d\u7f6e\u4fdd\u5b58\u540e</span><span style=\" font-size:11px; color:#ff0000;\">\u5b9e\u65f6\u751f\u6548</span><span style=\" font-size:11px;\">\uff0c\u65e0\u9700\u811a\u672c\u4e0a\u91cd\u65b0\u8fd0\u884c\u8be5\u7a97\u53e3</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u5404\u7a97\u53e3\u53ef\u8bbe\u7f6e\u4e0d\u540c\u65b9\u6848\uff0c\u65b9\u6848\u65e0\u9650\u521b\u5efa</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; tex"
                        "t-indent:0px;\"><span style=\" font-size:11px;\">\u4e00\u952e\u8bbe\u7f6e\u65b9\u6848\uff0c\u4e00\u952e\u8fd0\u884c/\u6682\u505c/\u7ec8\u6b62</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px; color:#ff0000;\">\u4e94\u5f00\u8fde\u63a7\uff0c\u961f\u957f\u4f1a\u4f20\u9012\u5404\u79cd\u4fe1\u53f7\u7ed9\u961f\u5458\u6302\u673a\u7684\u961f\u53cb</span><span style=\" font-size:11px;\">\uff0c\u4e0d\u540c\u961f\u4f0d\u4e92\u4e0d\u5e72\u6270</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u667a\u80fd\u6551\u4eba\u7b97\u6cd5\uff0c\u591a\u4eba\u53d7\u4f24\u4e0b\uff0c\u6bcf\u4e2a\u4eba\u90fd\u4f1a\u88ab\u6551\u5230\uff0c</span><span style=\" font-size:11px; color:#ff0000;\">\u4e0d\u4f1a\u5168\u90e8\u53ea\u6551\u540c\u4e00\u4e2a\u4eba"
                        "</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u80cc\u5305\u4f7f\u7528\u7269\u54c1\u4f1a\u4f18\u5148\u5f53\u524d\u9875\uff0c\u518d\u5207\u6362\u5176\u5b83\u9875\u5bfb\u627e</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u652f\u6301\u95ed\u5173\u8d2f\u901a\uff08\u4f1a\u81ea\u52a8\u4e0a\u4e0b\u5750\u9a91\uff09\uff0c\u662f\u5426\u4ed3\u5e93\u53d6\u51dd\u795e\u4f1a\u795e\u5e76\u4f7f\u7528\u53ef\u81ea\u7531\u642d\u914d</span></li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11px;\">\u56de\u57ce\u65b9\u5f0f\u5982\u679c\u5f00\u5c01\u7968\u6ca1\u6709\u4e86\uff0c\u4f1a</span><span style="
                        "\" font-size:11px; color:#ff0000;\">\u81ea\u52a8\u964d\u7ea7</span><span style=\" font-size:11px;\">\u4e3a\u95e8\u6d3e\u7968\uff0c\u8fd8\u6ca1\u6709\u5c31\u4ece\u4e0a\u5f80\u4e0b \u4f9d\u6b21\u964d\u7ea7\u76f4\u5230 \u8dd1\u6b65 \u5b8c\u6210\u540e\u7eed</span></li></ol></body></html>", None))
        ___qtablewidgetitem = self.tbe_console.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u83b7\u53d6\u5168\u90e8\u6e38\u620f\u7a97\u53e3\u53e5\u67c4, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u663e\u793a\u6fc0\u6d3b\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem1 = self.tbe_console.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WndMain", u"\u89d2\u8272\u540d", None));
        ___qtablewidgetitem2 = self.tbe_console.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WndMain", u"\u65b9\u6848", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u8bbe\u7f6e\u65b9\u6848", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.tbe_console.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WndMain", u"\u8fd0\u884c", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem3.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u8fd0\u884c, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u8fd0\u884c\u5355\u4e2a\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem4 = self.tbe_console.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WndMain", u"\u6682\u505c", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem4.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u6682\u505c, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u6682\u505c\u5355\u4e2a\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem5 = self.tbe_console.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WndMain", u"\u7ec8\u6b62", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem5.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u7ec8\u6b62, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u7ec8\u6b62\u5355\u4e2a\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem6 = self.tbe_console.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WndMain", u"\u65e5\u5fd7", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem6.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u663e\u793a\u672c\u8f6f\u4ef6\u65e5\u5fd7, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u663e\u793a\u5404\u7a97\u53e3\u6267\u884c\u65e5\u5fd7", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem7 = self.tbe_console.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WndMain", u"\u8d26\u53f7", None));
        ___qtablewidgetitem8 = self.tbe_console.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WndMain", u"\u5bc6\u7801", None));
        ___qtablewidgetitem9 = self.tbe_console.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WndMain", u"\u670d\u52a1\u5668", None));
        ___qtablewidgetitem10 = self.tbe_console.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("WndMain", u" 1 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem10.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem11 = self.tbe_console.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("WndMain", u" 2 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem11.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem12 = self.tbe_console.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("WndMain", u" 3 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem12.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem13 = self.tbe_console.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("WndMain", u" 4 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem13.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem14 = self.tbe_console.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("WndMain", u" 5 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem14.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem15 = self.tbe_console.verticalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("WndMain", u" 6 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem15.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem16 = self.tbe_console.verticalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("WndMain", u" 7 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem16.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem17 = self.tbe_console.verticalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("WndMain", u" 8 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem17.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem18 = self.tbe_console.verticalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("WndMain", u" 9 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem18.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem19 = self.tbe_console.verticalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("WndMain", u"10", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem19.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem20 = self.tbe_console.verticalHeaderItem(10)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("WndMain", u"11", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem20.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem21 = self.tbe_console.verticalHeaderItem(11)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("WndMain", u"12", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem21.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem22 = self.tbe_console.verticalHeaderItem(12)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("WndMain", u"13", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem22.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem23 = self.tbe_console.verticalHeaderItem(13)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("WndMain", u"14", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem23.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem24 = self.tbe_console.verticalHeaderItem(14)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("WndMain", u"15", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem24.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem25 = self.tbe_console.verticalHeaderItem(15)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("WndMain", u"16", None));
        ___qtablewidgetitem26 = self.tbe_console.verticalHeaderItem(16)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("WndMain", u"17", None));
        ___qtablewidgetitem27 = self.tbe_console.verticalHeaderItem(17)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("WndMain", u"18", None));
        ___qtablewidgetitem28 = self.tbe_console.verticalHeaderItem(18)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("WndMain", u"19", None));
        ___qtablewidgetitem29 = self.tbe_console.verticalHeaderItem(19)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("WndMain", u"20", None));
        ___qtablewidgetitem30 = self.tbe_console.verticalHeaderItem(20)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("WndMain", u"21", None));
        ___qtablewidgetitem31 = self.tbe_console.verticalHeaderItem(21)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("WndMain", u"22", None));
        ___qtablewidgetitem32 = self.tbe_console.verticalHeaderItem(22)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("WndMain", u"23", None));
        ___qtablewidgetitem33 = self.tbe_console.verticalHeaderItem(23)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("WndMain", u"24", None));
        ___qtablewidgetitem34 = self.tbe_console.verticalHeaderItem(24)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("WndMain", u"25", None));
        ___qtablewidgetitem35 = self.tbe_console.verticalHeaderItem(25)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("WndMain", u"26", None));
        ___qtablewidgetitem36 = self.tbe_console.verticalHeaderItem(26)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("WndMain", u"27", None));
        ___qtablewidgetitem37 = self.tbe_console.verticalHeaderItem(27)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("WndMain", u"28", None));
        ___qtablewidgetitem38 = self.tbe_console.verticalHeaderItem(28)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("WndMain", u"29", None));
        ___qtablewidgetitem39 = self.tbe_console.verticalHeaderItem(29)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("WndMain", u"30", None));
        ___qtablewidgetitem40 = self.tbe_console.verticalHeaderItem(30)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("WndMain", u"31", None));
        ___qtablewidgetitem41 = self.tbe_console.verticalHeaderItem(31)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("WndMain", u"32", None));
        ___qtablewidgetitem42 = self.tbe_console.verticalHeaderItem(32)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("WndMain", u"33", None));
        ___qtablewidgetitem43 = self.tbe_console.verticalHeaderItem(33)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("WndMain", u"34", None));
        ___qtablewidgetitem44 = self.tbe_console.verticalHeaderItem(34)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("WndMain", u"35", None));
        ___qtablewidgetitem45 = self.tbe_console.verticalHeaderItem(35)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("WndMain", u"36", None));
        ___qtablewidgetitem46 = self.tbe_console.verticalHeaderItem(36)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("WndMain", u"37", None));
        ___qtablewidgetitem47 = self.tbe_console.verticalHeaderItem(37)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("WndMain", u"38", None));
        ___qtablewidgetitem48 = self.tbe_console.verticalHeaderItem(38)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("WndMain", u"39", None));
        ___qtablewidgetitem49 = self.tbe_console.verticalHeaderItem(39)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("WndMain", u"40", None));
        ___qtablewidgetitem50 = self.tbe_console.verticalHeaderItem(40)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("WndMain", u"41", None));
        ___qtablewidgetitem51 = self.tbe_console.verticalHeaderItem(41)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("WndMain", u"42", None));
        ___qtablewidgetitem52 = self.tbe_console.verticalHeaderItem(42)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("WndMain", u"43", None));
        ___qtablewidgetitem53 = self.tbe_console.verticalHeaderItem(43)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("WndMain", u"44", None));
        ___qtablewidgetitem54 = self.tbe_console.verticalHeaderItem(44)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("WndMain", u"45", None));
        ___qtablewidgetitem55 = self.tbe_console.verticalHeaderItem(45)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("WndMain", u"46", None));
        ___qtablewidgetitem56 = self.tbe_console.verticalHeaderItem(46)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("WndMain", u"47", None));
        ___qtablewidgetitem57 = self.tbe_console.verticalHeaderItem(47)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("WndMain", u"48", None));
        ___qtablewidgetitem58 = self.tbe_console.verticalHeaderItem(48)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("WndMain", u"49", None));
        ___qtablewidgetitem59 = self.tbe_console.verticalHeaderItem(49)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("WndMain", u"50", None));
        ___qtablewidgetitem60 = self.tbe_console.verticalHeaderItem(50)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("WndMain", u"51", None));
        ___qtablewidgetitem61 = self.tbe_console.verticalHeaderItem(51)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("WndMain", u"52", None));
        ___qtablewidgetitem62 = self.tbe_console.verticalHeaderItem(52)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("WndMain", u"53", None));
        ___qtablewidgetitem63 = self.tbe_console.verticalHeaderItem(53)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("WndMain", u"54", None));
        ___qtablewidgetitem64 = self.tbe_console.verticalHeaderItem(54)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("WndMain", u"55", None));
        ___qtablewidgetitem65 = self.tbe_console.verticalHeaderItem(55)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("WndMain", u"56", None));
        ___qtablewidgetitem66 = self.tbe_console.verticalHeaderItem(56)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("WndMain", u"57", None));
        ___qtablewidgetitem67 = self.tbe_console.verticalHeaderItem(57)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("WndMain", u"58", None));
        ___qtablewidgetitem68 = self.tbe_console.verticalHeaderItem(58)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("WndMain", u"59", None));
        ___qtablewidgetitem69 = self.tbe_console.verticalHeaderItem(59)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("WndMain", u"60", None));

        __sortingEnabled = self.tbe_console.isSortingEnabled()
        self.tbe_console.setSortingEnabled(False)
        self.tbe_console.setSortingEnabled(__sortingEnabled)

        self.groupBox_3.setTitle(QCoreApplication.translate("WndMain", u"\u57fa\u672c\u914d\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.edt_game_path.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u5165\u6e38\u620f\u5b89\u88c5\u76ee\u5f55\u4e0b\u7684update.exe", None))
#endif // QT_CONFIG(tooltip)
        self.edt_game_path.setPlaceholderText(QCoreApplication.translate("WndMain", u"C:/Program Files/LineKong/\u501a\u5929\u5251\u4e0e\u5c60\u9f99\u5200/update.exe", None))
        self.btn_open_folder_game_path.setText("")
        self.btn_open_game.setText(QCoreApplication.translate("WndMain", u"\u5f00", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("WndMain", u"\u83b7\u53d6\u7a97\u53e3\u540e", None))
        self.chk_arrange_get_wnd.setText(QCoreApplication.translate("WndMain", u"\u6392\u5217\u65b9\u5f0f", None))
        self.cmb_arrange_get_wnd.setItemText(0, QCoreApplication.translate("WndMain", u"0\u5782\u76f4\u7d27\u5bc6", None))
        self.cmb_arrange_get_wnd.setItemText(1, QCoreApplication.translate("WndMain", u"1\u5782\u76f4\u6269\u5c55", None))
        self.cmb_arrange_get_wnd.setItemText(2, QCoreApplication.translate("WndMain", u"2\u5e73\u94fa4K\u5c4f", None))
        self.cmb_arrange_get_wnd.setItemText(3, QCoreApplication.translate("WndMain", u"3\u5bf9\u89d2\u7d27\u5bc6", None))

        self.cmb_arrange_get_wnd.setCurrentText(QCoreApplication.translate("WndMain", u"0\u5782\u76f4\u7d27\u5bc6", None))
        self.chk_set_plan_get_wnd.setText(QCoreApplication.translate("WndMain", u"\u8bbe\u7f6e\u65b9\u6848", None))
        self.cmb_set_plan_get_wnd.setCurrentText("")
        self.chk_on_time.setTitle(QCoreApplication.translate("WndMain", u"\u5b9a\u65f6", None))
        self.chk_on_time_run_all.setText(QCoreApplication.translate("WndMain", u"\u8fd0\u884c\u5168\u90e8\u7a97\u53e3", None))
        self.tmedt_on_time_run_all.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.chk_on_time_shut_down.setText(QCoreApplication.translate("WndMain", u"\u5173\u95ed\u8ba1\u7b97\u673a", None))
        self.tmedt_on_time_shut_down.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u767b\u5f55", None))
        self.btn_start_auto_login.setText(QCoreApplication.translate("WndMain", u"\u5f00\u59cb\u767b\u5f55", None))
        self.btn_stop_auto_login.setText(QCoreApplication.translate("WndMain", u"\u505c\u6b62\u767b\u5f55", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u65b9\u6848\u5217 \u65b9\u6848\u5217\u4e00\u952e\u63a7\u4e94", None))
        self.label_55.setText(QCoreApplication.translate("WndMain", u"\u8bbe\u7f6e\u65b9\u6848", None))
        self.label_53.setText(QCoreApplication.translate("WndMain", u"\u65b9\u6848\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.lst_plan.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8bfb\u53d6\u6307\u5b9a\u65b9\u6848\u914d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.label_54.setText(QCoreApplication.translate("WndMain", u"\u65b0\u65b9\u6848\u540d\uff1a", None))
        self.btn_plan_create.setText(QCoreApplication.translate("WndMain", u"\u65b0 \u5efa", None))
        self.btn_plan_rename.setText(QCoreApplication.translate("WndMain", u"\u91cd\u547d\u540d", None))
        self.label_49.setText(QCoreApplication.translate("WndMain", u"\u529f\u80fd\u5217\u8868", None))
        ___qtreewidgetitem = self.tre_all.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("WndMain", u"\u6240\u6709\u529f\u80fd", None));

        __sortingEnabled1 = self.tre_all.isSortingEnabled()
        self.tre_all.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tre_all.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("WndMain", u"\u5355\u4eba\u4efb\u52a1", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("WndMain", u"\u6302\u673a\u5237\u91ce", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("WndMain", u"\u5185\u529f\u95ed\u5173", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("WndMain", u"\u7ecf\u8109\u8d2f\u901a", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("WndMain", u"\u5e08\u95e8\u4efb\u52a1", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("WndMain", u"\u56db\u8c61\u8dd1\u73af", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("WndMain", u"\u5e2e\u4f1a\u751f\u4ea7", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem1.child(6)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("WndMain", u"\u5e2e\u4f1a\u6750\u6599", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem1.child(7)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("WndMain", u"\u5e2e\u4f1a\u6316\u77ff", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem1.child(8)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("WndMain", u"\u5929\u547d\u5360\u5929", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem1.child(9)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("WndMain", u"\u6781\u9650\u6311\u6218", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem1.child(10)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("WndMain", u"\u5927\u5185\u9ad8\u624b", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem1.child(11)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("WndMain", u"\u5dc5\u5cf0\u4e4b\u5854", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem1.child(12)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("WndMain", u"\u8d77\u53f7\u4efb\u52a1", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem1.child(13)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("WndMain", u"\u4e2a\u4eba\u64c2\u53f0", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem1.child(14)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("WndMain", u"\u6311\u6218\u5802\u4e3b", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem1.child(15)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("WndMain", u"\u5c60\u9f99", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem1.child(16)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("WndMain", u"\u62bc\u9556", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem1.child(17)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("WndMain", u"\u4ea4\u8d27", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem1.child(18)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("WndMain", u"\u63a5\u8d27", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem1.child(19)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("WndMain", u"\u6316\u5b9d\u56fe", None));
        ___qtreewidgetitem22 = self.tre_all.topLevelItem(1)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("WndMain", u"\u56e2\u961f\u4efb\u52a1", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("WndMain", u"\u961f\u5458\u6302\u673a", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem22.child(1)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5237\u91ce", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem22.child(2)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6253\u725b", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem22.child(3)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6253\u864e", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem22.child(4)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6253\u9152", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem22.child(5)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5e73\u4e71", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem22.child(6)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5a01\u671b", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem22.child(7)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("WndMain", u"\u767e\u6218\u767e\u80dc", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem22.child(8)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("WndMain", u"\u56f4\u6355\u5927\u76d7", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem22.child(9)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("WndMain", u"\u8fb9\u5173\u6e05\u527f", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem22.child(10)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("WndMain", u"\u4eba\u7269\u526f\u672c", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem22.child(11)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("WndMain", u"\u968f\u4ece\u526f\u672c", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem22.child(12)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("WndMain", u"\u95ef\u5173", None));
        ___qtreewidgetitem36 = ___qtreewidgetitem22.child(13)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("WndMain", u"\u5bcc\u7532\u5929\u4e0b", None));
        ___qtreewidgetitem37 = ___qtreewidgetitem22.child(14)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("WndMain", u"\u56db\u5927\u540d\u6355", None));
        ___qtreewidgetitem38 = ___qtreewidgetitem22.child(15)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("WndMain", u"\u660e\u6559\u9ad8\u624b", None));
        ___qtreewidgetitem39 = ___qtreewidgetitem22.child(16)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("WndMain", u"\u4e94\u7edd", None));
        ___qtreewidgetitem40 = ___qtreewidgetitem22.child(17)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("WndMain", u"\u7d2b\u7981\u9ad8\u624b", None));
        ___qtreewidgetitem41 = ___qtreewidgetitem22.child(18)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("WndMain", u"\u73cd\u73d1\u68cb\u5c40", None));
        ___qtreewidgetitem42 = ___qtreewidgetitem22.child(19)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("WndMain", u"\u68a6\u5883\u5bfb\u5b9d", None));
        ___qtreewidgetitem43 = ___qtreewidgetitem22.child(20)
        ___qtreewidgetitem43.setText(0, QCoreApplication.translate("WndMain", u"\u6b66\u6597\u5927\u4f1a", None));
        ___qtreewidgetitem44 = ___qtreewidgetitem22.child(21)
        ___qtreewidgetitem44.setText(0, QCoreApplication.translate("WndMain", u"\u56e2\u4f53\u64c2\u53f0", None));
        ___qtreewidgetitem45 = ___qtreewidgetitem22.child(22)
        ___qtreewidgetitem45.setText(0, QCoreApplication.translate("WndMain", u"\u6316\u5b9d\u9a6c\u8d3c", None));
        ___qtreewidgetitem46 = self.tre_all.topLevelItem(2)
        ___qtreewidgetitem46.setText(0, QCoreApplication.translate("WndMain", u"\u5176\u5b83\u529f\u80fd", None));
        ___qtreewidgetitem47 = ___qtreewidgetitem46.child(0)
        ___qtreewidgetitem47.setText(0, QCoreApplication.translate("WndMain", u"\u6e05\u7406\u80cc\u5305", None));
        ___qtreewidgetitem48 = ___qtreewidgetitem46.child(1)
        ___qtreewidgetitem48.setText(0, QCoreApplication.translate("WndMain", u"\u8d2d\u4e70\u7269\u54c1", None));
        ___qtreewidgetitem49 = ___qtreewidgetitem46.child(2)
        ___qtreewidgetitem49.setText(0, QCoreApplication.translate("WndMain", u"\u4f7f\u7528\u7269\u54c1", None));
        ___qtreewidgetitem50 = ___qtreewidgetitem46.child(3)
        ___qtreewidgetitem50.setText(0, QCoreApplication.translate("WndMain", u"\u4ed3\u5e93\u53d6\u7269", None));
        ___qtreewidgetitem51 = ___qtreewidgetitem46.child(4)
        ___qtreewidgetitem51.setText(0, QCoreApplication.translate("WndMain", u"\u4fee\u7406\u5fe0\u8bda", None));
        ___qtreewidgetitem52 = ___qtreewidgetitem46.child(5)
        ___qtreewidgetitem52.setText(0, QCoreApplication.translate("WndMain", u"\u9886\u53d6\u53cc\u500d", None));
        ___qtreewidgetitem53 = ___qtreewidgetitem46.child(6)
        ___qtreewidgetitem53.setText(0, QCoreApplication.translate("WndMain", u"\u5e2e\u4f1a\u53cc\u500d", None));
        ___qtreewidgetitem54 = ___qtreewidgetitem46.child(7)
        ___qtreewidgetitem54.setText(0, QCoreApplication.translate("WndMain", u"\u51bb\u7ed3\u53cc\u500d", None));
        ___qtreewidgetitem55 = ___qtreewidgetitem46.child(8)
        ___qtreewidgetitem55.setText(0, QCoreApplication.translate("WndMain", u"\u89e3\u51bb\u53cc\u500d", None));
        ___qtreewidgetitem56 = ___qtreewidgetitem46.child(9)
        ___qtreewidgetitem56.setText(0, QCoreApplication.translate("WndMain", u"\u9f20\u6807\u8fde\u70b9", None));
        ___qtreewidgetitem57 = ___qtreewidgetitem46.child(10)
        ___qtreewidgetitem57.setText(0, QCoreApplication.translate("WndMain", u"\u9635\u6cd5\u5347\u7ea7", None));
        ___qtreewidgetitem58 = ___qtreewidgetitem46.child(11)
        ___qtreewidgetitem58.setText(0, QCoreApplication.translate("WndMain", u"\u968f\u4ece\u5347\u7ea7", None));
        ___qtreewidgetitem59 = ___qtreewidgetitem46.child(12)
        ___qtreewidgetitem59.setText(0, QCoreApplication.translate("WndMain", u"\u968f\u4ece\u6253\u4e66", None));
        ___qtreewidgetitem60 = ___qtreewidgetitem46.child(13)
        ___qtreewidgetitem60.setText(0, QCoreApplication.translate("WndMain", u"\u7cbe\u70bc\u968f\u4ece", None));
        ___qtreewidgetitem61 = ___qtreewidgetitem46.child(14)
        ___qtreewidgetitem61.setText(0, QCoreApplication.translate("WndMain", u"\u7f16\u9a6f\u9a6c\u7ef3", None));
        ___qtreewidgetitem62 = ___qtreewidgetitem46.child(15)
        ___qtreewidgetitem62.setText(0, QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u558a\u8bdd", None));
        ___qtreewidgetitem63 = ___qtreewidgetitem46.child(16)
        ___qtreewidgetitem63.setText(0, QCoreApplication.translate("WndMain", u"\u5f81\u6218\u6c5f\u6e56", None));
        ___qtreewidgetitem64 = ___qtreewidgetitem46.child(17)
        ___qtreewidgetitem64.setText(0, QCoreApplication.translate("WndMain", u"\u62e6\u622a\u5546\u65c5", None));
        ___qtreewidgetitem65 = ___qtreewidgetitem46.child(18)
        ___qtreewidgetitem65.setText(0, QCoreApplication.translate("WndMain", u"\u4e0a\u7f34\u57fa\u77f3", None));
        ___qtreewidgetitem66 = ___qtreewidgetitem46.child(19)
        ___qtreewidgetitem66.setText(0, QCoreApplication.translate("WndMain", u"\u9886\u53d6\u98de\u7fbd", None));
        ___qtreewidgetitem67 = ___qtreewidgetitem46.child(20)
        ___qtreewidgetitem67.setText(0, QCoreApplication.translate("WndMain", u"\u8282\u65e5\u793c\u54c1", None));
        ___qtreewidgetitem68 = ___qtreewidgetitem46.child(21)
        ___qtreewidgetitem68.setText(0, QCoreApplication.translate("WndMain", u"\u5927\u5185\u9886\u5956", None));
        ___qtreewidgetitem69 = ___qtreewidgetitem46.child(22)
        ___qtreewidgetitem69.setText(0, QCoreApplication.translate("WndMain", u"\u5b9a\u65f6\u542f\u52a8", None));
        ___qtreewidgetitem70 = ___qtreewidgetitem46.child(23)
        ___qtreewidgetitem70.setText(0, QCoreApplication.translate("WndMain", u"\u79bb\u5f00\u961f\u4f0d", None));
        ___qtreewidgetitem71 = ___qtreewidgetitem46.child(24)
        ___qtreewidgetitem71.setText(0, QCoreApplication.translate("WndMain", u"\u6362\u7ebf", None));
        ___qtreewidgetitem72 = ___qtreewidgetitem46.child(25)
        ___qtreewidgetitem72.setText(0, QCoreApplication.translate("WndMain", u"\u7ec4\u961f", None));
        self.tre_all.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.tre_all.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u5217\u8868\u9879\u53ef\u6dfb\u52a0\u5230\u6267\u884c\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("WndMain", u"\u6267\u884c\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.lst_exec.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u9009\u4e2d\u5217\u8868\u9879\u53ef\u4ece\u6267\u884c\u5217\u8868\u4e2d\u5220\u9664, \u6309\u4f4f\u5e76\u62d6\u52a8\u53ef\u8c03\u6574\u4efb\u52a1\u7684\u6267\u884c\u987a\u5e8f", None))
#endif // QT_CONFIG(tooltip)
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_basic), QCoreApplication.translate("WndMain", u"\u57fa\u672c\u914d\u7f6e", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_single), QCoreApplication.translate("WndMain", u"\u5355\u4eba\u914d\u7f6e", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_team), QCoreApplication.translate("WndMain", u"\u56e2\u961f\u914d\u7f6e", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_other), QCoreApplication.translate("WndMain", u"\u5176\u5b83\u914d\u7f6e", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("WndMain", u"toolBar", None))
    # retranslateUi

