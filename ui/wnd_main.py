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
        self.groupBox_people = QGroupBox(self.widget_config_basic)
        self.groupBox_people.setObjectName(u"groupBox_people")
        self.groupBox_people.setGeometry(QRect(93, 1, 130, 551))
        self.groupBox_people.setMinimumSize(QSize(0, 0))
        self.groupBox_people.setMaximumSize(QSize(130, 16777215))
        self.groupBox_people.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox_people.setFlat(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_people)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.widget_people_fight = QWidget(self.groupBox_people)
        self.widget_people_fight.setObjectName(u"widget_people_fight")
        self.widget_people_fight.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_78 = QHBoxLayout(self.widget_people_fight)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.radio_fight_people_attack = QRadioButton(self.widget_people_fight)
        self.radio_fight_people_attack.setObjectName(u"radio_fight_people_attack")
        self.radio_fight_people_attack.setMaximumSize(QSize(16777215, 34))
        self.radio_fight_people_attack.setChecked(True)

        self.horizontalLayout_78.addWidget(self.radio_fight_people_attack)

        self.radio_fight_people_defend = QRadioButton(self.widget_people_fight)
        self.radio_fight_people_defend.setObjectName(u"radio_fight_people_defend")
        self.radio_fight_people_defend.setMaximumSize(QSize(16777215, 34))

        self.horizontalLayout_78.addWidget(self.radio_fight_people_defend)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_9)


        self.verticalLayout_5.addWidget(self.widget_people_fight)

        self.chk_fight_save_enemy_less = QGroupBox(self.groupBox_people)
        self.chk_fight_save_enemy_less.setObjectName(u"chk_fight_save_enemy_less")
        self.chk_fight_save_enemy_less.setMaximumSize(QSize(16777215, 52))
        self.chk_fight_save_enemy_less.setCheckable(True)
        self.chk_fight_save_enemy_less.setChecked(False)
        self.horizontalLayout_79 = QHBoxLayout(self.chk_fight_save_enemy_less)
        self.horizontalLayout_79.setSpacing(3)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(6, 3, 6, 3)
        self.label_88 = QLabel(self.chk_fight_save_enemy_less)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMaximumSize(QSize(74, 16777215))

        self.horizontalLayout_79.addWidget(self.label_88)

        self.spin_count_fight_save_enemy_less = QSpinBox(self.chk_fight_save_enemy_less)
        self.spin_count_fight_save_enemy_less.setObjectName(u"spin_count_fight_save_enemy_less")
        self.spin_count_fight_save_enemy_less.setMaximumSize(QSize(31, 16777215))
        self.spin_count_fight_save_enemy_less.setMinimum(1)
        self.spin_count_fight_save_enemy_less.setMaximum(10)
        self.spin_count_fight_save_enemy_less.setValue(3)

        self.horizontalLayout_79.addWidget(self.spin_count_fight_save_enemy_less)


        self.verticalLayout_5.addWidget(self.chk_fight_save_enemy_less)

        self.groupBox_people_save_people = QGroupBox(self.groupBox_people)
        self.groupBox_people_save_people.setObjectName(u"groupBox_people_save_people")
        self.groupBox_people_save_people.setMaximumSize(QSize(116, 54))
        self.groupBox_people_save_people.setCheckable(True)
        self.gridLayout_39 = QGridLayout(self.groupBox_people_save_people)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(6, 3, 6, 3)
        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setSpacing(4)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_89 = QLabel(self.groupBox_people_save_people)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_80.addWidget(self.label_89)

        self.spin_count_people_save_people = QSpinBox(self.groupBox_people_save_people)
        self.spin_count_people_save_people.setObjectName(u"spin_count_people_save_people")
        self.spin_count_people_save_people.setMinimumSize(QSize(38, 0))
        self.spin_count_people_save_people.setValue(10)

        self.horizontalLayout_80.addWidget(self.spin_count_people_save_people)

        self.label_90 = QLabel(self.groupBox_people_save_people)
        self.label_90.setObjectName(u"label_90")

        self.horizontalLayout_80.addWidget(self.label_90)


        self.gridLayout_39.addLayout(self.horizontalLayout_80, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_people_save_people)

        self.groupBox_people_save_bb = QGroupBox(self.groupBox_people)
        self.groupBox_people_save_bb.setObjectName(u"groupBox_people_save_bb")
        self.groupBox_people_save_bb.setMaximumSize(QSize(116, 54))
        self.groupBox_people_save_bb.setCheckable(True)
        self.groupBox_people_save_bb.setChecked(False)
        self.gridLayout_40 = QGridLayout(self.groupBox_people_save_bb)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(6, 3, 6, 3)
        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setSpacing(4)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_91 = QLabel(self.groupBox_people_save_bb)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_81.addWidget(self.label_91)

        self.spin_count_people_save_bb = QSpinBox(self.groupBox_people_save_bb)
        self.spin_count_people_save_bb.setObjectName(u"spin_count_people_save_bb")
        self.spin_count_people_save_bb.setMinimumSize(QSize(38, 0))
        self.spin_count_people_save_bb.setValue(50)

        self.horizontalLayout_81.addWidget(self.spin_count_people_save_bb)

        self.label_92 = QLabel(self.groupBox_people_save_bb)
        self.label_92.setObjectName(u"label_92")

        self.horizontalLayout_81.addWidget(self.label_92)


        self.gridLayout_40.addLayout(self.horizontalLayout_81, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_people_save_bb)

        self.groupBox_people_use_skill = QGroupBox(self.groupBox_people)
        self.groupBox_people_use_skill.setObjectName(u"groupBox_people_use_skill")
        self.groupBox_people_use_skill.setMinimumSize(QSize(0, 168))
        self.groupBox_people_use_skill.setMaximumSize(QSize(116, 16777215))
        self.groupBox_people_use_skill.setCheckable(True)
        self.groupBox_people_use_skill.setChecked(False)
        self.verticalLayout_46 = QVBoxLayout(self.groupBox_people_use_skill)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(6, 6, 3, 6)
        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setSpacing(1)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.chk_people_skill_cixue = QCheckBox(self.groupBox_people_use_skill)
        self.chk_people_skill_cixue.setObjectName(u"chk_people_skill_cixue")
        self.chk_people_skill_cixue.setMinimumSize(QSize(62, 0))
        self.chk_people_skill_cixue.setChecked(True)

        self.horizontalLayout_82.addWidget(self.chk_people_skill_cixue)

        self.spin_count_skill_frequency = QSpinBox(self.groupBox_people_use_skill)
        self.spin_count_skill_frequency.setObjectName(u"spin_count_skill_frequency")
        self.spin_count_skill_frequency.setMinimumSize(QSize(35, 0))
        self.spin_count_skill_frequency.setMaximumSize(QSize(35, 16777215))
        self.spin_count_skill_frequency.setValue(15)

        self.horizontalLayout_82.addWidget(self.spin_count_skill_frequency)


        self.verticalLayout_46.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setSpacing(1)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.chk_people_skill_huxin = QCheckBox(self.groupBox_people_use_skill)
        self.chk_people_skill_huxin.setObjectName(u"chk_people_skill_huxin")
        self.chk_people_skill_huxin.setMinimumSize(QSize(62, 0))
        self.chk_people_skill_huxin.setChecked(True)

        self.horizontalLayout_83.addWidget(self.chk_people_skill_huxin)

        self.spin_count_huxin_percent = QSpinBox(self.groupBox_people_use_skill)
        self.spin_count_huxin_percent.setObjectName(u"spin_count_huxin_percent")
        self.spin_count_huxin_percent.setMinimumSize(QSize(35, 0))
        self.spin_count_huxin_percent.setMaximumSize(QSize(35, 16777215))
        self.spin_count_huxin_percent.setValue(60)

        self.horizontalLayout_83.addWidget(self.spin_count_huxin_percent)


        self.verticalLayout_46.addLayout(self.horizontalLayout_83)

        self.chk_people_skill_single = QCheckBox(self.groupBox_people_use_skill)
        self.chk_people_skill_single.setObjectName(u"chk_people_skill_single")
        self.chk_people_skill_single.setChecked(True)

        self.verticalLayout_46.addWidget(self.chk_people_skill_single)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setSpacing(3)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.chk_people_skill_continue_cixue = QCheckBox(self.groupBox_people_use_skill)
        self.chk_people_skill_continue_cixue.setObjectName(u"chk_people_skill_continue_cixue")

        self.verticalLayout_47.addWidget(self.chk_people_skill_continue_cixue)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setSpacing(1)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.label_93 = QLabel(self.groupBox_people_use_skill)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMaximumSize(QSize(12, 16777215))

        self.horizontalLayout_84.addWidget(self.label_93)

        self.spin_count_people_skill_continue_cixue = QSpinBox(self.groupBox_people_use_skill)
        self.spin_count_people_skill_continue_cixue.setObjectName(u"spin_count_people_skill_continue_cixue")
        self.spin_count_people_skill_continue_cixue.setMinimumSize(QSize(34, 22))
        self.spin_count_people_skill_continue_cixue.setMaximumSize(QSize(34, 16777215))
        self.spin_count_people_skill_continue_cixue.setValue(50)

        self.horizontalLayout_84.addWidget(self.spin_count_people_skill_continue_cixue)

        self.label_94 = QLabel(self.groupBox_people_use_skill)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_84.addWidget(self.label_94)


        self.verticalLayout_47.addLayout(self.horizontalLayout_84)


        self.verticalLayout_46.addLayout(self.verticalLayout_47)


        self.verticalLayout_5.addWidget(self.groupBox_people_use_skill)

        self.groupBox_call_bb = QGroupBox(self.groupBox_people)
        self.groupBox_call_bb.setObjectName(u"groupBox_call_bb")
        self.groupBox_call_bb.setMinimumSize(QSize(0, 0))
        self.groupBox_call_bb.setMaximumSize(QSize(116, 134))
        self.groupBox_call_bb.setCheckable(True)
        self.groupBox_call_bb.setChecked(False)
        self.verticalLayout_48 = QVBoxLayout(self.groupBox_call_bb)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_95 = QLabel(self.groupBox_call_bb)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(34, 0))

        self.horizontalLayout_85.addWidget(self.label_95)

        self.spin_count_call_bb_blood = QSpinBox(self.groupBox_call_bb)
        self.spin_count_call_bb_blood.setObjectName(u"spin_count_call_bb_blood")
        self.spin_count_call_bb_blood.setMinimumSize(QSize(38, 0))
        self.spin_count_call_bb_blood.setValue(50)

        self.horizontalLayout_85.addWidget(self.spin_count_call_bb_blood)

        self.label_96 = QLabel(self.groupBox_call_bb)
        self.label_96.setObjectName(u"label_96")

        self.horizontalLayout_85.addWidget(self.label_96)


        self.verticalLayout_48.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_97 = QLabel(self.groupBox_call_bb)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(34, 0))

        self.horizontalLayout_86.addWidget(self.label_97)

        self.spin_count_call_bb_round = QSpinBox(self.groupBox_call_bb)
        self.spin_count_call_bb_round.setObjectName(u"spin_count_call_bb_round")
        self.spin_count_call_bb_round.setMinimumSize(QSize(38, 0))
        self.spin_count_call_bb_round.setValue(20)

        self.horizontalLayout_86.addWidget(self.spin_count_call_bb_round)


        self.verticalLayout_48.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_98 = QLabel(self.groupBox_call_bb)
        self.label_98.setObjectName(u"label_98")

        self.horizontalLayout_87.addWidget(self.label_98)

        self.edt_call_bb_name = QLineEdit(self.groupBox_call_bb)
        self.edt_call_bb_name.setObjectName(u"edt_call_bb_name")
        self.edt_call_bb_name.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_87.addWidget(self.edt_call_bb_name)


        self.verticalLayout_48.addLayout(self.horizontalLayout_87)


        self.verticalLayout_5.addWidget(self.groupBox_call_bb)

        self.groupBox_bb = QGroupBox(self.widget_config_basic)
        self.groupBox_bb.setObjectName(u"groupBox_bb")
        self.groupBox_bb.setGeometry(QRect(230, 1, 221, 321))
        self.groupBox_bb.setMinimumSize(QSize(210, 0))
        self.groupBox_bb.setMaximumSize(QSize(230, 16777215))
        self.groupBox_bb.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox_bb.setFlat(False)
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_bb)
        self.verticalLayout_36.setSpacing(3)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(3, 3, 3, 3)
        self.groupBox_bb_fight_defend = QGroupBox(self.groupBox_bb)
        self.groupBox_bb_fight_defend.setObjectName(u"groupBox_bb_fight_defend")
        self.groupBox_bb_fight_defend.setMaximumSize(QSize(16777215, 48))
        self.verticalLayout_37 = QVBoxLayout(self.groupBox_bb_fight_defend)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(3, 3, 3, 3)
        self.widget_bb_fight = QWidget(self.groupBox_bb_fight_defend)
        self.widget_bb_fight.setObjectName(u"widget_bb_fight")
        self.widget_bb_fight.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_bb_fight)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.radioButton_14 = QRadioButton(self.widget_bb_fight)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.horizontalLayout_28.addWidget(self.radioButton_14)

        self.radioButton_15 = QRadioButton(self.widget_bb_fight)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.horizontalLayout_28.addWidget(self.radioButton_15)

        self.radioButton_16 = QRadioButton(self.widget_bb_fight)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setChecked(True)

        self.horizontalLayout_28.addWidget(self.radioButton_16)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_8)


        self.verticalLayout_37.addWidget(self.widget_bb_fight)


        self.verticalLayout_36.addWidget(self.groupBox_bb_fight_defend)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.groupBox_fight_bb = QGroupBox(self.groupBox_bb)
        self.groupBox_fight_bb.setObjectName(u"groupBox_fight_bb")
        self.groupBox_fight_bb.setMinimumSize(QSize(0, 126))
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_fight_bb)
        self.verticalLayout_38.setSpacing(6)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(3, 3, 3, 3)
        self.groupBox_fight_bb_save_people = QGroupBox(self.groupBox_fight_bb)
        self.groupBox_fight_bb_save_people.setObjectName(u"groupBox_fight_bb_save_people")
        self.groupBox_fight_bb_save_people.setCheckable(True)
        self.groupBox_fight_bb_save_people.setChecked(False)
        self.gridLayout_29 = QGridLayout(self.groupBox_fight_bb_save_people)
        self.gridLayout_29.setSpacing(3)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setSpacing(4)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_67 = QLabel(self.groupBox_fight_bb_save_people)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_63.addWidget(self.label_67)

        self.spin_count_fight_bb_save_people = QSpinBox(self.groupBox_fight_bb_save_people)
        self.spin_count_fight_bb_save_people.setObjectName(u"spin_count_fight_bb_save_people")
        self.spin_count_fight_bb_save_people.setMinimumSize(QSize(35, 0))
        self.spin_count_fight_bb_save_people.setMaximumSize(QSize(35, 16777215))
        self.spin_count_fight_bb_save_people.setMinimum(1)
        self.spin_count_fight_bb_save_people.setValue(10)

        self.horizontalLayout_63.addWidget(self.spin_count_fight_bb_save_people)

        self.label_68 = QLabel(self.groupBox_fight_bb_save_people)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_63.addWidget(self.label_68)


        self.gridLayout_29.addLayout(self.horizontalLayout_63, 0, 0, 1, 1)


        self.verticalLayout_38.addWidget(self.groupBox_fight_bb_save_people)

        self.groupBox_fight_bb_save_bb = QGroupBox(self.groupBox_fight_bb)
        self.groupBox_fight_bb_save_bb.setObjectName(u"groupBox_fight_bb_save_bb")
        self.groupBox_fight_bb_save_bb.setCheckable(True)
        self.groupBox_fight_bb_save_bb.setChecked(False)
        self.gridLayout_35 = QGridLayout(self.groupBox_fight_bb_save_bb)
        self.gridLayout_35.setSpacing(3)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setSpacing(4)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_69 = QLabel(self.groupBox_fight_bb_save_bb)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_71.addWidget(self.label_69)

        self.spin_count_fight_bb_save_bb = QSpinBox(self.groupBox_fight_bb_save_bb)
        self.spin_count_fight_bb_save_bb.setObjectName(u"spin_count_fight_bb_save_bb")
        self.spin_count_fight_bb_save_bb.setMinimumSize(QSize(35, 0))
        self.spin_count_fight_bb_save_bb.setMaximumSize(QSize(35, 16777215))
        self.spin_count_fight_bb_save_bb.setMinimum(1)
        self.spin_count_fight_bb_save_bb.setValue(10)

        self.horizontalLayout_71.addWidget(self.spin_count_fight_bb_save_bb)

        self.label_70 = QLabel(self.groupBox_fight_bb_save_bb)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_71.addWidget(self.label_70)


        self.gridLayout_35.addLayout(self.horizontalLayout_71, 0, 0, 1, 1)


        self.verticalLayout_38.addWidget(self.groupBox_fight_bb_save_bb)


        self.horizontalLayout_61.addWidget(self.groupBox_fight_bb)

        self.groupBox_defend_bb = QGroupBox(self.groupBox_bb)
        self.groupBox_defend_bb.setObjectName(u"groupBox_defend_bb")
        self.groupBox_defend_bb.setMinimumSize(QSize(0, 126))
        self.verticalLayout_39 = QVBoxLayout(self.groupBox_defend_bb)
        self.verticalLayout_39.setSpacing(6)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(3, 3, 3, 3)
        self.groupBox_defend_bb_save_people = QGroupBox(self.groupBox_defend_bb)
        self.groupBox_defend_bb_save_people.setObjectName(u"groupBox_defend_bb_save_people")
        self.groupBox_defend_bb_save_people.setCheckable(True)
        self.gridLayout_36 = QGridLayout(self.groupBox_defend_bb_save_people)
        self.gridLayout_36.setSpacing(3)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setSpacing(4)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_82 = QLabel(self.groupBox_defend_bb_save_people)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_72.addWidget(self.label_82)

        self.spin_count_defend_bb_save_people = QSpinBox(self.groupBox_defend_bb_save_people)
        self.spin_count_defend_bb_save_people.setObjectName(u"spin_count_defend_bb_save_people")
        self.spin_count_defend_bb_save_people.setMinimumSize(QSize(35, 0))
        self.spin_count_defend_bb_save_people.setMaximumSize(QSize(35, 16777215))
        self.spin_count_defend_bb_save_people.setMinimum(1)
        self.spin_count_defend_bb_save_people.setValue(10)

        self.horizontalLayout_72.addWidget(self.spin_count_defend_bb_save_people)

        self.label_83 = QLabel(self.groupBox_defend_bb_save_people)
        self.label_83.setObjectName(u"label_83")

        self.horizontalLayout_72.addWidget(self.label_83)


        self.gridLayout_36.addLayout(self.horizontalLayout_72, 0, 0, 1, 1)


        self.verticalLayout_39.addWidget(self.groupBox_defend_bb_save_people)

        self.groupBox_defend_bb_save_bb = QGroupBox(self.groupBox_defend_bb)
        self.groupBox_defend_bb_save_bb.setObjectName(u"groupBox_defend_bb_save_bb")
        self.groupBox_defend_bb_save_bb.setCheckable(True)
        self.groupBox_defend_bb_save_bb.setChecked(False)
        self.gridLayout_37 = QGridLayout(self.groupBox_defend_bb_save_bb)
        self.gridLayout_37.setSpacing(3)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setSpacing(4)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_84 = QLabel(self.groupBox_defend_bb_save_bb)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_73.addWidget(self.label_84)

        self.spin_count_defend_bb_save_bb = QSpinBox(self.groupBox_defend_bb_save_bb)
        self.spin_count_defend_bb_save_bb.setObjectName(u"spin_count_defend_bb_save_bb")
        self.spin_count_defend_bb_save_bb.setMinimumSize(QSize(35, 0))
        self.spin_count_defend_bb_save_bb.setMaximumSize(QSize(35, 16777215))
        self.spin_count_defend_bb_save_bb.setMinimum(1)
        self.spin_count_defend_bb_save_bb.setValue(10)

        self.horizontalLayout_73.addWidget(self.spin_count_defend_bb_save_bb)

        self.label_85 = QLabel(self.groupBox_defend_bb_save_bb)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_73.addWidget(self.label_85)


        self.gridLayout_37.addLayout(self.horizontalLayout_73, 0, 0, 1, 1)


        self.verticalLayout_39.addWidget(self.groupBox_defend_bb_save_bb)


        self.horizontalLayout_61.addWidget(self.groupBox_defend_bb)


        self.verticalLayout_36.addLayout(self.horizontalLayout_61)

        self.groupBox_bb_use_skill = QGroupBox(self.groupBox_bb)
        self.groupBox_bb_use_skill.setObjectName(u"groupBox_bb_use_skill")
        self.groupBox_bb_use_skill.setMinimumSize(QSize(0, 70))
        self.groupBox_bb_use_skill.setCheckable(True)
        self.verticalLayout_40 = QVBoxLayout(self.groupBox_bb_use_skill)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setSpacing(3)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.chk_fight_bb_jzz = QCheckBox(self.groupBox_bb_use_skill)
        self.chk_fight_bb_jzz.setObjectName(u"chk_fight_bb_jzz")

        self.horizontalLayout_74.addWidget(self.chk_fight_bb_jzz)

        self.chk_fight_bb_tbs = QCheckBox(self.groupBox_bb_use_skill)
        self.chk_fight_bb_tbs.setObjectName(u"chk_fight_bb_tbs")
        self.chk_fight_bb_tbs.setChecked(False)

        self.horizontalLayout_74.addWidget(self.chk_fight_bb_tbs)

        self.chk_fight_bb_lsgs = QCheckBox(self.groupBox_bb_use_skill)
        self.chk_fight_bb_lsgs.setObjectName(u"chk_fight_bb_lsgs")
        self.chk_fight_bb_lsgs.setChecked(False)

        self.horizontalLayout_74.addWidget(self.chk_fight_bb_lsgs)


        self.verticalLayout_40.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setSpacing(3)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.chk_fight_bb_hj = QCheckBox(self.groupBox_bb_use_skill)
        self.chk_fight_bb_hj.setObjectName(u"chk_fight_bb_hj")
        self.chk_fight_bb_hj.setChecked(True)

        self.horizontalLayout_75.addWidget(self.chk_fight_bb_hj)

        self.chk_fight_bb_jj = QCheckBox(self.groupBox_bb_use_skill)
        self.chk_fight_bb_jj.setObjectName(u"chk_fight_bb_jj")
        self.chk_fight_bb_jj.setChecked(True)

        self.horizontalLayout_75.addWidget(self.chk_fight_bb_jj)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setSpacing(1)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.chk_fight_bb_pf = QCheckBox(self.groupBox_bb_use_skill)
        self.chk_fight_bb_pf.setObjectName(u"chk_fight_bb_pf")
        self.chk_fight_bb_pf.setChecked(True)

        self.horizontalLayout_76.addWidget(self.chk_fight_bb_pf)

        self.spin_count_fight_bb_pf_round = QSpinBox(self.groupBox_bb_use_skill)
        self.spin_count_fight_bb_pf_round.setObjectName(u"spin_count_fight_bb_pf_round")
        self.spin_count_fight_bb_pf_round.setMinimumSize(QSize(34, 0))
        self.spin_count_fight_bb_pf_round.setValue(20)

        self.horizontalLayout_76.addWidget(self.spin_count_fight_bb_pf_round)


        self.horizontalLayout_75.addLayout(self.horizontalLayout_76)


        self.verticalLayout_40.addLayout(self.horizontalLayout_75)


        self.verticalLayout_36.addWidget(self.groupBox_bb_use_skill)

        self.layoutWidget = QWidget(self.widget_config_basic)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 87, 321))
        self.verticalLayout_41 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.groupBox_back = QGroupBox(self.layoutWidget)
        self.groupBox_back.setObjectName(u"groupBox_back")
        self.groupBox_back.setMinimumSize(QSize(0, 142))
        self.groupBox_back.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_42 = QVBoxLayout(self.groupBox_back)
        self.verticalLayout_42.setSpacing(3)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(3, 3, 3, 3)
        self.radio_back_dunjia_super = QRadioButton(self.groupBox_back)
        self.radio_back_dunjia_super.setObjectName(u"radio_back_dunjia_super")

        self.verticalLayout_42.addWidget(self.radio_back_dunjia_super)

        self.radio_back_dunjia_small = QRadioButton(self.groupBox_back)
        self.radio_back_dunjia_small.setObjectName(u"radio_back_dunjia_small")

        self.verticalLayout_42.addWidget(self.radio_back_dunjia_small)

        self.radio_back_kaifeng = QRadioButton(self.groupBox_back)
        self.radio_back_kaifeng.setObjectName(u"radio_back_kaifeng")
        self.radio_back_kaifeng.setChecked(True)

        self.verticalLayout_42.addWidget(self.radio_back_kaifeng)

        self.radio_back_menpai = QRadioButton(self.groupBox_back)
        self.radio_back_menpai.setObjectName(u"radio_back_menpai")
        self.radio_back_menpai.setChecked(False)

        self.verticalLayout_42.addWidget(self.radio_back_menpai)

        self.radio_back_run = QRadioButton(self.groupBox_back)
        self.radio_back_run.setObjectName(u"radio_back_run")

        self.verticalLayout_42.addWidget(self.radio_back_run)


        self.verticalLayout_41.addWidget(self.groupBox_back)

        self.groupBox_go = QGroupBox(self.layoutWidget)
        self.groupBox_go.setObjectName(u"groupBox_go")
        self.groupBox_go.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_43 = QVBoxLayout(self.groupBox_go)
        self.verticalLayout_43.setSpacing(3)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(3, 3, 3, 3)
        self.radio_go_dunjia_super = QRadioButton(self.groupBox_go)
        self.radio_go_dunjia_super.setObjectName(u"radio_go_dunjia_super")

        self.verticalLayout_43.addWidget(self.radio_go_dunjia_super)

        self.radio_go_run = QRadioButton(self.groupBox_go)
        self.radio_go_run.setObjectName(u"radio_go_run")
        self.radio_go_run.setChecked(True)

        self.verticalLayout_43.addWidget(self.radio_go_run)


        self.verticalLayout_41.addWidget(self.groupBox_go)

        self.groupBox_34 = QGroupBox(self.layoutWidget)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.gridLayout_38 = QGridLayout(self.groupBox_34)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(3, 2, 3, 2)
        self.cmb_people_bb_use_skill = QComboBox(self.groupBox_34)
        self.cmb_people_bb_use_skill.addItem("")
        self.cmb_people_bb_use_skill.addItem("")
        self.cmb_people_bb_use_skill.setObjectName(u"cmb_people_bb_use_skill")

        self.gridLayout_38.addWidget(self.cmb_people_bb_use_skill, 0, 0, 1, 1)


        self.verticalLayout_41.addWidget(self.groupBox_34)

        self.groupBox_35 = QGroupBox(self.widget_config_basic)
        self.groupBox_35.setObjectName(u"groupBox_35")
        self.groupBox_35.setGeometry(QRect(231, 324, 159, 86))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_35)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.chk_people_switch_primary_bb = QCheckBox(self.groupBox_35)
        self.chk_people_switch_primary_bb.setObjectName(u"chk_people_switch_primary_bb")
        self.chk_people_switch_primary_bb.setChecked(False)

        self.verticalLayout_9.addWidget(self.chk_people_switch_primary_bb)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.chk_after_fight_people_supply = QCheckBox(self.groupBox_35)
        self.chk_after_fight_people_supply.setObjectName(u"chk_after_fight_people_supply")

        self.horizontalLayout_23.addWidget(self.chk_after_fight_people_supply)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setSpacing(6)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.spin_count_after_fight_people_supply = QSpinBox(self.groupBox_35)
        self.spin_count_after_fight_people_supply.setObjectName(u"spin_count_after_fight_people_supply")
        self.spin_count_after_fight_people_supply.setMinimumSize(QSize(38, 0))
        self.spin_count_after_fight_people_supply.setValue(80)

        self.horizontalLayout_77.addWidget(self.spin_count_after_fight_people_supply)

        self.label_87 = QLabel(self.groupBox_35)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_77.addWidget(self.label_87)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_77)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)


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
        self.groupBox_ji_xian = QGroupBox(self.widget_config_single)
        self.groupBox_ji_xian.setObjectName(u"groupBox_ji_xian")
        self.groupBox_ji_xian.setGeometry(QRect(98, 251, 101, 121))
        self.groupBox_ji_xian.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_ji_xian)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_19 = QLabel(self.groupBox_ji_xian)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_26.addWidget(self.label_19)

        self.spin_count_ji_xian = QSpinBox(self.groupBox_ji_xian)
        self.spin_count_ji_xian.setObjectName(u"spin_count_ji_xian")
        self.spin_count_ji_xian.setMinimumSize(QSize(60, 0))
        self.spin_count_ji_xian.setMaximum(450)
        self.spin_count_ji_xian.setSingleStep(1)
        self.spin_count_ji_xian.setValue(300)

        self.horizontalLayout_26.addWidget(self.spin_count_ji_xian)


        self.verticalLayout_6.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.radioButton = QRadioButton(self.groupBox_ji_xian)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_27.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_ji_xian)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.horizontalLayout_27.addWidget(self.radioButton_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_27)

        self.chk_ji_xian_fail_stop = QCheckBox(self.groupBox_ji_xian)
        self.chk_ji_xian_fail_stop.setObjectName(u"chk_ji_xian_fail_stop")

        self.verticalLayout_6.addWidget(self.chk_ji_xian_fail_stop)

        self.groupBox_25 = QGroupBox(self.widget_config_single)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setGeometry(QRect(206, 251, 101, 141))
        self.groupBox_25.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_25)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.chk_shi_men_forever = QCheckBox(self.groupBox_25)
        self.chk_shi_men_forever.setObjectName(u"chk_shi_men_forever")

        self.verticalLayout_11.addWidget(self.chk_shi_men_forever)

        self.groupBox_shi_men_task_thing = QGroupBox(self.groupBox_25)
        self.groupBox_shi_men_task_thing.setObjectName(u"groupBox_shi_men_task_thing")
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_shi_men_task_thing)
        self.verticalLayout_30.setSpacing(3)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(6, 6, 6, 6)
        self.radioButton_12 = QRadioButton(self.groupBox_shi_men_task_thing)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setChecked(True)

        self.verticalLayout_30.addWidget(self.radioButton_12)

        self.radioButton_13 = QRadioButton(self.groupBox_shi_men_task_thing)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.verticalLayout_30.addWidget(self.radioButton_13)


        self.verticalLayout_11.addWidget(self.groupBox_shi_men_task_thing)

        self.groupBox_27 = QGroupBox(self.widget_config_single)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setGeometry(QRect(450, 4, 178, 281))
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_27)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_61 = QLabel(self.groupBox_27)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_41.addWidget(self.label_61)

        self.cmb_deliver_pos = QComboBox(self.groupBox_27)
        self.cmb_deliver_pos.addItem("")
        self.cmb_deliver_pos.addItem("")
        self.cmb_deliver_pos.addItem("")
        self.cmb_deliver_pos.addItem("")
        self.cmb_deliver_pos.setObjectName(u"cmb_deliver_pos")

        self.horizontalLayout_41.addWidget(self.cmb_deliver_pos)


        self.verticalLayout_22.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setSpacing(3)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.chk_deliver_banghui = QCheckBox(self.groupBox_27)
        self.chk_deliver_banghui.setObjectName(u"chk_deliver_banghui")

        self.horizontalLayout_42.addWidget(self.chk_deliver_banghui)

        self.edt_deliver_banghui = QLineEdit(self.groupBox_27)
        self.edt_deliver_banghui.setObjectName(u"edt_deliver_banghui")

        self.horizontalLayout_42.addWidget(self.edt_deliver_banghui)


        self.verticalLayout_22.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setSpacing(3)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.chk_deliver_yao_cai = QCheckBox(self.groupBox_27)
        self.chk_deliver_yao_cai.setObjectName(u"chk_deliver_yao_cai")

        self.horizontalLayout_43.addWidget(self.chk_deliver_yao_cai)

        self.edt_deliver_yao_cai = QLineEdit(self.groupBox_27)
        self.edt_deliver_yao_cai.setObjectName(u"edt_deliver_yao_cai")

        self.horizontalLayout_43.addWidget(self.edt_deliver_yao_cai)


        self.verticalLayout_22.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(3)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.chk_deliver_zhu_fu_cai = QCheckBox(self.groupBox_27)
        self.chk_deliver_zhu_fu_cai.setObjectName(u"chk_deliver_zhu_fu_cai")

        self.horizontalLayout_44.addWidget(self.chk_deliver_zhu_fu_cai)

        self.edt_deliver_zhu_fu_cai = QLineEdit(self.groupBox_27)
        self.edt_deliver_zhu_fu_cai.setObjectName(u"edt_deliver_zhu_fu_cai")

        self.horizontalLayout_44.addWidget(self.edt_deliver_zhu_fu_cai)


        self.verticalLayout_22.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(3)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.chk_deliver_za_huo = QCheckBox(self.groupBox_27)
        self.chk_deliver_za_huo.setObjectName(u"chk_deliver_za_huo")

        self.horizontalLayout_49.addWidget(self.chk_deliver_za_huo)

        self.edt_deliver_za_huo = QLineEdit(self.groupBox_27)
        self.edt_deliver_za_huo.setObjectName(u"edt_deliver_za_huo")

        self.horizontalLayout_49.addWidget(self.edt_deliver_za_huo)


        self.verticalLayout_22.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setSpacing(3)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.chk_deliver_bb_skill_book = QCheckBox(self.groupBox_27)
        self.chk_deliver_bb_skill_book.setObjectName(u"chk_deliver_bb_skill_book")

        self.horizontalLayout_45.addWidget(self.chk_deliver_bb_skill_book)

        self.edt_deliver_bb_skill_book = QLineEdit(self.groupBox_27)
        self.edt_deliver_bb_skill_book.setObjectName(u"edt_deliver_bb_skill_book")

        self.horizontalLayout_45.addWidget(self.edt_deliver_bb_skill_book)


        self.verticalLayout_22.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(3)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.chk_deliver_ling_shi = QCheckBox(self.groupBox_27)
        self.chk_deliver_ling_shi.setObjectName(u"chk_deliver_ling_shi")

        self.horizontalLayout_47.addWidget(self.chk_deliver_ling_shi)

        self.edt_deliver_ling_shi = QLineEdit(self.groupBox_27)
        self.edt_deliver_ling_shi.setObjectName(u"edt_deliver_ling_shi")

        self.horizontalLayout_47.addWidget(self.edt_deliver_ling_shi)


        self.verticalLayout_22.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setSpacing(3)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.chk_deliver_fu_ben = QCheckBox(self.groupBox_27)
        self.chk_deliver_fu_ben.setObjectName(u"chk_deliver_fu_ben")

        self.horizontalLayout_48.addWidget(self.chk_deliver_fu_ben)

        self.edt_deliver_fu_ben = QLineEdit(self.groupBox_27)
        self.edt_deliver_fu_ben.setObjectName(u"edt_deliver_fu_ben")

        self.horizontalLayout_48.addWidget(self.edt_deliver_fu_ben)


        self.verticalLayout_22.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(3)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.chk_deliver_cangbaotu = QCheckBox(self.groupBox_27)
        self.chk_deliver_cangbaotu.setObjectName(u"chk_deliver_cangbaotu")

        self.horizontalLayout_51.addWidget(self.chk_deliver_cangbaotu)

        self.edt_deliver_cangbaotu = QLineEdit(self.groupBox_27)
        self.edt_deliver_cangbaotu.setObjectName(u"edt_deliver_cangbaotu")

        self.horizontalLayout_51.addWidget(self.edt_deliver_cangbaotu)


        self.verticalLayout_22.addLayout(self.horizontalLayout_51)

        self.groupBox_9 = QGroupBox(self.widget_config_single)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(7, 4, 301, 240))
        self.groupBox_9.setMinimumSize(QSize(0, 240))
        self.groupBox_9.setMaximumSize(QSize(16777215, 300))
        self.gridLayout_22 = QGridLayout(self.groupBox_9)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(6, 6, 6, 6)
        self.groupBox_qing_li_tongbaodai = QGroupBox(self.groupBox_9)
        self.groupBox_qing_li_tongbaodai.setObjectName(u"groupBox_qing_li_tongbaodai")
        self.groupBox_qing_li_tongbaodai.setMaximumSize(QSize(16777215, 54))
        self.gridLayout_20 = QGridLayout(self.groupBox_qing_li_tongbaodai)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_tongbaodai_store = QRadioButton(self.groupBox_qing_li_tongbaodai)
        self.radio_clean_tongbaodai_store.setObjectName(u"radio_clean_tongbaodai_store")

        self.gridLayout_20.addWidget(self.radio_clean_tongbaodai_store, 0, 0, 1, 1)

        self.radio_clean_tongbaodai_use = QRadioButton(self.groupBox_qing_li_tongbaodai)
        self.radio_clean_tongbaodai_use.setObjectName(u"radio_clean_tongbaodai_use")
        self.radio_clean_tongbaodai_use.setChecked(True)

        self.gridLayout_20.addWidget(self.radio_clean_tongbaodai_use, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_qing_li_tongbaodai, 2, 2, 1, 1)

        self.groupBox_qing_li_yaocai = QGroupBox(self.groupBox_9)
        self.groupBox_qing_li_yaocai.setObjectName(u"groupBox_qing_li_yaocai")
        self.groupBox_qing_li_yaocai.setMaximumSize(QSize(16777215, 54))
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_qing_li_yaocai)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_drug_store = QRadioButton(self.groupBox_qing_li_yaocai)
        self.radio_clean_drug_store.setObjectName(u"radio_clean_drug_store")

        self.horizontalLayout_7.addWidget(self.radio_clean_drug_store)

        self.radio_clean_drug_sell = QRadioButton(self.groupBox_qing_li_yaocai)
        self.radio_clean_drug_sell.setObjectName(u"radio_clean_drug_sell")
        self.radio_clean_drug_sell.setChecked(True)

        self.horizontalLayout_7.addWidget(self.radio_clean_drug_sell)


        self.gridLayout_22.addWidget(self.groupBox_qing_li_yaocai, 0, 1, 1, 1)

        self.groupBox_qing_li_sixiang = QGroupBox(self.groupBox_9)
        self.groupBox_qing_li_sixiang.setObjectName(u"groupBox_qing_li_sixiang")
        self.groupBox_qing_li_sixiang.setMaximumSize(QSize(16777215, 54))
        self.gridLayout_23 = QGridLayout(self.groupBox_qing_li_sixiang)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_sixiang_store = QRadioButton(self.groupBox_qing_li_sixiang)
        self.radio_clean_sixiang_store.setObjectName(u"radio_clean_sixiang_store")

        self.gridLayout_23.addWidget(self.radio_clean_sixiang_store, 0, 0, 1, 1)

        self.radio_clean_sixiang_use = QRadioButton(self.groupBox_qing_li_sixiang)
        self.radio_clean_sixiang_use.setObjectName(u"radio_clean_sixiang_use")
        self.radio_clean_sixiang_use.setChecked(True)

        self.gridLayout_23.addWidget(self.radio_clean_sixiang_use, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_qing_li_sixiang, 2, 0, 1, 1)

        self.groupBox_qing_li_zhucai = QGroupBox(self.groupBox_9)
        self.groupBox_qing_li_zhucai.setObjectName(u"groupBox_qing_li_zhucai")
        self.groupBox_qing_li_zhucai.setMaximumSize(QSize(16777215, 54))
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_qing_li_zhucai)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_zhucai_store = QRadioButton(self.groupBox_qing_li_zhucai)
        self.radio_clean_zhucai_store.setObjectName(u"radio_clean_zhucai_store")

        self.horizontalLayout_8.addWidget(self.radio_clean_zhucai_store)

        self.radio_clean_zhucai_sell = QRadioButton(self.groupBox_qing_li_zhucai)
        self.radio_clean_zhucai_sell.setObjectName(u"radio_clean_zhucai_sell")
        self.radio_clean_zhucai_sell.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radio_clean_zhucai_sell)


        self.gridLayout_22.addWidget(self.groupBox_qing_li_zhucai, 1, 0, 1, 1)

        self.groupBox_qing_li_fucai = QGroupBox(self.groupBox_9)
        self.groupBox_qing_li_fucai.setObjectName(u"groupBox_qing_li_fucai")
        self.groupBox_qing_li_fucai.setMaximumSize(QSize(16777215, 54))
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_qing_li_fucai)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_fucai_store = QRadioButton(self.groupBox_qing_li_fucai)
        self.radio_clean_fucai_store.setObjectName(u"radio_clean_fucai_store")

        self.horizontalLayout_14.addWidget(self.radio_clean_fucai_store)

        self.radio_clean_fucai_sell = QRadioButton(self.groupBox_qing_li_fucai)
        self.radio_clean_fucai_sell.setObjectName(u"radio_clean_fucai_sell")
        self.radio_clean_fucai_sell.setChecked(True)

        self.horizontalLayout_14.addWidget(self.radio_clean_fucai_sell)


        self.gridLayout_22.addWidget(self.groupBox_qing_li_fucai, 1, 1, 1, 1)

        self.groupBox_qing_li_bailixiang = QGroupBox(self.groupBox_9)
        self.groupBox_qing_li_bailixiang.setObjectName(u"groupBox_qing_li_bailixiang")
        self.groupBox_qing_li_bailixiang.setMaximumSize(QSize(16777215, 54))
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_qing_li_bailixiang)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_bailixiang_store = QRadioButton(self.groupBox_qing_li_bailixiang)
        self.radio_clean_bailixiang_store.setObjectName(u"radio_clean_bailixiang_store")

        self.horizontalLayout_15.addWidget(self.radio_clean_bailixiang_store)

        self.radio_clean_bailixiang_throw = QRadioButton(self.groupBox_qing_li_bailixiang)
        self.radio_clean_bailixiang_throw.setObjectName(u"radio_clean_bailixiang_throw")
        self.radio_clean_bailixiang_throw.setChecked(True)

        self.horizontalLayout_15.addWidget(self.radio_clean_bailixiang_throw)


        self.gridLayout_22.addWidget(self.groupBox_qing_li_bailixiang, 2, 1, 1, 1)

        self.groupBox_qing_li_lingshi = QGroupBox(self.groupBox_9)
        self.groupBox_qing_li_lingshi.setObjectName(u"groupBox_qing_li_lingshi")
        self.groupBox_qing_li_lingshi.setMaximumSize(QSize(16777215, 54))
        self.horizontalLayout_58 = QHBoxLayout(self.groupBox_qing_li_lingshi)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_fucai_store_2 = QRadioButton(self.groupBox_qing_li_lingshi)
        self.radio_clean_fucai_store_2.setObjectName(u"radio_clean_fucai_store_2")
        self.radio_clean_fucai_store_2.setChecked(True)

        self.horizontalLayout_58.addWidget(self.radio_clean_fucai_store_2)

        self.radio_clean_fucai_sell_2 = QRadioButton(self.groupBox_qing_li_lingshi)
        self.radio_clean_fucai_sell_2.setObjectName(u"radio_clean_fucai_sell_2")
        self.radio_clean_fucai_sell_2.setChecked(False)

        self.horizontalLayout_58.addWidget(self.radio_clean_fucai_sell_2)


        self.gridLayout_22.addWidget(self.groupBox_qing_li_lingshi, 1, 2, 1, 1)

        self.groupBox_qing_li_zahuo = QGroupBox(self.groupBox_9)
        self.groupBox_qing_li_zahuo.setObjectName(u"groupBox_qing_li_zahuo")
        self.groupBox_qing_li_zahuo.setMaximumSize(QSize(16777215, 54))
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_qing_li_zahuo)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_zahuo_store = QRadioButton(self.groupBox_qing_li_zahuo)
        self.radio_clean_zahuo_store.setObjectName(u"radio_clean_zahuo_store")

        self.horizontalLayout_9.addWidget(self.radio_clean_zahuo_store)

        self.radio_clean_zahuo_sell = QRadioButton(self.groupBox_qing_li_zahuo)
        self.radio_clean_zahuo_sell.setObjectName(u"radio_clean_zahuo_sell")
        self.radio_clean_zahuo_sell.setChecked(True)

        self.horizontalLayout_9.addWidget(self.radio_clean_zahuo_sell)


        self.gridLayout_22.addWidget(self.groupBox_qing_li_zahuo, 0, 2, 1, 1)

        self.groupBox_qing_cangbaotu = QGroupBox(self.groupBox_9)
        self.groupBox_qing_cangbaotu.setObjectName(u"groupBox_qing_cangbaotu")
        self.groupBox_qing_cangbaotu.setMaximumSize(QSize(16777215, 54))
        self.horizontalLayout_37 = QHBoxLayout(self.groupBox_qing_cangbaotu)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_zhuqian_store_2 = QRadioButton(self.groupBox_qing_cangbaotu)
        self.radio_clean_zhuqian_store_2.setObjectName(u"radio_clean_zhuqian_store_2")

        self.horizontalLayout_37.addWidget(self.radio_clean_zhuqian_store_2)

        self.radio_clean_zhuqian_throw_2 = QRadioButton(self.groupBox_qing_cangbaotu)
        self.radio_clean_zhuqian_throw_2.setObjectName(u"radio_clean_zhuqian_throw_2")
        self.radio_clean_zhuqian_throw_2.setChecked(True)

        self.horizontalLayout_37.addWidget(self.radio_clean_zhuqian_throw_2)


        self.gridLayout_22.addWidget(self.groupBox_qing_cangbaotu, 0, 0, 1, 1)

        self.groupBox_qing_li_xun_ma = QGroupBox(self.groupBox_9)
        self.groupBox_qing_li_xun_ma.setObjectName(u"groupBox_qing_li_xun_ma")
        self.groupBox_qing_li_xun_ma.setMaximumSize(QSize(16777215, 54))
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_qing_li_xun_ma)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.radio_clean_zhucai_store_2 = QRadioButton(self.groupBox_qing_li_xun_ma)
        self.radio_clean_zhucai_store_2.setObjectName(u"radio_clean_zhucai_store_2")
        self.radio_clean_zhucai_store_2.setChecked(True)

        self.horizontalLayout_10.addWidget(self.radio_clean_zhucai_store_2)

        self.radio_clean_zhucai_sell_2 = QRadioButton(self.groupBox_qing_li_xun_ma)
        self.radio_clean_zhucai_sell_2.setObjectName(u"radio_clean_zhucai_sell_2")
        self.radio_clean_zhucai_sell_2.setChecked(False)

        self.horizontalLayout_10.addWidget(self.radio_clean_zhucai_sell_2)


        self.gridLayout_22.addWidget(self.groupBox_qing_li_xun_ma, 3, 0, 1, 1)

        self.groupBox = QGroupBox(self.widget_config_single)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(320, 4, 121, 422))
        self.groupBox.setMinimumSize(QSize(0, 422))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_25 = QVBoxLayout(self.groupBox)
        self.verticalLayout_25.setSpacing(4)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 6, -1, 6)
        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.cmb_shuaye_map = QComboBox(self.widget_3)
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.addItem("")
        self.cmb_shuaye_map.setObjectName(u"cmb_shuaye_map")
        self.cmb_shuaye_map.setMinimumSize(QSize(0, 20))
        self.cmb_shuaye_map.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_6.addWidget(self.cmb_shuaye_map)


        self.verticalLayout_25.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.groupBox)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_52 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_52.addWidget(self.label_5)

        self.edt_shuaye_time = QLineEdit(self.widget_4)
        self.edt_shuaye_time.setObjectName(u"edt_shuaye_time")
        self.edt_shuaye_time.setMinimumSize(QSize(0, 20))
        self.edt_shuaye_time.setMaximumSize(QSize(16777215, 20))
        self.edt_shuaye_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.edt_shuaye_time)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_52.addWidget(self.label_6)


        self.verticalLayout_25.addWidget(self.widget_4)

        self.groupBox_time_stop_shua_ye = QGroupBox(self.groupBox)
        self.groupBox_time_stop_shua_ye.setObjectName(u"groupBox_time_stop_shua_ye")
        self.groupBox_time_stop_shua_ye.setMaximumSize(QSize(16777215, 54))
        self.groupBox_time_stop_shua_ye.setCheckable(True)
        self.groupBox_time_stop_shua_ye.setChecked(False)
        self.gridLayout_27 = QGridLayout(self.groupBox_time_stop_shua_ye)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(6, 2, 3, 2)
        self.tedt_timer_shua_ye = QTimeEdit(self.groupBox_time_stop_shua_ye)
        self.tedt_timer_shua_ye.setObjectName(u"tedt_timer_shua_ye")
        self.tedt_timer_shua_ye.setMinimumSize(QSize(0, 25))
        self.tedt_timer_shua_ye.setTime(QTime(14, 4, 0))

        self.gridLayout_27.addWidget(self.tedt_timer_shua_ye, 0, 0, 1, 1)


        self.verticalLayout_25.addWidget(self.groupBox_time_stop_shua_ye)

        self.chk_shuaye_deliver = QCheckBox(self.groupBox)
        self.chk_shuaye_deliver.setObjectName(u"chk_shuaye_deliver")

        self.verticalLayout_25.addWidget(self.chk_shuaye_deliver)

        self.chk_shuaye_qingli = QCheckBox(self.groupBox)
        self.chk_shuaye_qingli.setObjectName(u"chk_shuaye_qingli")
        self.chk_shuaye_qingli.setChecked(True)

        self.verticalLayout_25.addWidget(self.chk_shuaye_qingli)

        self.chk_shuaye_fix_bb = QCheckBox(self.groupBox)
        self.chk_shuaye_fix_bb.setObjectName(u"chk_shuaye_fix_bb")
        self.chk_shuaye_fix_bb.setChecked(True)

        self.verticalLayout_25.addWidget(self.chk_shuaye_fix_bb)

        self.chk_shuaye_terse_bb = QCheckBox(self.groupBox)
        self.chk_shuaye_terse_bb.setObjectName(u"chk_shuaye_terse_bb")
        self.chk_shuaye_terse_bb.setChecked(False)

        self.verticalLayout_25.addWidget(self.chk_shuaye_terse_bb)

        self.chk_shuaye_xun_ma = QCheckBox(self.groupBox)
        self.chk_shuaye_xun_ma.setObjectName(u"chk_shuaye_xun_ma")
        self.chk_shuaye_xun_ma.setChecked(True)

        self.verticalLayout_25.addWidget(self.chk_shuaye_xun_ma)

        self.chk_shuaye_catch_bb = QCheckBox(self.groupBox)
        self.chk_shuaye_catch_bb.setObjectName(u"chk_shuaye_catch_bb")
        self.chk_shuaye_catch_bb.setChecked(True)

        self.verticalLayout_25.addWidget(self.chk_shuaye_catch_bb)

        self.chk_shuaye_fight_e_ren = QCheckBox(self.groupBox)
        self.chk_shuaye_fight_e_ren.setObjectName(u"chk_shuaye_fight_e_ren")
        self.chk_shuaye_fight_e_ren.setChecked(False)

        self.verticalLayout_25.addWidget(self.chk_shuaye_fight_e_ren)

        self.chk_shuaye_fight_yan = QCheckBox(self.groupBox)
        self.chk_shuaye_fight_yan.setObjectName(u"chk_shuaye_fight_yan")
        self.chk_shuaye_fight_yan.setChecked(False)

        self.verticalLayout_25.addWidget(self.chk_shuaye_fight_yan)

        self.chk_shuaye_che_tui = QCheckBox(self.groupBox)
        self.chk_shuaye_che_tui.setObjectName(u"chk_shuaye_che_tui")
        self.chk_shuaye_che_tui.setChecked(False)

        self.verticalLayout_25.addWidget(self.chk_shuaye_che_tui)

        self.chk_shuaye_qiandao = QCheckBox(self.groupBox)
        self.chk_shuaye_qiandao.setObjectName(u"chk_shuaye_qiandao")

        self.verticalLayout_25.addWidget(self.chk_shuaye_qiandao)

        self.groupBox_29 = QGroupBox(self.widget_config_single)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.groupBox_29.setGeometry(QRect(450, 292, 86, 82))
        self.verticalLayout_35 = QVBoxLayout(self.groupBox_29)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 6, -1, 6)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_65 = QLabel(self.groupBox_29)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_20.addWidget(self.label_65)

        self.spin_count_tang_zhu = QSpinBox(self.groupBox_29)
        self.spin_count_tang_zhu.setObjectName(u"spin_count_tang_zhu")
        self.spin_count_tang_zhu.setMinimumSize(QSize(0, 22))
        self.spin_count_tang_zhu.setMaximumSize(QSize(36, 16777215))
        self.spin_count_tang_zhu.setMaximum(100)
        self.spin_count_tang_zhu.setSingleStep(10)
        self.spin_count_tang_zhu.setValue(70)

        self.horizontalLayout_20.addWidget(self.spin_count_tang_zhu)


        self.verticalLayout_35.addLayout(self.horizontalLayout_20)

        self.cmb_tang_zhu = QComboBox(self.groupBox_29)
        self.cmb_tang_zhu.addItem("")
        self.cmb_tang_zhu.addItem("")
        self.cmb_tang_zhu.addItem("")
        self.cmb_tang_zhu.addItem("")
        self.cmb_tang_zhu.addItem("")
        self.cmb_tang_zhu.addItem("")
        self.cmb_tang_zhu.setObjectName(u"cmb_tang_zhu")

        self.verticalLayout_35.addWidget(self.cmb_tang_zhu)

        self.groupBox_zheng_zhan = QGroupBox(self.widget_config_single)
        self.groupBox_zheng_zhan.setObjectName(u"groupBox_zheng_zhan")
        self.groupBox_zheng_zhan.setGeometry(QRect(545, 292, 81, 81))
        self.groupBox_zheng_zhan.setMaximumSize(QSize(16777215, 88))
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_zheng_zhan)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(-1, 6, -1, 6)
        self.radioButton_3 = QRadioButton(self.groupBox_zheng_zhan)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(False)

        self.verticalLayout_31.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_zheng_zhan)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setChecked(True)

        self.verticalLayout_31.addWidget(self.radioButton_4)

        self.groupBox_33 = QGroupBox(self.widget_config_single)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.groupBox_33.setGeometry(QRect(450, 380, 78, 54))
        self.groupBox_33.setMinimumSize(QSize(0, 54))
        self.gridLayout_16 = QGridLayout(self.groupBox_33)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(6, 6, 6, 6)
        self.spin_count_wa_kuang_chu_tou = QSpinBox(self.groupBox_33)
        self.spin_count_wa_kuang_chu_tou.setObjectName(u"spin_count_wa_kuang_chu_tou")
        self.spin_count_wa_kuang_chu_tou.setMinimumSize(QSize(0, 22))
        self.spin_count_wa_kuang_chu_tou.setMaximumSize(QSize(40, 16777215))
        self.spin_count_wa_kuang_chu_tou.setMaximum(100)
        self.spin_count_wa_kuang_chu_tou.setSingleStep(1)
        self.spin_count_wa_kuang_chu_tou.setValue(3)

        self.gridLayout_16.addWidget(self.spin_count_wa_kuang_chu_tou, 0, 1, 1, 1)

        self.label_66 = QLabel(self.groupBox_33)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_16.addWidget(self.label_66, 0, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.widget_config_single)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(11, 317, 80, 56))
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_19.setSpacing(4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(6, 6, 6, 6)
        self.label_20 = QLabel(self.groupBox_12)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_19.addWidget(self.label_20)

        self.spin_count_si_xiang = QSpinBox(self.groupBox_12)
        self.spin_count_si_xiang.setObjectName(u"spin_count_si_xiang")
        self.spin_count_si_xiang.setMinimumSize(QSize(0, 22))
        self.spin_count_si_xiang.setMaximumSize(QSize(36, 16777215))
        self.spin_count_si_xiang.setMaximum(100)
        self.spin_count_si_xiang.setSingleStep(10)
        self.spin_count_si_xiang.setValue(20)

        self.horizontalLayout_19.addWidget(self.spin_count_si_xiang)

        self.groupBox_30 = QGroupBox(self.widget_config_single)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.groupBox_30.setGeometry(QRect(11, 251, 80, 54))
        self.groupBox_30.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_53 = QHBoxLayout(self.groupBox_30)
        self.horizontalLayout_53.setSpacing(4)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(6, 6, 6, 6)
        self.label_16 = QLabel(self.groupBox_30)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_53.addWidget(self.label_16)

        self.spin_count_pa_ta = QSpinBox(self.groupBox_30)
        self.spin_count_pa_ta.setObjectName(u"spin_count_pa_ta")
        self.spin_count_pa_ta.setMinimumSize(QSize(0, 22))
        self.spin_count_pa_ta.setMaximumSize(QSize(36, 16777215))
        self.spin_count_pa_ta.setMinimum(1)
        self.spin_count_pa_ta.setMaximum(199)
        self.spin_count_pa_ta.setValue(4)

        self.horizontalLayout_53.addWidget(self.spin_count_pa_ta)


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
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -113, 623, 500))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_config_team = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_config_team.setObjectName(u"widget_config_team")
        self.widget_config_team.setMinimumSize(QSize(0, 500))
        self.widget_31 = QWidget(self.widget_config_team)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setGeometry(QRect(7, 1, 111, 410))
        self.verticalLayout_16 = QVBoxLayout(self.widget_31)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.groupBox_8 = QGroupBox(self.widget_31)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 112))
        self.groupBox_8.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_23.setSpacing(3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_3 = QLabel(self.groupBox_8)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_46.addWidget(self.label_3)

        self.spin_count_ping_luan = QSpinBox(self.groupBox_8)
        self.spin_count_ping_luan.setObjectName(u"spin_count_ping_luan")
        self.spin_count_ping_luan.setMinimumSize(QSize(50, 0))
        self.spin_count_ping_luan.setMaximum(240)
        self.spin_count_ping_luan.setSingleStep(10)
        self.spin_count_ping_luan.setValue(240)

        self.horizontalLayout_46.addWidget(self.spin_count_ping_luan)


        self.verticalLayout_23.addLayout(self.horizontalLayout_46)

        self.groupBox_time_stop_ping_luan = QGroupBox(self.groupBox_8)
        self.groupBox_time_stop_ping_luan.setObjectName(u"groupBox_time_stop_ping_luan")
        self.groupBox_time_stop_ping_luan.setCheckable(True)
        self.groupBox_time_stop_ping_luan.setChecked(False)
        self.gridLayout_10 = QGridLayout(self.groupBox_time_stop_ping_luan)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(6, 2, 3, 2)
        self.tedt_timer_ping_luan = QTimeEdit(self.groupBox_time_stop_ping_luan)
        self.tedt_timer_ping_luan.setObjectName(u"tedt_timer_ping_luan")
        self.tedt_timer_ping_luan.setMinimumSize(QSize(0, 25))
        self.tedt_timer_ping_luan.setTime(QTime(14, 4, 0))

        self.gridLayout_10.addWidget(self.tedt_timer_ping_luan, 0, 0, 1, 1)


        self.verticalLayout_23.addWidget(self.groupBox_time_stop_ping_luan)


        self.verticalLayout_16.addWidget(self.groupBox_8)

        self.groupBox_5 = QGroupBox(self.widget_31)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 112))
        self.groupBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_24.setSpacing(3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setSpacing(3)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_50.addWidget(self.label_2)

        self.spin_count_wei_wang = QSpinBox(self.groupBox_5)
        self.spin_count_wei_wang.setObjectName(u"spin_count_wei_wang")
        self.spin_count_wei_wang.setMinimumSize(QSize(50, 0))
        self.spin_count_wei_wang.setMaximum(210)
        self.spin_count_wei_wang.setSingleStep(10)
        self.spin_count_wei_wang.setValue(210)

        self.horizontalLayout_50.addWidget(self.spin_count_wei_wang)


        self.verticalLayout_24.addLayout(self.horizontalLayout_50)

        self.groupBox_time_stop_wei_wang = QGroupBox(self.groupBox_5)
        self.groupBox_time_stop_wei_wang.setObjectName(u"groupBox_time_stop_wei_wang")
        self.groupBox_time_stop_wei_wang.setCheckable(True)
        self.groupBox_time_stop_wei_wang.setChecked(False)
        self.gridLayout = QGridLayout(self.groupBox_time_stop_wei_wang)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 2, 3, 2)
        self.tedt_timer_wei_wang = QTimeEdit(self.groupBox_time_stop_wei_wang)
        self.tedt_timer_wei_wang.setObjectName(u"tedt_timer_wei_wang")
        self.tedt_timer_wei_wang.setMinimumSize(QSize(0, 25))
        self.tedt_timer_wei_wang.setTime(QTime(14, 4, 0))

        self.gridLayout.addWidget(self.tedt_timer_wei_wang, 0, 0, 1, 1)


        self.verticalLayout_24.addWidget(self.groupBox_time_stop_wei_wang)


        self.verticalLayout_16.addWidget(self.groupBox_5)

        self.groupBox_31 = QGroupBox(self.widget_31)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setMinimumSize(QSize(0, 156))
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_31)
        self.verticalLayout_26.setSpacing(3)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(6, 6, 6, 6)
        self.cmb_shuaye_team_map = QComboBox(self.groupBox_31)
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.addItem("")
        self.cmb_shuaye_team_map.setObjectName(u"cmb_shuaye_team_map")
        self.cmb_shuaye_team_map.setMinimumSize(QSize(80, 20))
        self.cmb_shuaye_team_map.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_26.addWidget(self.cmb_shuaye_team_map)

        self.chk_shuaye_team_fix_bb = QCheckBox(self.groupBox_31)
        self.chk_shuaye_team_fix_bb.setObjectName(u"chk_shuaye_team_fix_bb")
        self.chk_shuaye_team_fix_bb.setChecked(True)

        self.verticalLayout_26.addWidget(self.chk_shuaye_team_fix_bb)

        self.groupBox_time_stop_shua_ye_team = QGroupBox(self.groupBox_31)
        self.groupBox_time_stop_shua_ye_team.setObjectName(u"groupBox_time_stop_shua_ye_team")
        self.groupBox_time_stop_shua_ye_team.setCheckable(True)
        self.groupBox_time_stop_shua_ye_team.setChecked(True)
        self.gridLayout_28 = QGridLayout(self.groupBox_time_stop_shua_ye_team)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(6, 2, 3, 2)
        self.tedt_timer_shua_ye_team = QTimeEdit(self.groupBox_time_stop_shua_ye_team)
        self.tedt_timer_shua_ye_team.setObjectName(u"tedt_timer_shua_ye_team")
        self.tedt_timer_shua_ye_team.setMinimumSize(QSize(0, 25))
        self.tedt_timer_shua_ye_team.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(20, 32, 0)))
        self.tedt_timer_shua_ye_team.setTime(QTime(20, 32, 0))

        self.gridLayout_28.addWidget(self.tedt_timer_shua_ye_team, 0, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.groupBox_time_stop_shua_ye_team)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_22 = QLabel(self.groupBox_31)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_60.addWidget(self.label_22)

        self.edt_shuaye_team_time = QLineEdit(self.groupBox_31)
        self.edt_shuaye_team_time.setObjectName(u"edt_shuaye_team_time")
        self.edt_shuaye_team_time.setMinimumSize(QSize(0, 20))
        self.edt_shuaye_team_time.setMaximumSize(QSize(16777215, 20))
        self.edt_shuaye_team_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.edt_shuaye_team_time)

        self.label_48 = QLabel(self.groupBox_31)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_60.addWidget(self.label_48)


        self.verticalLayout_26.addLayout(self.horizontalLayout_60)


        self.verticalLayout_16.addWidget(self.groupBox_31)

        self.groupBox_23 = QGroupBox(self.widget_config_team)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setGeometry(QRect(128, 400, 261, 91))
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_23)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label = QLabel(self.groupBox_23)
        self.label.setObjectName(u"label")

        self.horizontalLayout_30.addWidget(self.label)

        self.cmb_ma_zei_map1 = QComboBox(self.groupBox_23)
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.addItem("")
        self.cmb_ma_zei_map1.setObjectName(u"cmb_ma_zei_map1")
        self.cmb_ma_zei_map1.setMinimumSize(QSize(70, 20))
        self.cmb_ma_zei_map1.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_30.addWidget(self.cmb_ma_zei_map1)

        self.label_7 = QLabel(self.groupBox_23)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_30.addWidget(self.label_7)

        self.cmb_ma_zei_map2 = QComboBox(self.groupBox_23)
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.addItem("")
        self.cmb_ma_zei_map2.setObjectName(u"cmb_ma_zei_map2")
        self.cmb_ma_zei_map2.setMinimumSize(QSize(70, 20))
        self.cmb_ma_zei_map2.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_30.addWidget(self.cmb_ma_zei_map2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_30)

        self.chk_ma_zei_continue = QCheckBox(self.groupBox_23)
        self.chk_ma_zei_continue.setObjectName(u"chk_ma_zei_continue")

        self.verticalLayout_13.addWidget(self.chk_ma_zei_continue)

        self.groupBox_2 = QGroupBox(self.widget_config_team)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(447, 134, 128, 54))
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_12.addWidget(self.label_18)

        self.cmb_daniu_map = QComboBox(self.groupBox_2)
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.addItem("")
        self.cmb_daniu_map.setObjectName(u"cmb_daniu_map")
        self.cmb_daniu_map.setMinimumSize(QSize(80, 20))
        self.cmb_daniu_map.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_12.addWidget(self.cmb_daniu_map)

        self.groupBox_6 = QGroupBox(self.widget_config_team)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(350, 134, 91, 54))
        self.gridLayout_9 = QGridLayout(self.groupBox_6)
        self.gridLayout_9.setSpacing(4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(4, 2, 4, 2)
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(26, 16777215))

        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 1)

        self.cmb_double_time = QComboBox(self.groupBox_6)
        self.cmb_double_time.addItem("")
        self.cmb_double_time.addItem("")
        self.cmb_double_time.addItem("")
        self.cmb_double_time.setObjectName(u"cmb_double_time")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cmb_double_time.sizePolicy().hasHeightForWidth())
        self.cmb_double_time.setSizePolicy(sizePolicy3)
        self.cmb_double_time.setMinimumSize(QSize(55, 20))
        self.cmb_double_time.setMaximumSize(QSize(52, 20))

        self.gridLayout_9.addWidget(self.cmb_double_time, 0, 1, 1, 1)

        self.groupBox_16 = QGroupBox(self.widget_config_team)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(349, 2, 291, 131))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.groupBox_fuben_bb90 = QGroupBox(self.groupBox_16)
        self.groupBox_fuben_bb90.setObjectName(u"groupBox_fuben_bb90")
        self.groupBox_fuben_bb90.setCheckable(True)
        self.verticalLayout = QVBoxLayout(self.groupBox_fuben_bb90)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 6, 0)
        self.radio_bb_fuben_hsrm = QRadioButton(self.groupBox_fuben_bb90)
        self.radio_bb_fuben_hsrm.setObjectName(u"radio_bb_fuben_hsrm")
        self.radio_bb_fuben_hsrm.setChecked(True)

        self.verticalLayout.addWidget(self.radio_bb_fuben_hsrm)

        self.radio_bb_fuben_zpwk = QRadioButton(self.groupBox_fuben_bb90)
        self.radio_bb_fuben_zpwk.setObjectName(u"radio_bb_fuben_zpwk")

        self.verticalLayout.addWidget(self.radio_bb_fuben_zpwk)

        self.radio_bb_fuben_znpd = QRadioButton(self.groupBox_fuben_bb90)
        self.radio_bb_fuben_znpd.setObjectName(u"radio_bb_fuben_znpd")

        self.verticalLayout.addWidget(self.radio_bb_fuben_znpd)


        self.horizontalLayout_4.addWidget(self.groupBox_fuben_bb90)

        self.groupBox_fuben_bb100 = QGroupBox(self.groupBox_16)
        self.groupBox_fuben_bb100.setObjectName(u"groupBox_fuben_bb100")
        self.groupBox_fuben_bb100.setCheckable(True)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_fuben_bb100)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 0, 6, 0)
        self.radio_bb_fuben_jzhs = QRadioButton(self.groupBox_fuben_bb100)
        self.radio_bb_fuben_jzhs.setObjectName(u"radio_bb_fuben_jzhs")
        self.radio_bb_fuben_jzhs.setChecked(True)

        self.verticalLayout_7.addWidget(self.radio_bb_fuben_jzhs)

        self.radio_bb_fuben_dzwd = QRadioButton(self.groupBox_fuben_bb100)
        self.radio_bb_fuben_dzwd.setObjectName(u"radio_bb_fuben_dzwd")

        self.verticalLayout_7.addWidget(self.radio_bb_fuben_dzwd)

        self.radio_bb_fuben_wldh = QRadioButton(self.groupBox_fuben_bb100)
        self.radio_bb_fuben_wldh.setObjectName(u"radio_bb_fuben_wldh")

        self.verticalLayout_7.addWidget(self.radio_bb_fuben_wldh)


        self.horizontalLayout_4.addWidget(self.groupBox_fuben_bb100)

        self.groupBox_fuben_bb110 = QGroupBox(self.groupBox_16)
        self.groupBox_fuben_bb110.setObjectName(u"groupBox_fuben_bb110")
        self.groupBox_fuben_bb110.setCheckable(True)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_fuben_bb110)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(6, 0, 6, 0)
        self.radio_bb_fuben_wljp = QRadioButton(self.groupBox_fuben_bb110)
        self.radio_bb_fuben_wljp.setObjectName(u"radio_bb_fuben_wljp")
        self.radio_bb_fuben_wljp.setChecked(True)

        self.verticalLayout_12.addWidget(self.radio_bb_fuben_wljp)

        self.radio_bb_fuben_thzq = QRadioButton(self.groupBox_fuben_bb110)
        self.radio_bb_fuben_thzq.setObjectName(u"radio_bb_fuben_thzq")

        self.verticalLayout_12.addWidget(self.radio_bb_fuben_thzq)

        self.radio_bb_fuben_mzzz = QRadioButton(self.groupBox_fuben_bb110)
        self.radio_bb_fuben_mzzz.setObjectName(u"radio_bb_fuben_mzzz")

        self.verticalLayout_12.addWidget(self.radio_bb_fuben_mzzz)


        self.horizontalLayout_4.addWidget(self.groupBox_fuben_bb110)

        self.groupBox_13 = QGroupBox(self.widget_config_team)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(239, 2, 103, 191))
        self.gridLayout_17 = QGridLayout(self.groupBox_13)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_26 = QLabel(self.groupBox_13)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(48, 0))

        self.gridLayout_17.addWidget(self.label_26, 0, 0, 1, 1)

        self.spin_count_fuben_70_meng = QSpinBox(self.groupBox_13)
        self.spin_count_fuben_70_meng.setObjectName(u"spin_count_fuben_70_meng")
        self.spin_count_fuben_70_meng.setMaximum(3)

        self.gridLayout_17.addWidget(self.spin_count_fuben_70_meng, 0, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(48, 0))

        self.gridLayout_17.addWidget(self.label_28, 1, 0, 1, 1)

        self.spin_count_fuben_80_meng = QSpinBox(self.groupBox_13)
        self.spin_count_fuben_80_meng.setObjectName(u"spin_count_fuben_80_meng")
        self.spin_count_fuben_80_meng.setMaximum(1)

        self.gridLayout_17.addWidget(self.spin_count_fuben_80_meng, 1, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(48, 0))

        self.gridLayout_17.addWidget(self.label_29, 2, 0, 1, 1)

        self.spin_count_fuben_90_meng = QSpinBox(self.groupBox_13)
        self.spin_count_fuben_90_meng.setObjectName(u"spin_count_fuben_90_meng")
        self.spin_count_fuben_90_meng.setMaximum(1)

        self.gridLayout_17.addWidget(self.spin_count_fuben_90_meng, 2, 1, 1, 1)

        self.label_30 = QLabel(self.groupBox_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(48, 0))

        self.gridLayout_17.addWidget(self.label_30, 3, 0, 1, 1)

        self.spin_count_fuben_100_hua = QSpinBox(self.groupBox_13)
        self.spin_count_fuben_100_hua.setObjectName(u"spin_count_fuben_100_hua")
        self.spin_count_fuben_100_hua.setMaximum(1)

        self.gridLayout_17.addWidget(self.spin_count_fuben_100_hua, 3, 1, 1, 1)

        self.label_56 = QLabel(self.groupBox_13)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(48, 0))

        self.gridLayout_17.addWidget(self.label_56, 4, 0, 1, 1)

        self.spin_count_fuben_110_wu = QSpinBox(self.groupBox_13)
        self.spin_count_fuben_110_wu.setObjectName(u"spin_count_fuben_110_wu")
        self.spin_count_fuben_110_wu.setMaximum(1)

        self.gridLayout_17.addWidget(self.spin_count_fuben_110_wu, 4, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.widget_config_team)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(127, 1, 104, 191))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.chk_duiyuan_ls = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_ls.setObjectName(u"chk_duiyuan_ls")
        self.chk_duiyuan_ls.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_ls.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_ls.setChecked(True)

        self.verticalLayout_8.addWidget(self.chk_duiyuan_ls)

        self.chk_duiyuan_ds = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_ds.setObjectName(u"chk_duiyuan_ds")
        self.chk_duiyuan_ds.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_ds.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_ds.setChecked(True)

        self.verticalLayout_8.addWidget(self.chk_duiyuan_ds)

        self.chk_duiyuan_js = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_js.setObjectName(u"chk_duiyuan_js")
        self.chk_duiyuan_js.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_js.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_js.setChecked(True)

        self.verticalLayout_8.addWidget(self.chk_duiyuan_js)

        self.chk_duiyuan_ld = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_ld.setObjectName(u"chk_duiyuan_ld")
        self.chk_duiyuan_ld.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_ld.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_ld.setChecked(True)

        self.verticalLayout_8.addWidget(self.chk_duiyuan_ld)

        self.chk_duiyuan_hx = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_hx.setObjectName(u"chk_duiyuan_hx")
        self.chk_duiyuan_hx.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_hx.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_hx.setChecked(True)

        self.verticalLayout_8.addWidget(self.chk_duiyuan_hx)

        self.groupBox_32 = QGroupBox(self.widget_config_team)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.groupBox_32.setGeometry(QRect(127, 195, 511, 196))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_32)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.chk_super_chanllenge_fix_bb = QCheckBox(self.groupBox_32)
        self.chk_super_chanllenge_fix_bb.setObjectName(u"chk_super_chanllenge_fix_bb")

        self.horizontalLayout_24.addWidget(self.chk_super_chanllenge_fix_bb)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_2)

        self.label_62 = QLabel(self.groupBox_32)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_24.addWidget(self.label_62)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.groupBox_17 = QGroupBox(self.groupBox_32)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setMaximumSize(QSize(90, 16777215))
        self.gridLayout_25 = QGridLayout(self.groupBox_17)
        self.gridLayout_25.setSpacing(4)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(4, 4, 4, 4)
        self.label_27 = QLabel(self.groupBox_17)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(34, 0))

        self.gridLayout_25.addWidget(self.label_27, 0, 0, 1, 1)

        self.spin_count_mingbu_wuqing = QSpinBox(self.groupBox_17)
        self.spin_count_mingbu_wuqing.setObjectName(u"spin_count_mingbu_wuqing")
        self.spin_count_mingbu_wuqing.setMinimumSize(QSize(0, 22))
        self.spin_count_mingbu_wuqing.setMaximumSize(QSize(34, 16777215))
        self.spin_count_mingbu_wuqing.setMinimum(-1)
        self.spin_count_mingbu_wuqing.setMaximum(4)

        self.gridLayout_25.addWidget(self.spin_count_mingbu_wuqing, 0, 1, 1, 1)

        self.label_31 = QLabel(self.groupBox_17)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(34, 0))

        self.gridLayout_25.addWidget(self.label_31, 1, 0, 1, 1)

        self.spin_count_mingbu_tieshou = QSpinBox(self.groupBox_17)
        self.spin_count_mingbu_tieshou.setObjectName(u"spin_count_mingbu_tieshou")
        self.spin_count_mingbu_tieshou.setMinimumSize(QSize(0, 22))
        self.spin_count_mingbu_tieshou.setMaximumSize(QSize(34, 16777215))
        self.spin_count_mingbu_tieshou.setMinimum(-1)
        self.spin_count_mingbu_tieshou.setMaximum(4)

        self.gridLayout_25.addWidget(self.spin_count_mingbu_tieshou, 1, 1, 1, 1)

        self.label_32 = QLabel(self.groupBox_17)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(34, 0))

        self.gridLayout_25.addWidget(self.label_32, 2, 0, 1, 1)

        self.spin_count_mingbu_zhuiming = QSpinBox(self.groupBox_17)
        self.spin_count_mingbu_zhuiming.setObjectName(u"spin_count_mingbu_zhuiming")
        self.spin_count_mingbu_zhuiming.setMinimumSize(QSize(0, 22))
        self.spin_count_mingbu_zhuiming.setMaximumSize(QSize(34, 16777215))
        self.spin_count_mingbu_zhuiming.setMinimum(-1)
        self.spin_count_mingbu_zhuiming.setMaximum(4)

        self.gridLayout_25.addWidget(self.spin_count_mingbu_zhuiming, 2, 1, 1, 1)

        self.label_33 = QLabel(self.groupBox_17)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(34, 0))

        self.gridLayout_25.addWidget(self.label_33, 3, 0, 1, 1)

        self.spin_count_mingbu_lengxue = QSpinBox(self.groupBox_17)
        self.spin_count_mingbu_lengxue.setObjectName(u"spin_count_mingbu_lengxue")
        self.spin_count_mingbu_lengxue.setMinimumSize(QSize(0, 22))
        self.spin_count_mingbu_lengxue.setMaximumSize(QSize(34, 16777215))
        self.spin_count_mingbu_lengxue.setMinimum(-1)
        self.spin_count_mingbu_lengxue.setMaximum(4)

        self.gridLayout_25.addWidget(self.spin_count_mingbu_lengxue, 3, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.groupBox_17)

        self.groupBox_18 = QGroupBox(self.groupBox_32)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_19 = QGridLayout(self.groupBox_18)
        self.gridLayout_19.setSpacing(4)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(4, 4, 4, 4)
        self.label_34 = QLabel(self.groupBox_18)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(48, 0))

        self.gridLayout_19.addWidget(self.label_34, 0, 0, 1, 1)

        self.spin_count_mingjiao_weiyixiao = QSpinBox(self.groupBox_18)
        self.spin_count_mingjiao_weiyixiao.setObjectName(u"spin_count_mingjiao_weiyixiao")
        self.spin_count_mingjiao_weiyixiao.setMinimumSize(QSize(0, 22))
        self.spin_count_mingjiao_weiyixiao.setMaximumSize(QSize(34, 16777215))
        self.spin_count_mingjiao_weiyixiao.setMinimum(-1)
        self.spin_count_mingjiao_weiyixiao.setMaximum(4)

        self.gridLayout_19.addWidget(self.spin_count_mingjiao_weiyixiao, 0, 1, 1, 1)

        self.label_35 = QLabel(self.groupBox_18)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(48, 0))

        self.gridLayout_19.addWidget(self.label_35, 1, 0, 1, 1)

        self.spin_count_mingjiao_xiexun = QSpinBox(self.groupBox_18)
        self.spin_count_mingjiao_xiexun.setObjectName(u"spin_count_mingjiao_xiexun")
        self.spin_count_mingjiao_xiexun.setMinimumSize(QSize(0, 22))
        self.spin_count_mingjiao_xiexun.setMaximumSize(QSize(34, 16777215))
        self.spin_count_mingjiao_xiexun.setMinimum(-1)
        self.spin_count_mingjiao_xiexun.setMaximum(4)

        self.gridLayout_19.addWidget(self.spin_count_mingjiao_xiexun, 1, 1, 1, 1)

        self.label_36 = QLabel(self.groupBox_18)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(48, 0))

        self.gridLayout_19.addWidget(self.label_36, 2, 0, 1, 1)

        self.spin_count_mingjiao_yintianzheng = QSpinBox(self.groupBox_18)
        self.spin_count_mingjiao_yintianzheng.setObjectName(u"spin_count_mingjiao_yintianzheng")
        self.spin_count_mingjiao_yintianzheng.setMinimumSize(QSize(0, 22))
        self.spin_count_mingjiao_yintianzheng.setMaximumSize(QSize(34, 16777215))
        self.spin_count_mingjiao_yintianzheng.setMinimum(-1)
        self.spin_count_mingjiao_yintianzheng.setMaximum(4)

        self.gridLayout_19.addWidget(self.spin_count_mingjiao_yintianzheng, 2, 1, 1, 1)

        self.label_37 = QLabel(self.groupBox_18)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(48, 0))

        self.gridLayout_19.addWidget(self.label_37, 3, 0, 1, 1)

        self.spin_count_mingjiao_zishan = QSpinBox(self.groupBox_18)
        self.spin_count_mingjiao_zishan.setObjectName(u"spin_count_mingjiao_zishan")
        self.spin_count_mingjiao_zishan.setMinimumSize(QSize(0, 22))
        self.spin_count_mingjiao_zishan.setMaximumSize(QSize(34, 16777215))
        self.spin_count_mingjiao_zishan.setMinimum(-1)
        self.spin_count_mingjiao_zishan.setMaximum(4)

        self.gridLayout_19.addWidget(self.spin_count_mingjiao_zishan, 3, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.groupBox_18)

        self.groupBox_19 = QGroupBox(self.groupBox_32)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_15 = QGridLayout(self.groupBox_19)
        self.gridLayout_15.setSpacing(4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(4, 4, 4, 4)
        self.label_38 = QLabel(self.groupBox_19)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(48, 0))

        self.gridLayout_15.addWidget(self.label_38, 0, 0, 1, 1)

        self.spin_count_wujue_huangyaoshi = QSpinBox(self.groupBox_19)
        self.spin_count_wujue_huangyaoshi.setObjectName(u"spin_count_wujue_huangyaoshi")
        self.spin_count_wujue_huangyaoshi.setMinimumSize(QSize(0, 22))
        self.spin_count_wujue_huangyaoshi.setMaximumSize(QSize(34, 16777215))
        self.spin_count_wujue_huangyaoshi.setMinimum(-1)
        self.spin_count_wujue_huangyaoshi.setMaximum(4)

        self.gridLayout_15.addWidget(self.spin_count_wujue_huangyaoshi, 0, 1, 1, 1)

        self.label_39 = QLabel(self.groupBox_19)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(48, 0))

        self.gridLayout_15.addWidget(self.label_39, 1, 0, 1, 1)

        self.spin_count_wujue_ouyangfeng = QSpinBox(self.groupBox_19)
        self.spin_count_wujue_ouyangfeng.setObjectName(u"spin_count_wujue_ouyangfeng")
        self.spin_count_wujue_ouyangfeng.setMinimumSize(QSize(0, 22))
        self.spin_count_wujue_ouyangfeng.setMaximumSize(QSize(34, 16777215))
        self.spin_count_wujue_ouyangfeng.setMinimum(-1)
        self.spin_count_wujue_ouyangfeng.setMaximum(4)

        self.gridLayout_15.addWidget(self.spin_count_wujue_ouyangfeng, 1, 1, 1, 1)

        self.label_40 = QLabel(self.groupBox_19)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(48, 0))

        self.gridLayout_15.addWidget(self.label_40, 2, 0, 1, 1)

        self.spin_count_wujue_duanzhixing = QSpinBox(self.groupBox_19)
        self.spin_count_wujue_duanzhixing.setObjectName(u"spin_count_wujue_duanzhixing")
        self.spin_count_wujue_duanzhixing.setMinimumSize(QSize(0, 22))
        self.spin_count_wujue_duanzhixing.setMaximumSize(QSize(34, 16777215))
        self.spin_count_wujue_duanzhixing.setMinimum(-1)
        self.spin_count_wujue_duanzhixing.setMaximum(4)

        self.gridLayout_15.addWidget(self.spin_count_wujue_duanzhixing, 2, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_19)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(48, 0))

        self.gridLayout_15.addWidget(self.label_41, 3, 0, 1, 1)

        self.spin_count_wujue_hongqi = QSpinBox(self.groupBox_19)
        self.spin_count_wujue_hongqi.setObjectName(u"spin_count_wujue_hongqi")
        self.spin_count_wujue_hongqi.setMinimumSize(QSize(0, 22))
        self.spin_count_wujue_hongqi.setMaximumSize(QSize(34, 16777215))
        self.spin_count_wujue_hongqi.setMinimum(-1)
        self.spin_count_wujue_hongqi.setMaximum(4)

        self.gridLayout_15.addWidget(self.spin_count_wujue_hongqi, 3, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.groupBox_19)

        self.groupBox_20 = QGroupBox(self.groupBox_32)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_13 = QGridLayout(self.groupBox_20)
        self.gridLayout_13.setSpacing(4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(4, 4, 4, 4)
        self.label_42 = QLabel(self.groupBox_20)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(48, 0))

        self.gridLayout_13.addWidget(self.label_42, 0, 0, 1, 1)

        self.spin_count_zijin_huamanlou = QSpinBox(self.groupBox_20)
        self.spin_count_zijin_huamanlou.setObjectName(u"spin_count_zijin_huamanlou")
        self.spin_count_zijin_huamanlou.setMinimumSize(QSize(0, 22))
        self.spin_count_zijin_huamanlou.setMaximumSize(QSize(34, 16777215))
        self.spin_count_zijin_huamanlou.setMinimum(-1)
        self.spin_count_zijin_huamanlou.setMaximum(4)

        self.gridLayout_13.addWidget(self.spin_count_zijin_huamanlou, 0, 1, 1, 1)

        self.label_43 = QLabel(self.groupBox_20)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(48, 0))

        self.gridLayout_13.addWidget(self.label_43, 1, 0, 1, 1)

        self.spin_count_zijin_sikongzhaixing = QSpinBox(self.groupBox_20)
        self.spin_count_zijin_sikongzhaixing.setObjectName(u"spin_count_zijin_sikongzhaixing")
        self.spin_count_zijin_sikongzhaixing.setMinimumSize(QSize(0, 22))
        self.spin_count_zijin_sikongzhaixing.setMaximumSize(QSize(34, 16777215))
        self.spin_count_zijin_sikongzhaixing.setMinimum(-1)
        self.spin_count_zijin_sikongzhaixing.setMaximum(4)

        self.gridLayout_13.addWidget(self.spin_count_zijin_sikongzhaixing, 1, 1, 1, 1)

        self.label_44 = QLabel(self.groupBox_20)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(48, 0))

        self.gridLayout_13.addWidget(self.label_44, 2, 0, 1, 1)

        self.spin_count_zijin_yegucheng = QSpinBox(self.groupBox_20)
        self.spin_count_zijin_yegucheng.setObjectName(u"spin_count_zijin_yegucheng")
        self.spin_count_zijin_yegucheng.setMinimumSize(QSize(0, 22))
        self.spin_count_zijin_yegucheng.setMaximumSize(QSize(34, 16777215))
        self.spin_count_zijin_yegucheng.setMinimum(-1)
        self.spin_count_zijin_yegucheng.setMaximum(4)

        self.gridLayout_13.addWidget(self.spin_count_zijin_yegucheng, 2, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_20)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(48, 0))

        self.gridLayout_13.addWidget(self.label_45, 3, 0, 1, 1)

        self.spin_count_zijin_ximenchuixue = QSpinBox(self.groupBox_20)
        self.spin_count_zijin_ximenchuixue.setObjectName(u"spin_count_zijin_ximenchuixue")
        self.spin_count_zijin_ximenchuixue.setMinimumSize(QSize(0, 22))
        self.spin_count_zijin_ximenchuixue.setMaximumSize(QSize(34, 16777215))
        self.spin_count_zijin_ximenchuixue.setMinimum(-1)
        self.spin_count_zijin_ximenchuixue.setMaximum(4)

        self.gridLayout_13.addWidget(self.spin_count_zijin_ximenchuixue, 3, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.groupBox_20)

        self.groupBox_21 = QGroupBox(self.groupBox_32)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.gridLayout_12 = QGridLayout(self.groupBox_21)
        self.gridLayout_12.setSpacing(4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(4, 4, 4, 4)
        self.label_46 = QLabel(self.groupBox_21)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(48, 0))

        self.gridLayout_12.addWidget(self.label_46, 0, 0, 1, 1)

        self.spin_count_zhenlong_suxinghe = QSpinBox(self.groupBox_21)
        self.spin_count_zhenlong_suxinghe.setObjectName(u"spin_count_zhenlong_suxinghe")
        self.spin_count_zhenlong_suxinghe.setMinimumSize(QSize(0, 22))
        self.spin_count_zhenlong_suxinghe.setMaximumSize(QSize(34, 16777215))
        self.spin_count_zhenlong_suxinghe.setMinimum(-1)
        self.spin_count_zhenlong_suxinghe.setMaximum(4)

        self.gridLayout_12.addWidget(self.spin_count_zhenlong_suxinghe, 0, 1, 1, 1)

        self.label_47 = QLabel(self.groupBox_21)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(48, 0))

        self.gridLayout_12.addWidget(self.label_47, 1, 0, 1, 1)

        self.spin_count_zhenlong_dingchunqiu = QSpinBox(self.groupBox_21)
        self.spin_count_zhenlong_dingchunqiu.setObjectName(u"spin_count_zhenlong_dingchunqiu")
        self.spin_count_zhenlong_dingchunqiu.setMinimumSize(QSize(0, 22))
        self.spin_count_zhenlong_dingchunqiu.setMaximumSize(QSize(34, 16777215))
        self.spin_count_zhenlong_dingchunqiu.setMinimum(-1)
        self.spin_count_zhenlong_dingchunqiu.setMaximum(4)

        self.gridLayout_12.addWidget(self.spin_count_zhenlong_dingchunqiu, 1, 1, 1, 1)

        self.label_50 = QLabel(self.groupBox_21)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(48, 0))

        self.gridLayout_12.addWidget(self.label_50, 2, 0, 1, 1)

        self.spin_count_zhenlong_liqiusuhi = QSpinBox(self.groupBox_21)
        self.spin_count_zhenlong_liqiusuhi.setObjectName(u"spin_count_zhenlong_liqiusuhi")
        self.spin_count_zhenlong_liqiusuhi.setMinimumSize(QSize(0, 22))
        self.spin_count_zhenlong_liqiusuhi.setMaximumSize(QSize(34, 16777215))
        self.spin_count_zhenlong_liqiusuhi.setMinimum(-1)
        self.spin_count_zhenlong_liqiusuhi.setMaximum(4)

        self.gridLayout_12.addWidget(self.spin_count_zhenlong_liqiusuhi, 2, 1, 1, 1)

        self.label_51 = QLabel(self.groupBox_21)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(48, 0))

        self.gridLayout_12.addWidget(self.label_51, 3, 0, 1, 1)

        self.spin_count_zhenlong_tianshantongmu = QSpinBox(self.groupBox_21)
        self.spin_count_zhenlong_tianshantongmu.setObjectName(u"spin_count_zhenlong_tianshantongmu")
        self.spin_count_zhenlong_tianshantongmu.setMinimumSize(QSize(0, 22))
        self.spin_count_zhenlong_tianshantongmu.setMaximumSize(QSize(34, 16777215))
        self.spin_count_zhenlong_tianshantongmu.setMinimum(-1)
        self.spin_count_zhenlong_tianshantongmu.setMaximum(4)

        self.gridLayout_12.addWidget(self.spin_count_zhenlong_tianshantongmu, 3, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.groupBox_21)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)


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
        self.groupBox_14 = QGroupBox(self.widget_config_other)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(274, 4, 98, 212))
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.chk_shiyong_bai_li_xiang = QCheckBox(self.groupBox_14)
        self.chk_shiyong_bai_li_xiang.setObjectName(u"chk_shiyong_bai_li_xiang")
        self.chk_shiyong_bai_li_xiang.setChecked(True)

        self.verticalLayout_15.addWidget(self.chk_shiyong_bai_li_xiang)

        self.chk_shiyong_hnx = QCheckBox(self.groupBox_14)
        self.chk_shiyong_hnx.setObjectName(u"chk_shiyong_hnx")
        self.chk_shiyong_hnx.setChecked(True)

        self.verticalLayout_15.addWidget(self.chk_shiyong_hnx)

        self.chk_shiyong_xiulianjuan = QCheckBox(self.groupBox_14)
        self.chk_shiyong_xiulianjuan.setObjectName(u"chk_shiyong_xiulianjuan")
        self.chk_shiyong_xiulianjuan.setChecked(True)

        self.verticalLayout_15.addWidget(self.chk_shiyong_xiulianjuan)

        self.chk_shiyong_tongbaozuan = QCheckBox(self.groupBox_14)
        self.chk_shiyong_tongbaozuan.setObjectName(u"chk_shiyong_tongbaozuan")
        self.chk_shiyong_tongbaozuan.setChecked(True)

        self.verticalLayout_15.addWidget(self.chk_shiyong_tongbaozuan)

        self.chk_shiyong_tianmingsuipian = QCheckBox(self.groupBox_14)
        self.chk_shiyong_tianmingsuipian.setObjectName(u"chk_shiyong_tianmingsuipian")
        self.chk_shiyong_tianmingsuipian.setChecked(True)

        self.verticalLayout_15.addWidget(self.chk_shiyong_tianmingsuipian)

        self.chk_shiyong_xinglangyueka = QCheckBox(self.groupBox_14)
        self.chk_shiyong_xinglangyueka.setObjectName(u"chk_shiyong_xinglangyueka")
        self.chk_shiyong_xinglangyueka.setChecked(True)

        self.verticalLayout_15.addWidget(self.chk_shiyong_xinglangyueka)

        self.chk_shiyong_sixiang = QCheckBox(self.groupBox_14)
        self.chk_shiyong_sixiang.setObjectName(u"chk_shiyong_sixiang")
        self.chk_shiyong_sixiang.setChecked(True)

        self.verticalLayout_15.addWidget(self.chk_shiyong_sixiang)

        self.groupBox_26 = QGroupBox(self.widget_config_other)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setGeometry(QRect(480, 4, 141, 158))
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_26)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.chk_buy_xmx = QCheckBox(self.groupBox_26)
        self.chk_buy_xmx.setObjectName(u"chk_buy_xmx")
        self.chk_buy_xmx.setMinimumSize(QSize(72, 0))
        self.chk_buy_xmx.setMaximumSize(QSize(72, 16777215))

        self.horizontalLayout_38.addWidget(self.chk_buy_xmx)

        self.edt_buy_xmx = QLineEdit(self.groupBox_26)
        self.edt_buy_xmx.setObjectName(u"edt_buy_xmx")
        self.edt_buy_xmx.setMinimumSize(QSize(0, 24))
        self.edt_buy_xmx.setMaximumSize(QSize(50, 24))

        self.horizontalLayout_38.addWidget(self.edt_buy_xmx)


        self.verticalLayout_21.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.chk_buy_bcml = QCheckBox(self.groupBox_26)
        self.chk_buy_bcml.setObjectName(u"chk_buy_bcml")
        self.chk_buy_bcml.setMinimumSize(QSize(72, 0))
        self.chk_buy_bcml.setMaximumSize(QSize(72, 16777215))

        self.horizontalLayout_39.addWidget(self.chk_buy_bcml)

        self.edt_buy_bcml = QLineEdit(self.groupBox_26)
        self.edt_buy_bcml.setObjectName(u"edt_buy_bcml")
        self.edt_buy_bcml.setMinimumSize(QSize(0, 24))
        self.edt_buy_bcml.setMaximumSize(QSize(50, 24))

        self.horizontalLayout_39.addWidget(self.edt_buy_bcml)


        self.verticalLayout_21.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.chk_buy_hslh = QCheckBox(self.groupBox_26)
        self.chk_buy_hslh.setObjectName(u"chk_buy_hslh")
        self.chk_buy_hslh.setMinimumSize(QSize(72, 0))
        self.chk_buy_hslh.setMaximumSize(QSize(72, 16777215))

        self.horizontalLayout_40.addWidget(self.chk_buy_hslh)

        self.edt_buy_hslh = QLineEdit(self.groupBox_26)
        self.edt_buy_hslh.setObjectName(u"edt_buy_hslh")
        self.edt_buy_hslh.setMinimumSize(QSize(0, 24))
        self.edt_buy_hslh.setMaximumSize(QSize(50, 24))

        self.horizontalLayout_40.addWidget(self.edt_buy_hslh)


        self.verticalLayout_21.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.chk_buy_xbz = QCheckBox(self.groupBox_26)
        self.chk_buy_xbz.setObjectName(u"chk_buy_xbz")
        self.chk_buy_xbz.setMinimumSize(QSize(72, 0))
        self.chk_buy_xbz.setMaximumSize(QSize(72, 16777215))

        self.horizontalLayout_59.addWidget(self.chk_buy_xbz)

        self.edt_buy_xbz = QLineEdit(self.groupBox_26)
        self.edt_buy_xbz.setObjectName(u"edt_buy_xbz")
        self.edt_buy_xbz.setMinimumSize(QSize(0, 24))
        self.edt_buy_xbz.setMaximumSize(QSize(50, 24))

        self.horizontalLayout_59.addWidget(self.edt_buy_xbz)


        self.verticalLayout_21.addLayout(self.horizontalLayout_59)

        self.groupBox_shout = QGroupBox(self.widget_config_other)
        self.groupBox_shout.setObjectName(u"groupBox_shout")
        self.groupBox_shout.setGeometry(QRect(274, 224, 341, 161))
        self.groupBox_shout.setCheckable(False)
        self.groupBox_shout.setChecked(False)
        self.gridLayout_32 = QGridLayout(self.groupBox_shout)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_63 = QLabel(self.groupBox_shout)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_32.addWidget(self.label_63, 1, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(197, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.spin_count_shout_frequency = QSpinBox(self.groupBox_shout)
        self.spin_count_shout_frequency.setObjectName(u"spin_count_shout_frequency")
        self.spin_count_shout_frequency.setMinimum(2)

        self.gridLayout_32.addWidget(self.spin_count_shout_frequency, 1, 1, 1, 1)

        self.edt_shout = QPlainTextEdit(self.groupBox_shout)
        self.edt_shout.setObjectName(u"edt_shout")

        self.gridLayout_32.addWidget(self.edt_shout, 0, 0, 1, 3)

        self.groupBox_15 = QGroupBox(self.widget_config_other)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(5, 4, 262, 261))
        self.groupBox_fetch_lingshi = QGroupBox(self.groupBox_15)
        self.groupBox_fetch_lingshi.setObjectName(u"groupBox_fetch_lingshi")
        self.groupBox_fetch_lingshi.setGeometry(QRect(10, 26, 242, 108))
        self.groupBox_fetch_lingshi.setCheckable(True)
        self.groupBox_fetch_lingshi.setChecked(False)
        self.gridLayout_24 = QGridLayout(self.groupBox_fetch_lingshi)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_24 = QLabel(self.groupBox_fetch_lingshi)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_24.addWidget(self.label_24, 0, 0, 1, 1)

        self.chk_fetch_lingshi1 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi1.setObjectName(u"chk_fetch_lingshi1")

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi1, 0, 1, 1, 1)

        self.chk_fetch_lingshi2 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi2.setObjectName(u"chk_fetch_lingshi2")

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi2, 0, 2, 1, 1)

        self.chk_fetch_lingshi3 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi3.setObjectName(u"chk_fetch_lingshi3")

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi3, 0, 3, 1, 1)

        self.chk_fetch_lingshi4 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi4.setObjectName(u"chk_fetch_lingshi4")
        self.chk_fetch_lingshi4.setChecked(True)

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi4, 0, 4, 1, 1)

        self.chk_fetch_lingshi5 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi5.setObjectName(u"chk_fetch_lingshi5")

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi5, 0, 5, 1, 1)

        self.chk_fetch_lingshi6 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi6.setObjectName(u"chk_fetch_lingshi6")

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi6, 1, 1, 1, 1)

        self.chk_fetch_lingshi7 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi7.setObjectName(u"chk_fetch_lingshi7")

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi7, 1, 2, 1, 1)

        self.chk_fetch_lingshi8 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi8.setObjectName(u"chk_fetch_lingshi8")

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi8, 1, 3, 1, 1)

        self.chk_fetch_lingshi9 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi9.setObjectName(u"chk_fetch_lingshi9")

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi9, 1, 4, 1, 1)

        self.chk_fetch_lingshi10 = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi10.setObjectName(u"chk_fetch_lingshi10")

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi10, 1, 5, 1, 1)

        self.label_25 = QLabel(self.groupBox_fetch_lingshi)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_24.addWidget(self.label_25, 2, 0, 1, 1)

        self.chk_fetch_lingshi_jin = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi_jin.setObjectName(u"chk_fetch_lingshi_jin")
        self.chk_fetch_lingshi_jin.setChecked(True)

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi_jin, 2, 1, 1, 1)

        self.chk_fetch_lingshi_mu = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi_mu.setObjectName(u"chk_fetch_lingshi_mu")
        self.chk_fetch_lingshi_mu.setChecked(True)

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi_mu, 2, 2, 1, 1)

        self.chk_fetch_lingshi_shui = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi_shui.setObjectName(u"chk_fetch_lingshi_shui")
        self.chk_fetch_lingshi_shui.setChecked(True)

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi_shui, 2, 3, 1, 1)

        self.chk_fetch_lingshi_huo = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi_huo.setObjectName(u"chk_fetch_lingshi_huo")
        self.chk_fetch_lingshi_huo.setChecked(True)

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi_huo, 2, 4, 1, 1)

        self.chk_fetch_lingshi_tu = QCheckBox(self.groupBox_fetch_lingshi)
        self.chk_fetch_lingshi_tu.setObjectName(u"chk_fetch_lingshi_tu")
        self.chk_fetch_lingshi_tu.setChecked(True)

        self.gridLayout_24.addWidget(self.chk_fetch_lingshi_tu, 2, 5, 1, 1)

        self.chk_fetch_hnx = QCheckBox(self.groupBox_15)
        self.chk_fetch_hnx.setObjectName(u"chk_fetch_hnx")
        self.chk_fetch_hnx.setGeometry(QRect(10, 140, 78, 20))
        self.chk_fetch_hnx.setChecked(True)
        self.chk_fetch_bai_li_xiang = QCheckBox(self.groupBox_15)
        self.chk_fetch_bai_li_xiang.setObjectName(u"chk_fetch_bai_li_xiang")
        self.chk_fetch_bai_li_xiang.setGeometry(QRect(103, 140, 56, 20))
        self.chk_fetch_bai_li_xiang.setChecked(False)
        self.chk_fetch_yao_cai = QCheckBox(self.groupBox_15)
        self.chk_fetch_yao_cai.setObjectName(u"chk_fetch_yao_cai")
        self.chk_fetch_yao_cai.setGeometry(QRect(60, 170, 45, 20))
        self.chk_fetch_za_huo = QCheckBox(self.groupBox_15)
        self.chk_fetch_za_huo.setObjectName(u"chk_fetch_za_huo")
        self.chk_fetch_za_huo.setGeometry(QRect(10, 170, 45, 20))
        self.chk_fetch_tong_bao_dai = QCheckBox(self.groupBox_15)
        self.chk_fetch_tong_bao_dai.setObjectName(u"chk_fetch_tong_bao_dai")
        self.chk_fetch_tong_bao_dai.setGeometry(QRect(170, 140, 56, 20))
        self.label_64 = QLabel(self.groupBox_15)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(165, 166, 87, 20))
        self.chk_fetch_zhu_fu_cai = QCheckBox(self.groupBox_15)
        self.chk_fetch_zhu_fu_cai.setObjectName(u"chk_fetch_zhu_fu_cai")
        self.chk_fetch_zhu_fu_cai.setGeometry(QRect(110, 170, 61, 20))
        self.chk_fetch_skill_book = QCheckBox(self.groupBox_15)
        self.chk_fetch_skill_book.setObjectName(u"chk_fetch_skill_book")
        self.chk_fetch_skill_book.setGeometry(QRect(170, 170, 61, 20))
        self.chk_fetch_xun_ma = QCheckBox(self.groupBox_15)
        self.chk_fetch_xun_ma.setObjectName(u"chk_fetch_xun_ma")
        self.chk_fetch_xun_ma.setGeometry(QRect(10, 200, 71, 20))
        self.chk_fetch_fu_ben = QCheckBox(self.groupBox_15)
        self.chk_fetch_fu_ben.setObjectName(u"chk_fetch_fu_ben")
        self.chk_fetch_fu_ben.setGeometry(QRect(90, 200, 71, 20))
        self.chk_fetch_bang_hui = QCheckBox(self.groupBox_15)
        self.chk_fetch_bang_hui.setObjectName(u"chk_fetch_bang_hui")
        self.chk_fetch_bang_hui.setGeometry(QRect(170, 200, 71, 20))
        self.chk_fetch_tang_zhu = QCheckBox(self.groupBox_15)
        self.chk_fetch_tang_zhu.setObjectName(u"chk_fetch_tang_zhu")
        self.chk_fetch_tang_zhu.setGeometry(QRect(10, 230, 81, 16))
        self.chk_fetch_cangbaotu = QCheckBox(self.groupBox_15)
        self.chk_fetch_cangbaotu.setObjectName(u"chk_fetch_cangbaotu")
        self.chk_fetch_cangbaotu.setGeometry(QRect(90, 231, 71, 16))
        self.groupBox_22 = QGroupBox(self.widget_config_other)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setGeometry(QRect(380, 4, 91, 61))
        self.gridLayout_31 = QGridLayout(self.groupBox_22)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.tedt_timer_run = QTimeEdit(self.groupBox_22)
        self.tedt_timer_run.setObjectName(u"tedt_timer_run")
        self.tedt_timer_run.setMinimumSize(QSize(0, 25))
        self.tedt_timer_run.setTime(QTime(14, 4, 0))

        self.gridLayout_31.addWidget(self.tedt_timer_run, 0, 0, 1, 1)

        self.groupBox_shout_bang_hui = QGroupBox(self.widget_config_other)
        self.groupBox_shout_bang_hui.setObjectName(u"groupBox_shout_bang_hui")
        self.groupBox_shout_bang_hui.setGeometry(QRect(5, 275, 261, 111))
        self.groupBox_shout_bang_hui.setCheckable(True)
        self.groupBox_shout_bang_hui.setChecked(True)
        self.gridLayout_34 = QGridLayout(self.groupBox_shout_bang_hui)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.edt_shout_bang_hui = QPlainTextEdit(self.groupBox_shout_bang_hui)
        self.edt_shout_bang_hui.setObjectName(u"edt_shout_bang_hui")

        self.gridLayout_34.addWidget(self.edt_shout_bang_hui, 0, 0, 1, 2)

        self.groupBox_24 = QGroupBox(self.widget_config_other)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setGeometry(QRect(380, 84, 91, 71))
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_24)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_60 = QLabel(self.groupBox_24)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_17.addWidget(self.label_60)

        self.cmb_switch_line = QComboBox(self.groupBox_24)
        self.cmb_switch_line.addItem("")
        self.cmb_switch_line.addItem("")
        self.cmb_switch_line.addItem("")
        self.cmb_switch_line.addItem("")
        self.cmb_switch_line.addItem("")
        self.cmb_switch_line.addItem("")
        self.cmb_switch_line.setObjectName(u"cmb_switch_line")
        self.cmb_switch_line.setMinimumSize(QSize(0, 0))
        self.cmb_switch_line.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_17.addWidget(self.cmb_switch_line)


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

        self.stack_widget.setCurrentIndex(2)
        self.tab_set.setCurrentIndex(0)
        self.cmb_people_bb_use_skill.setCurrentIndex(1)
        self.cmb_shuaye_map.setCurrentIndex(16)
        self.cmb_shuaye_team_map.setCurrentIndex(23)
        self.cmb_ma_zei_map1.setCurrentIndex(9)
        self.cmb_ma_zei_map2.setCurrentIndex(26)
        self.cmb_daniu_map.setCurrentIndex(0)
        self.cmb_double_time.setCurrentIndex(1)


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
        self.groupBox_people.setTitle(QCoreApplication.translate("WndMain", u"\u4eba\u7269\u6218\u6597", None))
        self.radio_fight_people_attack.setText(QCoreApplication.translate("WndMain", u"\u653b", None))
        self.radio_fight_people_defend.setText(QCoreApplication.translate("WndMain", u"\u9632", None))
        self.chk_fight_save_enemy_less.setTitle(QCoreApplication.translate("WndMain", u"\u6551\u4eba\u524d\u63d0", None))
        self.label_88.setText(QCoreApplication.translate("WndMain", u"\u62c9\u836f\u602a\u6570<", None))
        self.groupBox_people_save_people.setTitle(QCoreApplication.translate("WndMain", u"\u6218\u6597\u6551\u4eba", None))
        self.label_89.setText(QCoreApplication.translate("WndMain", u"\u8840\u5185<", None))
        self.label_90.setText(QCoreApplication.translate("WndMain", u"%", None))
        self.groupBox_people_save_bb.setTitle(QCoreApplication.translate("WndMain", u"\u6218\u6597\u6551BB", None))
        self.label_91.setText(QCoreApplication.translate("WndMain", u"\u8840\u5185<", None))
        self.label_92.setText(QCoreApplication.translate("WndMain", u"%", None))
        self.groupBox_people_use_skill.setTitle(QCoreApplication.translate("WndMain", u"\u4f7f\u7528\u6280\u80fd", None))
        self.chk_people_skill_cixue.setText(QCoreApplication.translate("WndMain", u"\u523a\u7a74F7/", None))
#if QT_CONFIG(tooltip)
        self.spin_count_skill_frequency.setToolTip(QCoreApplication.translate("WndMain", u"\u8fd9\u4e2a\u662f\u969c\u788d\u6280\u80fd\u7684\u56de\u5408\u6570\uff0c \u8bbe\u7f6e4\u5c31\u662f\u6bcf4\u56de\u5408\u4f7f\u7528\u4e00\u6b21\uff0c\u5373\u7b2c\u4e00\u56de\u5408\u7528\u4e86\uff0c\u7b2c\u4e94\u56de\u5408\u4f1a\u518d\u7528", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.spin_count_skill_frequency.setStatusTip(QCoreApplication.translate("WndMain", u"\u8fd9\u4e2a\u662f\u969c\u788d\u6280\u80fd\u7684\u56de\u5408\u6570\uff0c \u8bbe\u7f6e4\u5c31\u662f\u6bcf4\u56de\u5408\u4f7f\u7528\u4e00\u6b21\uff0c\u5373\u7b2c\u4e00\u56de\u5408\u7528\u4e86\uff0c\u7b2c\u4e94\u56de\u5408\u4f1a\u518d\u7528", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.spin_count_skill_frequency.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.chk_people_skill_huxin.setToolTip(QCoreApplication.translate("WndMain", u"\u8840\u5185\u4f4e\u4e8e60%", None))
#endif // QT_CONFIG(tooltip)
        self.chk_people_skill_huxin.setText(QCoreApplication.translate("WndMain", u"\u62a4\u5fc3F6<", None))
#if QT_CONFIG(tooltip)
        self.spin_count_huxin_percent.setToolTip(QCoreApplication.translate("WndMain", u"\u8fd9\u4e2a\u662f\u89e6\u53d1\u62a4\u5fc3\u7684\u767e\u5206\u6bd4, \u4f4e\u4e8e\u8fd9\u4e2a\u9608\u503c\u4f1a\u81ea\u52a8\u7528", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.spin_count_huxin_percent.setStatusTip(QCoreApplication.translate("WndMain", u"\u8fd9\u4e2a\u662f\u89e6\u53d1\u62a4\u5fc3\u7684\u767e\u5206\u6bd4, \u4f4e\u4e8e\u8fd9\u4e2a\u9608\u503c\u4f1a\u81ea\u52a8\u7528", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.spin_count_huxin_percent.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.chk_people_skill_single.setToolTip(QCoreApplication.translate("WndMain", u"\u6ce8\u610f\u8fd9\u4e2a\u5728 \u6781\u9650,\u722c\u5854,\u5927\u5185,\u5c60\u9f99\u65f6\u624d\u751f\u6548\n"
"\u8981\u63d0\u524d\u6309\u91d1\u6728\u571f\u6c34\u706b\u7684\u987a\u5e8f\u4f9d\u6b21\u653e\u7f6eF1-F5, \n"
"\u4f1a\u81ea\u52a8\u6839\u636eboss\u7684\u4e94\u884c\u62db\u6765\u8bbe\u7f6e\u81ea\u5df1\u7684\u514b\u602a\u62db, \u6700\u597d\u642d\u914d\u523a\u7a74, \u628aboss\u7684\u4e94\u884c\u62db\u786e\u5b9a\u4e0b\u6765", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.chk_people_skill_single.setStatusTip(QCoreApplication.translate("WndMain", u"\u6ce8\u610f\u8fd9\u4e2a\u5728 \u6781\u9650,\u722c\u5854,\u5927\u5185,\u5c60\u9f99\u65f6\u624d\u751f\u6548\\n\u8981\u63d0\u524d\u6309\u91d1\u6728\u571f\u6c34\u706b\u7684\u987a\u5e8f\u4f9d\u6b21\u653e\u7f6eF1-F5, \\n\u4f1a\u81ea\u52a8\u6839\u636eboss\u7684\u4e94\u884c\u62db\u6765\u8bbe\u7f6e\u81ea\u5df1\u7684\u514b\u602a\u62db, \u6700\u597d\u642d\u914d\u523a\u7a74, \u628aboss\u7684\u4e94\u884c\u62db\u786e\u5b9a\u4e0b\u6765", None))
#endif // QT_CONFIG(statustip)
        self.chk_people_skill_single.setText(QCoreApplication.translate("WndMain", u"\u4e94\u884c\u514b\u5236F1-F5", None))
#if QT_CONFIG(tooltip)
        self.chk_people_skill_continue_cixue.setToolTip(QCoreApplication.translate("WndMain", u"\u6ce8\u610f\u8fd9\u4e2a\u5728 \u6781\u9650,\u722c\u5854,\u5927\u5185,\u5c60\u9f99\u65f6\u624d\u751f\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.chk_people_skill_continue_cixue.setText(QCoreApplication.translate("WndMain", u"\u523a\u602a\u6570\u6bd4\u4f8b <", None))
        self.label_93.setText("")
        self.label_94.setText(QCoreApplication.translate("WndMain", u"%\u7ee7\u7eed\u523a", None))
#if QT_CONFIG(tooltip)
        self.groupBox_call_bb.setToolTip(QCoreApplication.translate("WndMain", u"\u6781\u9650 \u722c\u5854 \u5927\u5185 \u5c60\u9f99 \u65f6\u751f\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_call_bb.setTitle(QCoreApplication.translate("WndMain", u"\u5524\u51faBB ", None))
        self.label_95.setText(QCoreApplication.translate("WndMain", u"\u8840\u5185<", None))
        self.label_96.setText(QCoreApplication.translate("WndMain", u"%", None))
        self.label_97.setText(QCoreApplication.translate("WndMain", u"\u56de\u5408\u6570>", None))
        self.label_98.setText(QCoreApplication.translate("WndMain", u"BB\u540d\u5b57", None))
        self.edt_call_bb_name.setText(QCoreApplication.translate("WndMain", u"\u767d\u9f99", None))
        self.groupBox_bb.setTitle(QCoreApplication.translate("WndMain", u"BB\u6218\u6597", None))
        self.groupBox_bb_fight_defend.setTitle(QCoreApplication.translate("WndMain", u"BB\u653b\u9632", None))
        self.radioButton_14.setText(QCoreApplication.translate("WndMain", u"\u653b", None))
        self.radioButton_15.setText(QCoreApplication.translate("WndMain", u"\u9632", None))
#if QT_CONFIG(tooltip)
        self.radioButton_16.setToolTip(QCoreApplication.translate("WndMain", u"\u539f\u7406\u662f\u6bcf\u56de\u5408\u6839\u636e\u5b9d\u5b9d\u5934\u50cf\u51b3\u5b9a\u5b9d\u5b9d\u7684\u653b\u9632", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_16.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u5224\u65ad", None))
        self.groupBox_fight_bb.setTitle(QCoreApplication.translate("WndMain", u"\u8fdb\u653b\u7c7bBB", None))
        self.groupBox_fight_bb_save_people.setTitle(QCoreApplication.translate("WndMain", u"\u6218\u6597\u6551\u4eba", None))
        self.label_67.setText(QCoreApplication.translate("WndMain", u"\u8840\u5185<", None))
        self.label_68.setText(QCoreApplication.translate("WndMain", u"%", None))
        self.groupBox_fight_bb_save_bb.setTitle(QCoreApplication.translate("WndMain", u"\u6218\u6597\u6551BB", None))
        self.label_69.setText(QCoreApplication.translate("WndMain", u"\u8840\u5185<", None))
        self.label_70.setText(QCoreApplication.translate("WndMain", u"%", None))
        self.groupBox_defend_bb.setTitle(QCoreApplication.translate("WndMain", u"\u9632\u5b88\u7c7bBB", None))
        self.groupBox_defend_bb_save_people.setTitle(QCoreApplication.translate("WndMain", u"\u6218\u6597\u6551\u4eba", None))
        self.label_82.setText(QCoreApplication.translate("WndMain", u"\u8840\u5185<", None))
        self.label_83.setText(QCoreApplication.translate("WndMain", u"%", None))
        self.groupBox_defend_bb_save_bb.setTitle(QCoreApplication.translate("WndMain", u"\u6218\u6597\u6551BB", None))
        self.label_84.setText(QCoreApplication.translate("WndMain", u"\u8840\u5185<", None))
        self.label_85.setText(QCoreApplication.translate("WndMain", u"%", None))
#if QT_CONFIG(tooltip)
        self.groupBox_bb_use_skill.setToolTip(QCoreApplication.translate("WndMain", u"\u961f\u5458\u4e5f\u53ef\u4ee5\u52fe\u4e0a\u8fd9\u4e2a\uff0c\u4e0d\u662f\u6240\u6709\u4efb\u52a1\u90fd\u4f1a\u7528\uff0c\u5f53\u961f\u957f\u6267\u884c\u5230\u9ad8\u96be\u5ea6\u4efb\u52a1\u65f6\u624d\u4f1a\u7528", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_bb_use_skill.setTitle(QCoreApplication.translate("WndMain", u"\u4f7f\u7528\u6280\u80fd", None))
        self.chk_fight_bb_jzz.setText(QCoreApplication.translate("WndMain", u"\u91d1\u949f\u7f69", None))
        self.chk_fight_bb_tbs.setText(QCoreApplication.translate("WndMain", u"\u94c1\u5e03\u886b", None))
        self.chk_fight_bb_lsgs.setText(QCoreApplication.translate("WndMain", u"\u4e71\u795e\u9694\u4e16", None))
        self.chk_fight_bb_hj.setText(QCoreApplication.translate("WndMain", u"\u539a\u79ef", None))
        self.chk_fight_bb_jj.setText(QCoreApplication.translate("WndMain", u"\u6fc0\u5c06", None))
        self.chk_fight_bb_pf.setText(QCoreApplication.translate("WndMain", u"\u7834\u91dc>", None))
#if QT_CONFIG(tooltip)
        self.spin_count_fight_bb_pf_round.setToolTip(QCoreApplication.translate("WndMain", u"\u8d85\u8fc7\u8fd9\u91cc\u8bbe\u7f6e\u7684\u56de\u5408\u6570, \u7834\u91dc\u624d\u4f1a\u65bd\u653e, \u5e76\u4e14\u7834\u91dc\u53ea\u4f1a\u5728\u6253\u539a\u56db\u56de\u5408\u4ee5\u540e\u7528", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.spin_count_fight_bb_pf_round.setStatusTip(QCoreApplication.translate("WndMain", u"\u8d85\u8fc7\u8fd9\u91cc\u8bbe\u7f6e\u7684\u56de\u5408\u6570, \u7834\u91dc\u624d\u4f1a\u65bd\u653e, \u5e76\u4e14\u7834\u91dc\u53ea\u4f1a\u5728\u6253\u539a\u56db\u56de\u5408\u4ee5\u540e\u7528", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_back.setTitle(QCoreApplication.translate("WndMain", u"\u56de\u57ce", None))
        self.radio_back_dunjia_super.setText(QCoreApplication.translate("WndMain", u"\u8d85\u7ea7\u9041\u7532", None))
        self.radio_back_dunjia_small.setText(QCoreApplication.translate("WndMain", u"\u5c0f\u9041\u7532", None))
        self.radio_back_kaifeng.setText(QCoreApplication.translate("WndMain", u"\u5f00\u5c01\u7968", None))
        self.radio_back_menpai.setText(QCoreApplication.translate("WndMain", u"\u95e8\u6d3e\u7968", None))
        self.radio_back_run.setText(QCoreApplication.translate("WndMain", u"\u8dd1\u6b65", None))
        self.groupBox_go.setTitle(QCoreApplication.translate("WndMain", u"\u51fa\u57ce", None))
        self.radio_go_dunjia_super.setText(QCoreApplication.translate("WndMain", u"\u8d85\u7ea7\u9041\u7532", None))
        self.radio_go_run.setText(QCoreApplication.translate("WndMain", u"\u8dd1\u6b65", None))
#if QT_CONFIG(tooltip)
        self.groupBox_34.setToolTip(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u5224\u65ad\u6a21\u5f0f\u4e0b, \u961f\u5458\u6302\u673abb\u662f\u5426\u7528\u6280\u80fd\u662f\u6839\u636e\u961f\u957f\u4efb\u52a1\u6765\u7684, \n"
"\u6bd4\u5982\u5728\u961f\u957f\u5728\u5a01\u671b, \u961f\u5458\u7684bb\u5c31\u4e0d\u4f1a\u7528\u6280\u80fd, \n"
"\u5982\u679c\u961f\u957f\u5728\u540d\u6355, \u90a3\u961f\u5458\u7684bb\u5c31\u4f1a\u6253\u539a\u6fc0\u7834. \u5982\u679c\u4f60\u662f\u5355\u5f00\u6df7\u961f, \u8bf7\u5207\u6362\u5f3a\u5236\u4f7f\u7528", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.groupBox_34.setStatusTip(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u5224\u65ad\u6a21\u5f0f\u4e0b, \u961f\u5458\u6302\u673abb\u662f\u5426\u7528\u6280\u80fd\u662f\u6839\u636e\u961f\u957f\u4efb\u52a1\u6765\u7684, \\n\u6bd4\u5982\u5728\u961f\u957f\u5728\u5a01\u671b, \u961f\u5458\u7684bb\u5c31\u4e0d\u4f1a\u7528\u6280\u80fd, \\n\u5982\u679c\u961f\u957f\u5728\u540d\u6355, \u90a3\u961f\u5458\u7684bb\u5c31\u4f1a\u6253\u539a\u6fc0\u7834. \u5982\u679c\u4f60\u662f\u5355\u5f00\u6df7\u961f, \u8bf7\u5207\u6362\u5f3a\u5236\u4f7f\u7528", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_34.setTitle(QCoreApplication.translate("WndMain", u"\u4eba\u5ba0\u4f7f\u7528\u6280\u80fd", None))
        self.cmb_people_bb_use_skill.setItemText(0, QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u5224\u65ad", None))
        self.cmb_people_bb_use_skill.setItemText(1, QCoreApplication.translate("WndMain", u"\u5f3a\u5236\u4f7f\u7528", None))

#if QT_CONFIG(tooltip)
        self.cmb_people_bb_use_skill.setToolTip(QCoreApplication.translate("WndMain", u"\u5982\u679c\u4f60\u662f\u5355\u5f00\u6df7\u961f, \u8bf7\u5207\u6362\u5f3a\u5236\u4f7f\u7528\n"
"\u81ea\u52a8\u5224\u65ad\u6a21\u5f0f\u4e0b, \u961f\u5458\u6302\u673abb\u662f\u5426\u7528\u6280\u80fd\u662f\u6839\u636e\u961f\u957f\u4efb\u52a1\u6765\u7684, \n"
"\u6bd4\u5982\u5728\u961f\u957f\u5728\u5a01\u671b, \u961f\u5458\u7684bb\u5c31\u4e0d\u4f1a\u7528\u6280\u80fd, \n"
"\u5982\u679c\u961f\u957f\u5728\u540d\u6355, \u90a3\u961f\u5458\u7684bb\u5c31\u4f1a\u6253\u539a\u6fc0\u7834 ", None))
#endif // QT_CONFIG(tooltip)
        self.cmb_people_bb_use_skill.setCurrentText(QCoreApplication.translate("WndMain", u"\u5f3a\u5236\u4f7f\u7528", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("WndMain", u"\u6218\u540e", None))
        self.chk_people_switch_primary_bb.setText(QCoreApplication.translate("WndMain", u"\u5207\u9996\u53d1\u5ba0", None))
        self.chk_after_fight_people_supply.setText(QCoreApplication.translate("WndMain", u"\u8865\u5145\u8840\u5185<", None))
        self.label_87.setText(QCoreApplication.translate("WndMain", u"%", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_basic), QCoreApplication.translate("WndMain", u"\u57fa\u672c\u914d\u7f6e", None))
        self.groupBox_ji_xian.setTitle(QCoreApplication.translate("WndMain", u"\u6781\u9650\u6311\u6218", None))
        self.label_19.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
        self.radioButton.setText(QCoreApplication.translate("WndMain", u"\u5185", None))
        self.radioButton_2.setText(QCoreApplication.translate("WndMain", u"\u5916", None))
        self.chk_ji_xian_fail_stop.setText(QCoreApplication.translate("WndMain", u"\u5931\u8d25\u4e00\u6b21\u7ec8\u6b62", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("WndMain", u"\u5e08\u95e8", None))
        self.chk_shi_men_forever.setText(QCoreApplication.translate("WndMain", u"\u65e0\u9650\u505a", None))
        self.groupBox_shi_men_task_thing.setTitle(QCoreApplication.translate("WndMain", u"\u4efb\u52a1\u7269\u54c1", None))
        self.radioButton_12.setText(QCoreApplication.translate("WndMain", u"\u80cc\u5305\u81ea\u5907", None))
#if QT_CONFIG(tooltip)
        self.radioButton_13.setToolTip(QCoreApplication.translate("WndMain", u"\u628a\u6742\u8d27\u90fd\u653e\u5230", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_13.setText(QCoreApplication.translate("WndMain", u"\u95e8\u6d3e\u4ed3\u5e93", None))
#if QT_CONFIG(tooltip)
        self.groupBox_27.setToolTip(QCoreApplication.translate("WndMain", u"\u8f93\u5165\u6846\u586b\u63a5\u8d27\u4eba\uff0c\u4e0d\u586b\u7684\u8bdd\uff0c\u8be5\u7c7b\u7269\u54c1\u4f1a\u8d70\u6e05\u5305\u7684\u6d41\u7a0b", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_27.setTitle(QCoreApplication.translate("WndMain", u"\u4ea4\u63a5\u8d27", None))
        self.label_61.setText(QCoreApplication.translate("WndMain", u"\u4ea4\u63a5\u4f4d\u7f6e", None))
        self.cmb_deliver_pos.setItemText(0, QCoreApplication.translate("WndMain", u"\u5f00\u5c01\u4e00", None))
        self.cmb_deliver_pos.setItemText(1, QCoreApplication.translate("WndMain", u"\u5f00\u5c01\u4e8c", None))
        self.cmb_deliver_pos.setItemText(2, QCoreApplication.translate("WndMain", u"\u5f00\u5c01\u4e09", None))
        self.cmb_deliver_pos.setItemText(3, QCoreApplication.translate("WndMain", u"\u5f00\u5c01\u56db", None))

        self.chk_deliver_banghui.setText(QCoreApplication.translate("WndMain", u"\u8dd1\u5e2e\u7269\u54c1", None))
        self.edt_deliver_banghui.setPlaceholderText(QCoreApplication.translate("WndMain", u"\u63a5\u8d27\u4eba\u540d\u5b57", None))
        self.chk_deliver_yao_cai.setText(QCoreApplication.translate("WndMain", u"\u836f       \u6750", None))
        self.edt_deliver_yao_cai.setPlaceholderText(QCoreApplication.translate("WndMain", u"\u63a5\u8d27\u4eba\u540d\u5b57", None))
        self.chk_deliver_zhu_fu_cai.setText(QCoreApplication.translate("WndMain", u"\u4e3b  \u8f85  \u6750", None))
        self.edt_deliver_zhu_fu_cai.setPlaceholderText(QCoreApplication.translate("WndMain", u"\u63a5\u8d27\u4eba\u540d\u5b57", None))
        self.chk_deliver_za_huo.setText(QCoreApplication.translate("WndMain", u"\u6742       \u8d27", None))
        self.edt_deliver_za_huo.setPlaceholderText(QCoreApplication.translate("WndMain", u"\u63a5\u8d27\u4eba\u540d\u5b57", None))
        self.chk_deliver_bb_skill_book.setText(QCoreApplication.translate("WndMain", u"\u6280  \u80fd  \u4e66", None))
        self.edt_deliver_bb_skill_book.setPlaceholderText(QCoreApplication.translate("WndMain", u"\u63a5\u8d27\u4eba\u540d\u5b57", None))
        self.chk_deliver_ling_shi.setText(QCoreApplication.translate("WndMain", u"\u7075       \u77f3", None))
        self.edt_deliver_ling_shi.setPlaceholderText(QCoreApplication.translate("WndMain", u"\u63a5\u8d27\u4eba\u540d\u5b57", None))
        self.chk_deliver_fu_ben.setText(QCoreApplication.translate("WndMain", u"\u526f\u672c\u4ea7\u51fa", None))
        self.edt_deliver_fu_ben.setPlaceholderText(QCoreApplication.translate("WndMain", u"\u63a5\u8d27\u4eba\u540d\u5b57", None))
        self.chk_deliver_cangbaotu.setText(QCoreApplication.translate("WndMain", u"\u85cf  \u5b9d  \u56fe", None))
        self.edt_deliver_cangbaotu.setPlaceholderText(QCoreApplication.translate("WndMain", u"\u63a5\u8d27\u4eba\u540d\u5b57", None))
#if QT_CONFIG(tooltip)
        self.groupBox_9.setToolTip(QCoreApplication.translate("WndMain", u"\u4f1a\u81ea\u52a8\u5356\u6389\u7bb1\u5b50\uff0c\u88c5\u5907\uff0c \u4e22\u5f03\u7cfb\u9b42\u73e0\uff0c\u5783\u573e\u82b1\u7b49\u7269\u54c1\uff0c \u5f88\u591a\u4e0d\u9700\u8981\u9009\u62e9\u6b63\u5e38\u4eba\u90fd\u4f1a\u5b58\u7684\u4e1c\u897f\u6ca1\u5217\u51fa\u6765", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_9.setTitle(QCoreApplication.translate("WndMain", u"\u6e05\u7406\u80cc\u5305", None))
        self.groupBox_qing_li_tongbaodai.setTitle(QCoreApplication.translate("WndMain", u"\u901a\u5b9d\u888b", None))
        self.radio_clean_tongbaodai_store.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_tongbaodai_use.setText(QCoreApplication.translate("WndMain", u"\u7528", None))
        self.groupBox_qing_li_yaocai.setTitle(QCoreApplication.translate("WndMain", u"\u836f\u6750", None))
        self.radio_clean_drug_store.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_drug_sell.setText(QCoreApplication.translate("WndMain", u"\u5356", None))
        self.groupBox_qing_li_sixiang.setTitle(QCoreApplication.translate("WndMain", u"\u56db\u8c61\u6d17\u7ec3\u4e39", None))
        self.radio_clean_sixiang_store.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_sixiang_use.setText(QCoreApplication.translate("WndMain", u"\u7528", None))
        self.groupBox_qing_li_zhucai.setTitle(QCoreApplication.translate("WndMain", u"\u4e3b\u6750", None))
        self.radio_clean_zhucai_store.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_zhucai_sell.setText(QCoreApplication.translate("WndMain", u"\u5356", None))
        self.groupBox_qing_li_fucai.setTitle(QCoreApplication.translate("WndMain", u"\u8f85\u6750", None))
        self.radio_clean_fucai_store.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_fucai_sell.setText(QCoreApplication.translate("WndMain", u"\u5356", None))
#if QT_CONFIG(tooltip)
        self.groupBox_qing_li_bailixiang.setToolTip(QCoreApplication.translate("WndMain", u"\u5982\u72d7\u76ae\uff0c\u5f00\u5c71\u9524\uff0c\u5c0f\u9f99\u5973\u7684\u753b\u50cf\u7b49", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_qing_li_bailixiang.setTitle(QCoreApplication.translate("WndMain", u"\u767e\u91cc\u9999", None))
        self.radio_clean_bailixiang_store.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_bailixiang_throw.setText(QCoreApplication.translate("WndMain", u"\u4e22", None))
        self.groupBox_qing_li_lingshi.setTitle(QCoreApplication.translate("WndMain", u"\u7075\u77f3", None))
        self.radio_clean_fucai_store_2.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_fucai_sell_2.setText(QCoreApplication.translate("WndMain", u"\u5356", None))
#if QT_CONFIG(tooltip)
        self.groupBox_qing_li_zahuo.setToolTip(QCoreApplication.translate("WndMain", u"\u5982\u72d7\u76ae\uff0c\u5f00\u5c71\u9524\uff0c\u5c0f\u9f99\u5973\u7684\u753b\u50cf\u7b49", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_qing_li_zahuo.setTitle(QCoreApplication.translate("WndMain", u"\u6742\u8d27", None))
        self.radio_clean_zahuo_store.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_zahuo_sell.setText(QCoreApplication.translate("WndMain", u"\u5356", None))
        self.groupBox_qing_cangbaotu.setTitle(QCoreApplication.translate("WndMain", u"\u85cf\u5b9d\u56fe", None))
        self.radio_clean_zhuqian_store_2.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_zhuqian_throw_2.setText(QCoreApplication.translate("WndMain", u"\u4e22", None))
        self.groupBox_qing_li_xun_ma.setTitle(QCoreApplication.translate("WndMain", u"\u9a6f\u9a6c\u6750\u6599", None))
        self.radio_clean_zhucai_store_2.setText(QCoreApplication.translate("WndMain", u"\u5b58", None))
        self.radio_clean_zhucai_sell_2.setText(QCoreApplication.translate("WndMain", u"\u5356", None))
        self.groupBox.setTitle(QCoreApplication.translate("WndMain", u"\u6302\u673a\u5237\u91ce", None))
        self.label_4.setText(QCoreApplication.translate("WndMain", u"\u5730\u56fe", None))
        self.cmb_shuaye_map.setItemText(0, QCoreApplication.translate("WndMain", u"\u5f53\u524d\u5730\u56fe", None))
        self.cmb_shuaye_map.setItemText(1, QCoreApplication.translate("WndMain", u"\u6843\u82b1\u6797", None))
        self.cmb_shuaye_map.setItemText(2, QCoreApplication.translate("WndMain", u"\u6843\u82b1\u6ee9", None))
        self.cmb_shuaye_map.setItemText(3, QCoreApplication.translate("WndMain", u"\u6709\u5ea7\u5c71", None))
        self.cmb_shuaye_map.setItemText(4, QCoreApplication.translate("WndMain", u"\u7edd\u60c5\u8c37", None))
        self.cmb_shuaye_map.setItemText(5, QCoreApplication.translate("WndMain", u"\u5341\u5b57\u5761", None))
        self.cmb_shuaye_map.setItemText(6, QCoreApplication.translate("WndMain", u"\u738b\u5c4b\u5c71", None))
        self.cmb_shuaye_map.setItemText(7, QCoreApplication.translate("WndMain", u"\u901a\u5403\u5c9b", None))
        self.cmb_shuaye_map.setItemText(8, QCoreApplication.translate("WndMain", u"\u795e\u9f99\u5c9b", None))
        self.cmb_shuaye_map.setItemText(9, QCoreApplication.translate("WndMain", u"\u9f99\u95e8", None))
        self.cmb_shuaye_map.setItemText(10, QCoreApplication.translate("WndMain", u"\u7ec8\u5357\u5c71", None))
        self.cmb_shuaye_map.setItemText(11, QCoreApplication.translate("WndMain", u"\u767d\u9a7c\u5c71", None))
        self.cmb_shuaye_map.setItemText(12, QCoreApplication.translate("WndMain", u"\u78a7\u5cf0\u5ce1", None))
        self.cmb_shuaye_map.setItemText(13, QCoreApplication.translate("WndMain", u"\u6076\u4eba\u8c37", None))
        self.cmb_shuaye_map.setItemText(14, QCoreApplication.translate("WndMain", u"\u65e0\u91cf\u5c71", None))
        self.cmb_shuaye_map.setItemText(15, QCoreApplication.translate("WndMain", u"\u5937\u5dde\u5c9b", None))
        self.cmb_shuaye_map.setItemText(16, QCoreApplication.translate("WndMain", u"\u96c1\u95e8\u5173\u5916", None))
        self.cmb_shuaye_map.setItemText(17, QCoreApplication.translate("WndMain", u"\u5927\u8349\u539f", None))
        self.cmb_shuaye_map.setItemText(18, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e00\u5c42", None))
        self.cmb_shuaye_map.setItemText(19, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e8c\u5c42", None))
        self.cmb_shuaye_map.setItemText(20, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e09\u5c42", None))
        self.cmb_shuaye_map.setItemText(21, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e00\u5c42", None))
        self.cmb_shuaye_map.setItemText(22, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e8c\u5c42", None))
        self.cmb_shuaye_map.setItemText(23, QCoreApplication.translate("WndMain", u"\u7384\u971c\u6d45\u6ee9", None))
        self.cmb_shuaye_map.setItemText(24, QCoreApplication.translate("WndMain", u"\u91d1\u98ce\u5c71\u9053", None))
        self.cmb_shuaye_map.setItemText(25, QCoreApplication.translate("WndMain", u"\u8d64\u971e\u6e21\u53e3", None))
        self.cmb_shuaye_map.setItemText(26, QCoreApplication.translate("WndMain", u"\u9752\u4e91\u5e7d\u8c37", None))
        self.cmb_shuaye_map.setItemText(27, QCoreApplication.translate("WndMain", u"\u71d5\u5b50\u575e", None))
        self.cmb_shuaye_map.setItemText(28, QCoreApplication.translate("WndMain", u"\u697c\u5170\u53e4\u9053", None))
        self.cmb_shuaye_map.setItemText(29, QCoreApplication.translate("WndMain", u"\u7389\u95e8\u5173", None))
        self.cmb_shuaye_map.setItemText(30, QCoreApplication.translate("WndMain", u"\u843d\u65e5\u8c37", None))
        self.cmb_shuaye_map.setItemText(31, QCoreApplication.translate("WndMain", u"\u65a1\u96be\u6cb3", None))

        self.cmb_shuaye_map.setCurrentText(QCoreApplication.translate("WndMain", u"\u96c1\u95e8\u5173\u5916", None))
        self.label_5.setText(QCoreApplication.translate("WndMain", u"\u65f6\u957f", None))
#if QT_CONFIG(tooltip)
        self.edt_shuaye_time.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-99999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_shuaye_time.setText(QCoreApplication.translate("WndMain", u"600", None))
        self.label_6.setText(QCoreApplication.translate("WndMain", u"\u5206\u949f", None))
        self.groupBox_time_stop_shua_ye.setTitle(QCoreApplication.translate("WndMain", u"\u5b9a\u65f6\u7ed3\u675f", None))
        self.tedt_timer_shua_ye.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.chk_shuaye_deliver.setText(QCoreApplication.translate("WndMain", u"\u4f18\u5148\u4ea4\u8d27", None))
        self.chk_shuaye_qingli.setText(QCoreApplication.translate("WndMain", u"\u6e05\u7406\u80cc\u5305", None))
        self.chk_shuaye_fix_bb.setText(QCoreApplication.translate("WndMain", u"\u6559\u5316\u4fee\u7406", None))
        self.chk_shuaye_terse_bb.setText(QCoreApplication.translate("WndMain", u"\u7cbe\u70bc\u968f\u4ece", None))
        self.chk_shuaye_xun_ma.setText(QCoreApplication.translate("WndMain", u"\u7f16\u9a6f\u9a6c\u7ef3", None))
        self.chk_shuaye_catch_bb.setText(QCoreApplication.translate("WndMain", u"\u6536\u670d\u9e92\u9e9f", None))
        self.chk_shuaye_fight_e_ren.setText(QCoreApplication.translate("WndMain", u"\u6253\u6076\u4eba\u699c", None))
        self.chk_shuaye_fight_yan.setText(QCoreApplication.translate("WndMain", u"\u5237\u71d5\u5357\u5929", None))
        self.chk_shuaye_che_tui.setText(QCoreApplication.translate("WndMain", u"\u65e0\u5219\u64a4\u9000", None))
        self.chk_shuaye_qiandao.setText(QCoreApplication.translate("WndMain", u"\u7b7e\u5230\u7965\u745e", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("WndMain", u"\u6311\u6218\u5802\u4e3b", None))
        self.label_65.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
        self.cmb_tang_zhu.setItemText(0, QCoreApplication.translate("WndMain", u"\u836f\u795e", None))
        self.cmb_tang_zhu.setItemText(1, QCoreApplication.translate("WndMain", u"\u5929\u5de5", None))
        self.cmb_tang_zhu.setItemText(2, QCoreApplication.translate("WndMain", u"\u62a4\u536b", None))
        self.cmb_tang_zhu.setItemText(3, QCoreApplication.translate("WndMain", u"\u7cbe\u70bc", None))
        self.cmb_tang_zhu.setItemText(4, QCoreApplication.translate("WndMain", u"\u767e\u7145", None))
        self.cmb_tang_zhu.setItemText(5, QCoreApplication.translate("WndMain", u"\u9526\u8863", None))

        self.groupBox_zheng_zhan.setTitle(QCoreApplication.translate("WndMain", u"\u5f81\u6218\u6c5f\u6e56", None))
        self.radioButton_3.setText(QCoreApplication.translate("WndMain", u"\u7ee7\u7eed", None))
        self.radioButton_4.setText(QCoreApplication.translate("WndMain", u"\u4e0b\u4e00\u5173", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("WndMain", u"\u5e2e\u4f1a\u6316\u77ff", None))
        self.label_66.setText(QCoreApplication.translate("WndMain", u"\u9504\u5934", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("WndMain", u"\u56db\u8c61\u8dd1\u73af", None))
        self.label_20.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("WndMain", u"\u5dc5\u5cf0\u4e4b\u5854", None))
        self.label_16.setText(QCoreApplication.translate("WndMain", u"\u5c42\u6570", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_single), QCoreApplication.translate("WndMain", u"\u5355\u4eba\u914d\u7f6e", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5e73\u4e71", None))
        self.label_3.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
        self.groupBox_time_stop_ping_luan.setTitle(QCoreApplication.translate("WndMain", u"\u5b9a\u65f6\u7ed3\u675f", None))
        self.tedt_timer_ping_luan.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5a01\u671b", None))
        self.label_2.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
        self.groupBox_time_stop_wei_wang.setTitle(QCoreApplication.translate("WndMain", u"\u5b9a\u65f6\u7ed3\u675f", None))
        self.tedt_timer_wei_wang.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5237\u91ce", None))
        self.cmb_shuaye_team_map.setItemText(0, QCoreApplication.translate("WndMain", u"\u5f53\u524d\u5730\u56fe", None))
        self.cmb_shuaye_team_map.setItemText(1, QCoreApplication.translate("WndMain", u"\u6843\u82b1\u6797", None))
        self.cmb_shuaye_team_map.setItemText(2, QCoreApplication.translate("WndMain", u"\u6843\u82b1\u6ee9", None))
        self.cmb_shuaye_team_map.setItemText(3, QCoreApplication.translate("WndMain", u"\u6709\u5ea7\u5c71", None))
        self.cmb_shuaye_team_map.setItemText(4, QCoreApplication.translate("WndMain", u"\u7edd\u60c5\u8c37", None))
        self.cmb_shuaye_team_map.setItemText(5, QCoreApplication.translate("WndMain", u"\u5341\u5b57\u5761", None))
        self.cmb_shuaye_team_map.setItemText(6, QCoreApplication.translate("WndMain", u"\u738b\u5c4b\u5c71", None))
        self.cmb_shuaye_team_map.setItemText(7, QCoreApplication.translate("WndMain", u"\u901a\u5403\u5c9b", None))
        self.cmb_shuaye_team_map.setItemText(8, QCoreApplication.translate("WndMain", u"\u795e\u9f99\u5c9b", None))
        self.cmb_shuaye_team_map.setItemText(9, QCoreApplication.translate("WndMain", u"\u9f99\u95e8", None))
        self.cmb_shuaye_team_map.setItemText(10, QCoreApplication.translate("WndMain", u"\u7ec8\u5357\u5c71", None))
        self.cmb_shuaye_team_map.setItemText(11, QCoreApplication.translate("WndMain", u"\u767d\u9a7c\u5c71", None))
        self.cmb_shuaye_team_map.setItemText(12, QCoreApplication.translate("WndMain", u"\u78a7\u5cf0\u5ce1", None))
        self.cmb_shuaye_team_map.setItemText(13, QCoreApplication.translate("WndMain", u"\u6076\u4eba\u8c37", None))
        self.cmb_shuaye_team_map.setItemText(14, QCoreApplication.translate("WndMain", u"\u65e0\u91cf\u5c71", None))
        self.cmb_shuaye_team_map.setItemText(15, QCoreApplication.translate("WndMain", u"\u5937\u5dde\u5c9b", None))
        self.cmb_shuaye_team_map.setItemText(16, QCoreApplication.translate("WndMain", u"\u96c1\u95e8\u5173\u5916", None))
        self.cmb_shuaye_team_map.setItemText(17, QCoreApplication.translate("WndMain", u"\u5927\u8349\u539f", None))
        self.cmb_shuaye_team_map.setItemText(18, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e00\u5c42", None))
        self.cmb_shuaye_team_map.setItemText(19, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e8c\u5c42", None))
        self.cmb_shuaye_team_map.setItemText(20, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e09\u5c42", None))
        self.cmb_shuaye_team_map.setItemText(21, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e00\u5c42", None))
        self.cmb_shuaye_team_map.setItemText(22, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e8c\u5c42", None))
        self.cmb_shuaye_team_map.setItemText(23, QCoreApplication.translate("WndMain", u"\u7384\u971c\u6d45\u6ee9", None))
        self.cmb_shuaye_team_map.setItemText(24, QCoreApplication.translate("WndMain", u"\u91d1\u98ce\u5c71\u9053", None))
        self.cmb_shuaye_team_map.setItemText(25, QCoreApplication.translate("WndMain", u"\u8d64\u971e\u6e21\u53e3", None))
        self.cmb_shuaye_team_map.setItemText(26, QCoreApplication.translate("WndMain", u"\u9752\u4e91\u5e7d\u8c37", None))
        self.cmb_shuaye_team_map.setItemText(27, QCoreApplication.translate("WndMain", u"\u71d5\u5b50\u575e", None))
        self.cmb_shuaye_team_map.setItemText(28, QCoreApplication.translate("WndMain", u"\u697c\u5170\u53e4\u9053", None))
        self.cmb_shuaye_team_map.setItemText(29, QCoreApplication.translate("WndMain", u"\u7389\u95e8\u5173", None))
        self.cmb_shuaye_team_map.setItemText(30, QCoreApplication.translate("WndMain", u"\u843d\u65e5\u8c37", None))
        self.cmb_shuaye_team_map.setItemText(31, QCoreApplication.translate("WndMain", u"\u65a1\u96be\u6cb3", None))

        self.cmb_shuaye_team_map.setCurrentText(QCoreApplication.translate("WndMain", u"\u7384\u971c\u6d45\u6ee9", None))
        self.chk_shuaye_team_fix_bb.setText(QCoreApplication.translate("WndMain", u"\u4fee\u7406\u5fe0\u8bda", None))
        self.groupBox_time_stop_shua_ye_team.setTitle(QCoreApplication.translate("WndMain", u"\u5b9a\u65f6\u7ed3\u675f", None))
        self.tedt_timer_shua_ye_team.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.label_22.setText("")
#if QT_CONFIG(tooltip)
        self.edt_shuaye_team_time.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-99999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_shuaye_team_time.setText(QCoreApplication.translate("WndMain", u"1000", None))
        self.label_48.setText(QCoreApplication.translate("WndMain", u"\u5206\u949f", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("WndMain", u"\u6316\u5b9d\u9a6c\u8d3c", None))
        self.label.setText(QCoreApplication.translate("WndMain", u"\u6253\u9a6c\u8d3c\u8303\u56f4", None))
        self.cmb_ma_zei_map1.setItemText(0, QCoreApplication.translate("WndMain", u"\u6709\u5ea7\u5c71", None))
        self.cmb_ma_zei_map1.setItemText(1, QCoreApplication.translate("WndMain", u"\u7edd\u60c5\u8c37", None))
        self.cmb_ma_zei_map1.setItemText(2, QCoreApplication.translate("WndMain", u"\u5341\u5b57\u5761", None))
        self.cmb_ma_zei_map1.setItemText(3, QCoreApplication.translate("WndMain", u"\u738b\u5c4b\u5c71", None))
        self.cmb_ma_zei_map1.setItemText(4, QCoreApplication.translate("WndMain", u"\u901a\u5403\u5c9b", None))
        self.cmb_ma_zei_map1.setItemText(5, QCoreApplication.translate("WndMain", u"\u795e\u9f99\u5c9b", None))
        self.cmb_ma_zei_map1.setItemText(6, QCoreApplication.translate("WndMain", u"\u9f99\u95e8", None))
        self.cmb_ma_zei_map1.setItemText(7, QCoreApplication.translate("WndMain", u"\u7ec8\u5357\u5c71", None))
        self.cmb_ma_zei_map1.setItemText(8, QCoreApplication.translate("WndMain", u"\u767d\u9a7c\u5c71", None))
        self.cmb_ma_zei_map1.setItemText(9, QCoreApplication.translate("WndMain", u"\u78a7\u5cf0\u5ce1", None))
        self.cmb_ma_zei_map1.setItemText(10, QCoreApplication.translate("WndMain", u"\u6076\u4eba\u8c37", None))
        self.cmb_ma_zei_map1.setItemText(11, QCoreApplication.translate("WndMain", u"\u65e0\u91cf\u5c71", None))
        self.cmb_ma_zei_map1.setItemText(12, QCoreApplication.translate("WndMain", u"\u5937\u5dde\u5c9b", None))
        self.cmb_ma_zei_map1.setItemText(13, QCoreApplication.translate("WndMain", u"\u96c1\u95e8\u5173\u5916", None))
        self.cmb_ma_zei_map1.setItemText(14, QCoreApplication.translate("WndMain", u"\u5927\u8349\u539f", None))
        self.cmb_ma_zei_map1.setItemText(15, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e00\u5c42", None))
        self.cmb_ma_zei_map1.setItemText(16, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e8c\u5c42", None))
        self.cmb_ma_zei_map1.setItemText(17, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e09\u5c42", None))
        self.cmb_ma_zei_map1.setItemText(18, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e00\u5c42", None))
        self.cmb_ma_zei_map1.setItemText(19, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e8c\u5c42", None))
        self.cmb_ma_zei_map1.setItemText(20, QCoreApplication.translate("WndMain", u"\u7384\u971c\u6d45\u6ee9", None))
        self.cmb_ma_zei_map1.setItemText(21, QCoreApplication.translate("WndMain", u"\u91d1\u98ce\u5c71\u9053", None))
        self.cmb_ma_zei_map1.setItemText(22, QCoreApplication.translate("WndMain", u"\u8d64\u971e\u6e21\u53e3", None))
        self.cmb_ma_zei_map1.setItemText(23, QCoreApplication.translate("WndMain", u"\u9752\u4e91\u5e7d\u8c37", None))

        self.cmb_ma_zei_map1.setCurrentText(QCoreApplication.translate("WndMain", u"\u78a7\u5cf0\u5ce1", None))
        self.label_7.setText(QCoreApplication.translate("WndMain", u"\u4e00\u4e00", None))
        self.cmb_ma_zei_map2.setItemText(0, QCoreApplication.translate("WndMain", u"\u6709\u5ea7\u5c71", None))
        self.cmb_ma_zei_map2.setItemText(1, QCoreApplication.translate("WndMain", u"\u7edd\u60c5\u8c37", None))
        self.cmb_ma_zei_map2.setItemText(2, QCoreApplication.translate("WndMain", u"\u5341\u5b57\u5761", None))
        self.cmb_ma_zei_map2.setItemText(3, QCoreApplication.translate("WndMain", u"\u738b\u5c4b\u5c71", None))
        self.cmb_ma_zei_map2.setItemText(4, QCoreApplication.translate("WndMain", u"\u901a\u5403\u5c9b", None))
        self.cmb_ma_zei_map2.setItemText(5, QCoreApplication.translate("WndMain", u"\u795e\u9f99\u5c9b", None))
        self.cmb_ma_zei_map2.setItemText(6, QCoreApplication.translate("WndMain", u"\u9f99\u95e8", None))
        self.cmb_ma_zei_map2.setItemText(7, QCoreApplication.translate("WndMain", u"\u7ec8\u5357\u5c71", None))
        self.cmb_ma_zei_map2.setItemText(8, QCoreApplication.translate("WndMain", u"\u767d\u9a7c\u5c71", None))
        self.cmb_ma_zei_map2.setItemText(9, QCoreApplication.translate("WndMain", u"\u78a7\u5cf0\u5ce1", None))
        self.cmb_ma_zei_map2.setItemText(10, QCoreApplication.translate("WndMain", u"\u6076\u4eba\u8c37", None))
        self.cmb_ma_zei_map2.setItemText(11, QCoreApplication.translate("WndMain", u"\u65e0\u91cf\u5c71", None))
        self.cmb_ma_zei_map2.setItemText(12, QCoreApplication.translate("WndMain", u"\u5937\u5dde\u5c9b", None))
        self.cmb_ma_zei_map2.setItemText(13, QCoreApplication.translate("WndMain", u"\u96c1\u95e8\u5173\u5916", None))
        self.cmb_ma_zei_map2.setItemText(14, QCoreApplication.translate("WndMain", u"\u5927\u8349\u539f", None))
        self.cmb_ma_zei_map2.setItemText(15, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e00\u5c42", None))
        self.cmb_ma_zei_map2.setItemText(16, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e8c\u5c42", None))
        self.cmb_ma_zei_map2.setItemText(17, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e09\u5c42", None))
        self.cmb_ma_zei_map2.setItemText(18, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e00\u5c42", None))
        self.cmb_ma_zei_map2.setItemText(19, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e8c\u5c42", None))
        self.cmb_ma_zei_map2.setItemText(20, QCoreApplication.translate("WndMain", u"\u7384\u971c\u6d45\u6ee9", None))
        self.cmb_ma_zei_map2.setItemText(21, QCoreApplication.translate("WndMain", u"\u91d1\u98ce\u5c71\u9053", None))
        self.cmb_ma_zei_map2.setItemText(22, QCoreApplication.translate("WndMain", u"\u8d64\u971e\u6e21\u53e3", None))
        self.cmb_ma_zei_map2.setItemText(23, QCoreApplication.translate("WndMain", u"\u9752\u4e91\u5e7d\u8c37", None))
        self.cmb_ma_zei_map2.setItemText(24, QCoreApplication.translate("WndMain", u"\u71d5\u5b50\u575e", None))
        self.cmb_ma_zei_map2.setItemText(25, QCoreApplication.translate("WndMain", u"\u697c\u5170\u53e4\u9053", None))
        self.cmb_ma_zei_map2.setItemText(26, QCoreApplication.translate("WndMain", u"\u7389\u95e8\u5173", None))

        self.cmb_ma_zei_map2.setCurrentText(QCoreApplication.translate("WndMain", u"\u7389\u95e8\u5173", None))
        self.chk_ma_zei_continue.setText(QCoreApplication.translate("WndMain", u"\u6316\u5b8c\u5b9d\u56fe\u4ecd\u7ee7\u7eed\u76d1\u542c\u4e16\u754c\u9891\u9053\u9a6c\u8d3c\u6d88\u606f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6253\u725b", None))
        self.label_18.setText(QCoreApplication.translate("WndMain", u"\u5730\u56fe", None))
        self.cmb_daniu_map.setItemText(0, QCoreApplication.translate("WndMain", u"\u5f53\u524d\u5730\u56fe", None))
        self.cmb_daniu_map.setItemText(1, QCoreApplication.translate("WndMain", u"\u6843\u82b1\u6797", None))
        self.cmb_daniu_map.setItemText(2, QCoreApplication.translate("WndMain", u"\u6843\u82b1\u6ee9", None))
        self.cmb_daniu_map.setItemText(3, QCoreApplication.translate("WndMain", u"\u6709\u5ea7\u5c71", None))
        self.cmb_daniu_map.setItemText(4, QCoreApplication.translate("WndMain", u"\u7edd\u60c5\u8c37", None))
        self.cmb_daniu_map.setItemText(5, QCoreApplication.translate("WndMain", u"\u5341\u5b57\u5761", None))
        self.cmb_daniu_map.setItemText(6, QCoreApplication.translate("WndMain", u"\u738b\u5c4b\u5c71", None))
        self.cmb_daniu_map.setItemText(7, QCoreApplication.translate("WndMain", u"\u901a\u5403\u5c9b", None))
        self.cmb_daniu_map.setItemText(8, QCoreApplication.translate("WndMain", u"\u795e\u9f99\u5c9b", None))
        self.cmb_daniu_map.setItemText(9, QCoreApplication.translate("WndMain", u"\u9f99\u95e8", None))
        self.cmb_daniu_map.setItemText(10, QCoreApplication.translate("WndMain", u"\u7ec8\u5357\u5c71", None))
        self.cmb_daniu_map.setItemText(11, QCoreApplication.translate("WndMain", u"\u767d\u9a7c\u5c71", None))
        self.cmb_daniu_map.setItemText(12, QCoreApplication.translate("WndMain", u"\u78a7\u5cf0\u5ce1", None))
        self.cmb_daniu_map.setItemText(13, QCoreApplication.translate("WndMain", u"\u6076\u4eba\u8c37", None))
        self.cmb_daniu_map.setItemText(14, QCoreApplication.translate("WndMain", u"\u65e0\u91cf\u5c71", None))
        self.cmb_daniu_map.setItemText(15, QCoreApplication.translate("WndMain", u"\u5937\u5dde\u5c9b", None))
        self.cmb_daniu_map.setItemText(16, QCoreApplication.translate("WndMain", u"\u96c1\u95e8\u5173\u5916", None))
        self.cmb_daniu_map.setItemText(17, QCoreApplication.translate("WndMain", u"\u5927\u8349\u539f", None))
        self.cmb_daniu_map.setItemText(18, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e00\u5c42", None))
        self.cmb_daniu_map.setItemText(19, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e8c\u5c42", None))
        self.cmb_daniu_map.setItemText(20, QCoreApplication.translate("WndMain", u"\u53e4\u5893\u4e09\u5c42", None))
        self.cmb_daniu_map.setItemText(21, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e00\u5c42", None))
        self.cmb_daniu_map.setItemText(22, QCoreApplication.translate("WndMain", u"\u79e6\u9675\u4e8c\u5c42", None))
        self.cmb_daniu_map.setItemText(23, QCoreApplication.translate("WndMain", u"\u7384\u971c\u6d45\u6ee9", None))
        self.cmb_daniu_map.setItemText(24, QCoreApplication.translate("WndMain", u"\u91d1\u98ce\u5c71\u9053", None))
        self.cmb_daniu_map.setItemText(25, QCoreApplication.translate("WndMain", u"\u8d64\u971e\u6e21\u53e3", None))
        self.cmb_daniu_map.setItemText(26, QCoreApplication.translate("WndMain", u"\u9752\u4e91\u5e7d\u8c37", None))
        self.cmb_daniu_map.setItemText(27, QCoreApplication.translate("WndMain", u"\u71d5\u5b50\u575e", None))
        self.cmb_daniu_map.setItemText(28, QCoreApplication.translate("WndMain", u"\u697c\u5170\u53e4\u9053", None))
        self.cmb_daniu_map.setItemText(29, QCoreApplication.translate("WndMain", u"\u7389\u95e8\u5173", None))
        self.cmb_daniu_map.setItemText(30, QCoreApplication.translate("WndMain", u"\u843d\u65e5\u8c37", None))
        self.cmb_daniu_map.setItemText(31, QCoreApplication.translate("WndMain", u"\u65a1\u96be\u6cb3", None))

        self.cmb_daniu_map.setCurrentText(QCoreApplication.translate("WndMain", u"\u5f53\u524d\u5730\u56fe", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("WndMain", u"\u9886\u53d6\u53cc\u500d", None))
        self.label_17.setText(QCoreApplication.translate("WndMain", u"\u65f6\u95f4", None))
        self.cmb_double_time.setItemText(0, QCoreApplication.translate("WndMain", u"1\u5c0f\u65f6", None))
        self.cmb_double_time.setItemText(1, QCoreApplication.translate("WndMain", u"2\u5c0f\u65f6", None))
        self.cmb_double_time.setItemText(2, QCoreApplication.translate("WndMain", u"4\u5c0f\u65f6", None))

        self.groupBox_16.setTitle(QCoreApplication.translate("WndMain", u"\u968f\u4ece\u526f\u672c", None))
        self.groupBox_fuben_bb90.setTitle(QCoreApplication.translate("WndMain", u"90\u7ea7", None))
        self.radio_bb_fuben_hsrm.setText(QCoreApplication.translate("WndMain", u"\u6d3b\u6b7b\u4eba\u5893", None))
        self.radio_bb_fuben_zpwk.setText(QCoreApplication.translate("WndMain", u"\u667a\u7834\u502d\u5bc7", None))
        self.radio_bb_fuben_znpd.setText(QCoreApplication.translate("WndMain", u"\u7ec8\u5357\u7834\u654c", None))
        self.groupBox_fuben_bb100.setTitle(QCoreApplication.translate("WndMain", u"100\u7ea7", None))
        self.radio_bb_fuben_jzhs.setText(QCoreApplication.translate("WndMain", u"\u51b3\u6218\u534e\u5c71", None))
        self.radio_bb_fuben_dzwd.setText(QCoreApplication.translate("WndMain", u"\u5927\u6218\u6b66\u5f53", None))
        self.radio_bb_fuben_wldh.setText(QCoreApplication.translate("WndMain", u"\u6b66\u6797\u5927\u4f1a", None))
        self.groupBox_fuben_bb110.setTitle(QCoreApplication.translate("WndMain", u"110\u7ea7", None))
        self.radio_bb_fuben_wljp.setText(QCoreApplication.translate("WndMain", u"\u65e0\u91cf\u5251\u6d3e", None))
        self.radio_bb_fuben_thzq.setText(QCoreApplication.translate("WndMain", u"\u6843\u82b1\u62db\u4eb2", None))
        self.radio_bb_fuben_mzzz.setText(QCoreApplication.translate("WndMain", u"\u6885\u5e84\u4e4b\u6218", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("WndMain", u"\u4eba\u7269\u526f\u672c", None))
        self.label_26.setText(QCoreApplication.translate("WndMain", u"70\u68a6\u4e2d", None))
        self.label_28.setText(QCoreApplication.translate("WndMain", u"80\u68a6\u4e2d", None))
        self.label_29.setText(QCoreApplication.translate("WndMain", u"90\u68a6\u4e2d", None))
        self.label_30.setText(QCoreApplication.translate("WndMain", u"100\u534e\u5c71", None))
        self.label_56.setText(QCoreApplication.translate("WndMain", u"110\u4e94\u884c", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("WndMain", u"\u961f\u5458\u6302\u673a", None))
        self.chk_duiyuan_ls.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u9886\u53cc", None))
        self.chk_duiyuan_ds.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u51bb\u53cc", None))
        self.chk_duiyuan_js.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u89e3\u53cc", None))
        self.chk_duiyuan_ld.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u79bb\u961f", None))
        self.chk_duiyuan_hx.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u6362\u7ebf", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("WndMain", u"\u8d85\u7ea7\u6311\u6218", None))
        self.chk_super_chanllenge_fix_bb.setText(QCoreApplication.translate("WndMain", u"\u6362boss\u524d\u4fee\u7406BB", None))
        self.label_62.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p>\u6ce8: \u4e0b\u9762\u7684\u6570\u5b57\u4ee3\u8868\u5f3a\u5ea6, \u8f93\u51650\u5c31\u662f\u6253\u5b8c\u5f3a0, \u8f93\u5165-1\u5219\u8df3\u8fc7</p></body></html>", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("WndMain", u"\u56db\u5927\u540d\u6355", None))
        self.label_27.setText(QCoreApplication.translate("WndMain", u"\u65e0 \u60c5", None))
        self.label_31.setText(QCoreApplication.translate("WndMain", u"\u94c1 \u624b", None))
        self.label_32.setText(QCoreApplication.translate("WndMain", u"\u8ffd \u547d", None))
        self.label_33.setText(QCoreApplication.translate("WndMain", u"\u51b7 \u8840", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("WndMain", u"\u660e\u6559\u9ad8\u624b", None))
        self.label_34.setText(QCoreApplication.translate("WndMain", u"\u97e6 \u4e00 \u7b11", None))
        self.label_35.setText(QCoreApplication.translate("WndMain", u"\u8c22 \u900a", None))
        self.label_36.setText(QCoreApplication.translate("WndMain", u"\u6bb7 \u5929 \u6b63", None))
        self.label_37.setText(QCoreApplication.translate("WndMain", u"\u7d2b\u886b\u9f99\u738b", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("WndMain", u"\u4e94\u7edd", None))
        self.label_38.setText(QCoreApplication.translate("WndMain", u"\u9ec4 \u836f \u5e08", None))
        self.label_39.setText(QCoreApplication.translate("WndMain", u"\u6b27 \u9633 \u950b", None))
        self.label_40.setText(QCoreApplication.translate("WndMain", u"\u6bb5 \u667a \u5174", None))
        self.label_41.setText(QCoreApplication.translate("WndMain", u"\u6d2a   \u4e03", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("WndMain", u"\u7d2b\u7981\u9ad8\u624b", None))
        self.label_42.setText(QCoreApplication.translate("WndMain", u"\u82b1 \u6ee1 \u697c", None))
        self.label_43.setText(QCoreApplication.translate("WndMain", u"\u53f8\u7a7a\u6458\u661f", None))
        self.label_44.setText(QCoreApplication.translate("WndMain", u"\u53f6 \u5b64 \u57ce", None))
        self.label_45.setText(QCoreApplication.translate("WndMain", u"\u897f\u95e8\u5439\u96ea", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("WndMain", u"\u73cd\u73d1\u68cb\u5c40", None))
        self.label_46.setText(QCoreApplication.translate("WndMain", u"\u82cf \u661f \u6cb3", None))
        self.label_47.setText(QCoreApplication.translate("WndMain", u"\u4e01 \u6625 \u79cb", None))
        self.label_50.setText(QCoreApplication.translate("WndMain", u"\u674e \u79cb \u6c34", None))
        self.label_51.setText(QCoreApplication.translate("WndMain", u"\u5929\u5c71\u7ae5\u59e5", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_team), QCoreApplication.translate("WndMain", u"\u56e2\u961f\u914d\u7f6e", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("WndMain", u"\u4f7f\u7528\u7269\u54c1", None))
        self.chk_shiyong_bai_li_xiang.setText(QCoreApplication.translate("WndMain", u"\u767e\u91cc\u9999", None))
        self.chk_shiyong_hnx.setText(QCoreApplication.translate("WndMain", u"\u4f1a\u795e\u51dd\u795e\u9999", None))
        self.chk_shiyong_xiulianjuan.setText(QCoreApplication.translate("WndMain", u"\u4fee\u70bc\u5377", None))
        self.chk_shiyong_tongbaozuan.setText(QCoreApplication.translate("WndMain", u"\u901a\u5b9d\u94bb", None))
        self.chk_shiyong_tianmingsuipian.setText(QCoreApplication.translate("WndMain", u"\u5929\u547d\u788e\u7247\u888b", None))
        self.chk_shiyong_xinglangyueka.setText(QCoreApplication.translate("WndMain", u"\u884c\u56ca\u6708\u5361", None))
        self.chk_shiyong_sixiang.setText(QCoreApplication.translate("WndMain", u"\u56db\u8c61\u6d17\u7ec3\u4e39", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("WndMain", u"\u8d2d\u4e70\u7269\u54c1", None))
        self.chk_buy_xmx.setText(QCoreApplication.translate("WndMain", u"\u718a\u732b\u9999", None))
        self.edt_buy_xmx.setInputMask(QCoreApplication.translate("WndMain", u"000", None))
        self.edt_buy_xmx.setText(QCoreApplication.translate("WndMain", u"99", None))
        self.edt_buy_xmx.setPlaceholderText("")
        self.chk_buy_bcml.setText(QCoreApplication.translate("WndMain", u"\u767e\u8349\u871c\u917f", None))
        self.edt_buy_bcml.setInputMask(QCoreApplication.translate("WndMain", u"000", None))
        self.edt_buy_bcml.setText(QCoreApplication.translate("WndMain", u"99", None))
        self.edt_buy_bcml.setPlaceholderText("")
        self.chk_buy_hslh.setText(QCoreApplication.translate("WndMain", u"\u8d3a\u5c81\u793c\u82b1", None))
        self.edt_buy_hslh.setInputMask(QCoreApplication.translate("WndMain", u"000", None))
        self.edt_buy_hslh.setText(QCoreApplication.translate("WndMain", u"198", None))
        self.edt_buy_hslh.setPlaceholderText("")
        self.chk_buy_xbz.setText(QCoreApplication.translate("WndMain", u"\u7384\u51b0\u9488", None))
        self.edt_buy_xbz.setInputMask(QCoreApplication.translate("WndMain", u"000", None))
        self.edt_buy_xbz.setText(QCoreApplication.translate("WndMain", u"396", None))
        self.edt_buy_xbz.setPlaceholderText("")
        self.groupBox_shout.setTitle(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u558a\u8bdd", None))
        self.label_63.setText(QCoreApplication.translate("WndMain", u"\u558a\u8bdd\u9891\u7387(\u5206\u949f)", None))
        self.edt_shout.setPlainText("")
        self.groupBox_15.setTitle(QCoreApplication.translate("WndMain", u"\u4ed3\u5e93\u53d6\u7269", None))
        self.groupBox_fetch_lingshi.setTitle(QCoreApplication.translate("WndMain", u"\u7075\u77f3", None))
        self.label_24.setText(QCoreApplication.translate("WndMain", u"\u7ea7\u522b", None))
        self.chk_fetch_lingshi1.setText(QCoreApplication.translate("WndMain", u"\u4e00", None))
        self.chk_fetch_lingshi2.setText(QCoreApplication.translate("WndMain", u"\u4e8c", None))
        self.chk_fetch_lingshi3.setText(QCoreApplication.translate("WndMain", u"\u4e09", None))
        self.chk_fetch_lingshi4.setText(QCoreApplication.translate("WndMain", u"\u56db", None))
        self.chk_fetch_lingshi5.setText(QCoreApplication.translate("WndMain", u"\u4e94", None))
        self.chk_fetch_lingshi6.setText(QCoreApplication.translate("WndMain", u"\u516d", None))
        self.chk_fetch_lingshi7.setText(QCoreApplication.translate("WndMain", u"\u4e03", None))
        self.chk_fetch_lingshi8.setText(QCoreApplication.translate("WndMain", u"\u516b", None))
        self.chk_fetch_lingshi9.setText(QCoreApplication.translate("WndMain", u"\u4e5d", None))
        self.chk_fetch_lingshi10.setText(QCoreApplication.translate("WndMain", u"\u5341", None))
        self.label_25.setText(QCoreApplication.translate("WndMain", u"\u5c5e\u6027", None))
        self.chk_fetch_lingshi_jin.setText(QCoreApplication.translate("WndMain", u"\u91d1", None))
        self.chk_fetch_lingshi_mu.setText(QCoreApplication.translate("WndMain", u"\u6728", None))
        self.chk_fetch_lingshi_shui.setText(QCoreApplication.translate("WndMain", u"\u6c34", None))
        self.chk_fetch_lingshi_huo.setText(QCoreApplication.translate("WndMain", u"\u706b", None))
        self.chk_fetch_lingshi_tu.setText(QCoreApplication.translate("WndMain", u"\u571f", None))
        self.chk_fetch_hnx.setText(QCoreApplication.translate("WndMain", u"\u4f1a\u795e\u51dd\u795e\u9999", None))
        self.chk_fetch_bai_li_xiang.setText(QCoreApplication.translate("WndMain", u"\u767e\u91cc\u9999", None))
        self.chk_fetch_yao_cai.setText(QCoreApplication.translate("WndMain", u"\u836f\u6750", None))
        self.chk_fetch_za_huo.setText(QCoreApplication.translate("WndMain", u"\u6742\u8d27", None))
        self.chk_fetch_tong_bao_dai.setText(QCoreApplication.translate("WndMain", u"\u901a\u5b9d\u888b", None))
        self.label_64.setText("")
        self.chk_fetch_zhu_fu_cai.setText(QCoreApplication.translate("WndMain", u"\u4e3b\u8f85\u6750", None))
        self.chk_fetch_skill_book.setText(QCoreApplication.translate("WndMain", u"\u6280\u80fd\u4e66", None))
        self.chk_fetch_xun_ma.setText(QCoreApplication.translate("WndMain", u"\u9a6f\u9a6c\u6750\u6599", None))
        self.chk_fetch_fu_ben.setText(QCoreApplication.translate("WndMain", u"\u526f\u672c\u4ea7\u51fa", None))
        self.chk_fetch_bang_hui.setText(QCoreApplication.translate("WndMain", u"\u8dd1\u5e2e\u7269\u54c1", None))
        self.chk_fetch_tang_zhu.setText(QCoreApplication.translate("WndMain", u"\u5802\u4e3b\u6311\u6218\u4ee4", None))
        self.chk_fetch_cangbaotu.setText(QCoreApplication.translate("WndMain", u"\u85cf\u5b9d\u56fe", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("WndMain", u"\u5b9a\u65f6\u542f\u52a8", None))
        self.tedt_timer_run.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.groupBox_shout_bang_hui.setTitle(QCoreApplication.translate("WndMain", u"\u5e2e\u4f1a\u6750\u6599\u53f7\u558a\u8bdd", None))
        self.edt_shout_bang_hui.setPlainText(QCoreApplication.translate("WndMain", u"#143 \u5e2e\u4f1a\u6750\u6599\u53f7\u5728\u4e00\u7ebf\u5e2e\u4f1a\u5df2\u5c31\u4f4d  \u6709\u7a7a\u7684\u5144\u5f1f\u59d0\u59b9\u53ef\u4ee5\u8fc7\u6765\u8dd1\u751f\u4ea7\u4e86 \u9700\u8981\u7684\u4efb\u52a1\u54c1 \u70b9\u6211\u4ea4\u6613#127", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("WndMain", u"\u6362\u7ebf", None))
        self.label_60.setText(QCoreApplication.translate("WndMain", u"\u7ebf\u8def", None))
        self.cmb_switch_line.setItemText(0, QCoreApplication.translate("WndMain", u"\u4e00", None))
        self.cmb_switch_line.setItemText(1, QCoreApplication.translate("WndMain", u"\u4e8c", None))
        self.cmb_switch_line.setItemText(2, QCoreApplication.translate("WndMain", u"\u4e09", None))
        self.cmb_switch_line.setItemText(3, QCoreApplication.translate("WndMain", u"\u56db", None))
        self.cmb_switch_line.setItemText(4, QCoreApplication.translate("WndMain", u"\u4e94", None))
        self.cmb_switch_line.setItemText(5, QCoreApplication.translate("WndMain", u"\u516d", None))

        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_other), QCoreApplication.translate("WndMain", u"\u5176\u5b83\u914d\u7f6e", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("WndMain", u"toolBar", None))
    # retranslateUi

