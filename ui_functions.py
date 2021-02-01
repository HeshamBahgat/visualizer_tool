from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt, QEvent, QTimer
from PyQt5.QtGui import QIcon


GLOBAL_STATE = 0


class UIFunctions(object):

    def __init__(self, window):
        self.window = window

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTileBare(self):
        self.window.setWindowFlag(Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)

     ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.window.showMaximized()
            GLOBAL_STATE = 1
            self.window.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.window.ui.btn_maximize_restore.setToolTip("Restore")
            self.window.ui.btn_maximize_restore.setIcon(QIcon(u":/24x24/icons/24x24/cil-window-restore.png"))
            self.window.ui.frame_size_grip.hide()

        else:
            GLOBAL_STATE = 0
            self.window.showNormal()
            self.window.setGeometry(200, 100, 1200, 800)
            # obj.resize(1200, 800)
            self.window.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.window.ui.btn_maximize_restore.setToolTip("Maximize")
            self.window.ui.btn_maximize_restore.setIcon(QIcon(u":/24x24/icons/24x24/cil-window-maximize.png"))
            self.window.ui.frame_size_grip.show()

    ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
    ########################################################################
    def moveWindow(self, event):
        # IF MAXIMIZED CHANGE TO NORMAL
        if GLOBAL_STATE == 1:
            self.maximize_restore()

        # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.window.move(self.window.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        event.accept()

    # IF DOUBLE CLICK CHANGE STATUS
    def dobleClickMaximizeRestore(self, event):
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, lambda: self.maximize_restore())



    def labelPage(self, text):
        newText = text.upper()
        self.window.ui.label_des.setText(newText)

    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, standard, frameName):

        frame = getattr(self.window.ui, frameName)

        # GET WIDTH
        width = frame.width()
        maxExtend = maxWidth
        #standard = 30

        # SET MAX WIDTH
        if width == standard:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION
        self.window.animation = QPropertyAnimation(frame, b"minimumWidth")
        self.window.animation.setDuration(300)
        self.window.animation.setStartValue(width)
        self.window.animation.setEndValue(widthExtended)
        self.window.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.window.animation.start()



    @staticmethod
    def removeTileBare_statc(obj):
        obj.setWindowFlag(Qt.FramelessWindowHint)
        obj.setAttribute(Qt.WA_TranslucentBackground)


    # To Use Any Where
    @staticmethod
    def maximize_restore_staitc(obj, *args):
        global GLOBAL_STATE
        QIcon = args[0]
        status = GLOBAL_STATE
        if status == 0:
            obj.showMaximized()
            GLOBAL_STATE = 1
            obj.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            obj.ui.btn_maximize_restore.setToolTip("Restore")
            obj.ui.btn_maximize_restore.setIcon(QIcon(u":/24x24/icons/24x24/cil-window-restore.png"))
            obj.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            obj.showNormal()
            obj.setGeometry(200, 100, 1200, 800)
            #obj.resize(1200, 800)
            obj.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            obj.ui.btn_maximize_restore.setToolTip("Maximize")
            obj.ui.btn_maximize_restore.setIcon(QIcon(u":/24x24/icons/24x24/cil-window-maximize.png"))
            obj.ui.frame_size_grip.show()