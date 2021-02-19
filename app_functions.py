

from PyQt5.QtWidgets import QVBoxLayout
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

## temp
from algo.postool import *
from algo.visualtool import *


class AppFunctions(object):
    def __init__(self, window, objName):
        super(AppFunctions, self).__init__()


        self.window = window
        self.obj = getattr(self.window, objName)

    def removespines(self, *args):
        [ax.spines[spin].set_visible(False) for ax in args for spin in ["top", "left", "right"]]
        [ax.spines["bottom"].set_color((0.31, 0.62, 0.90)) for ax in args]
        [ax.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False) for ax in args]

    def addLayout(self, layoutName, objName):
        name = getattr(self.obj, objName)

        setattr(self.window, layoutName, QVBoxLayout(name))

        layoutName = getattr(self.window, layoutName)
        layoutName.setContentsMargins(0, 0, 0, 0)
        layoutName.setSpacing(0)
        layoutName.setObjectName(objName)

    def ctreateFigure(self, row, col, aXnames, objName):
        fig, axs = plt.subplots(row, col,figsize=(10, 5))
        setattr(self.window, objName, FigureCanvas(fig))

        if len(aXnames) == 1:
            setattr(self.window, aXnames[0], axs)
        else:
            [setattr(self.window, name, axs[idx]) for idx, name in enumerate(aXnames)]

    def confFigure(self, **kwargs):#objName):
        name = getattr(self.window, kwargs["objName"])
        name.setObjectName(kwargs["objName"])

        name.figure.patch.set_facecolor(kwargs['facecolor'])
        name.setStyleSheet(kwargs["background"])



    def drawArray(self, drawFunc, ax, arrFrames):
        drawFunc(ax, arrFrames)
        #ax.figure.canvas.draw()

    def drawTree(self, ax, treeFrames):
        height = gethieght(len(treeFrames))
        edgelist, pos = levelOrederPrint(treeFrames, height)

        ax.set_frame_on(False)
        ax.set_facecolor(("#B7CFDC"))

        drawArrows(ax, edgelist, pos)
        addLablesAndNodes(ax, treeFrames, pos)


    # Controllers
    def controllers(self, timer, *buttons):

        self.window.flag = True

        pauseButton = buttons[0]
        playButton  = buttons[1]
        stopButton  = buttons[2]

        playButton.clicked.connect(lambda: self.startStop(*buttons))

        self.changeStyle(pauseButton, "rgb(75, 100, 112)", False)
        pauseButton.clicked.connect(lambda: self.startStop(*buttons))

        self.changeStyle(stopButton, "rgb(75, 100, 112)", False)
        stopButton.clicked.connect(lambda: self.stop(timer, *buttons))

        #self.stopButton.setStyleSheet("background-color: rgb(75, 100, 122);")
        #self.stopButton.setEnabled(False)

    def timerFunc(self, func, canvas):
        canvas = getattr(self.window, canvas)
        _timer = canvas.new_timer(0)
        _timer.add_callback(func)
        return _timer

    def startStop(self, *buttons):
        pauseButton = buttons[0]
        playButton  = buttons[1]
        stopButton  = buttons[2]

        if self.window.flag:
            self.window.flag = False
            self.changeStyle(playButton, "rgb(75, 100, 112)", False)
            self.changeStyle(pauseButton, "rgb(15, 57, 112)", True)
            self.changeStyle(stopButton, "rgb(15, 57, 112)", True)



        elif not self.window.flag:
            self.window.flag = True
            self.changeStyle(playButton, "rgb(15, 57, 112)", True)
            self.changeStyle(pauseButton, "rgb(75, 100, 112)", False)
            self.changeStyle(stopButton, "rgb(75, 100, 112)", False)


    def stop(self, timer, *buttons):

        timer.stop()
        self.window.flag = False
        self.startStop(*buttons)
        self.changeStyle(buttons[1], "rgb(75, 100, 112)", False)

    def changeStyle(self, button, color, status):
        button.setStyleSheet(f"background-color: {color}; \ncolor: rgb(0, 0, 0)")
        button.setEnabled(status)