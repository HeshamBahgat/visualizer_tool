
#from PyQt5 import QtCore

from PyQt5.QtGui import QColor

from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QSizeGrip

## ==> MAIN WINDOW
from ui_MainWindow import Ui_MainWindow

from ui_functions import UIFunctions


GLOBAL_STATE = 0

## ==> MAIN WINDOW
# YOUR APPLICATION
class MainWindow(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setGeometry(200, 100, 0, 0)
        self.ui.setupUi(self)
        self.functions = UIFunctions(self)

        ## REMOVE ==> STANDARD TITLE BAR
        self.functions.removeTileBare()

        self.ui.frame_top.mouseDoubleClickEvent = self.functions.dobleClickMaximizeRestore
        self.mousePressEvent = self.functions.mousePressEvent
        self.ui.frame_top.mouseMoveEvent = self.functions.moveWindow

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> START PAGE in Stacked Widget
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        self.functions.labelPage("Home")

        ## Stacked Widget Switching Pages
        self.ui.home_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.home_btn.clicked.connect(lambda: self.functions.labelPage("Home"))

        self.ui.about_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_about))
        self.ui.about_btn.clicked.connect(lambda: self.functions.labelPage("About"))

        self.ui.sorting_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_sorting))
        self.ui.sorting_btn.clicked.connect(lambda: self.functions.labelPage("Sorting") )


        self.ui.tree_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tree))
        self.ui.tree_btn.clicked.connect(lambda: self.functions.labelPage("Tree"))

        self.ui.linkedlist_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_linkedlist))
        self.ui.linkedlist_btn.clicked.connect(lambda: self.functions.labelPage("LinkedList"))

        ## ==> TOGGLE MENU
        self.ui.btn_toggle.clicked.connect(lambda: self.functions.toggleMenu(50, 30, "frame_left_menu"))

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        # CLOSE WINDOW
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: self.functions.maximize_restore())

        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)