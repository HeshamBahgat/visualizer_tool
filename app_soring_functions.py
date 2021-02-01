
## MainWindow
from mainWindow import MainWindow
from app_functions import AppFunctions

from algo import data_set, sorting_algorithms as algorithms

class SortingAppFunctions(MainWindow):
    def __init__(self):
        super(SortingAppFunctions, self).__init__()

        self.function = AppFunctions(self, "ui")

        # Plot's Layout
        self.function.addLayout("ploting_layout",  "frame_visualizing")
        self.function.ctreateFigure(1, 1, ["_dynamic_ax"], "dynamic_canvas")

        # Load the Array in the initation setup with random dtype as a default
        self.graphsetup()

        # Connect the Buttons to the Create Data Func
        self.ui.shuffle.activated.connect(self.graphsetup)
        self.ui.algorithms.activated.connect(self.graphsetup)

        self._timer_sorting = self.function.timerFunc(lambda: self._update_canvass(), "dynamic_canvas")

        self.sorting_buttons = [self.ui.pause_sorting, self.ui.play_sorting, self.ui.stop_sorting]
        self.function.controllers(self._timer_sorting, *self.sorting_buttons)


        self.ui.play_sorting.clicked.connect(lambda: self._updatee())
        self.ui.stop_sorting.clicked.connect(lambda: self.reset())

    def reset(self):
        self.function.changeStyle(self.ui.algorithms, "rgb(255, 255, 255)", True)
        self.function.changeStyle(self.ui.shuffle, "rgb(255, 255, 255)", True)

    def graphsetup(self):
        self.ploting_layout.removeWidget(self.dynamic_canvas)
        self.create_data()
        self.function.changeStyle(self.ui.play_sorting, "rgb(15, 57, 112)", True)

        self.function.confFigure(objName= "dynamic_canvas", facecolor= "#4b647a", background= "background-color: rgb(75, 100, 122);\n""")
        self.ploting_layout.addWidget(self.dynamic_canvas)

        self.addAx()

    def addAx(self):
        self._dynamic_ax.cla()
        color = [v.color for v in self.frames]
        self._dynamic_ax.bar(range(1, len(self.A) + 1), self.A, color=color, width=0.5)
        [self._dynamic_ax.spines[spin].set_visible(False) for spin in ["top", "left", "right"]]
        self._dynamic_ax.spines["bottom"].set_color((0.31, 0.62, 0.90))
        self._dynamic_ax.set_facecolor(("#B7CFDC"))
        self._dynamic_ax.set_xticks([])
        self._dynamic_ax.set_yticks([])
        self._dynamic_ax.figure.canvas.draw()

    def create_data(self):
        self.dtype = self.ui.shuffle.currentText()
        self.A = getattr(data_set, self.dtype)(50)
        self.func = self.ui.algorithms.currentText()
        self.frames = [AddColor(data) for data in self.A]
        self.generator = getattr(algorithms, self.func)(self.frames)

    def algorithm_func(self):
        self.func = self.ui.algorithms.currentText()
        frames = [AddColor(data) for data in self.A]
        self.generator = getattr(algorithms, self.func)(frames)

    def _updatee(self):
        self.function.changeStyle(self.ui.algorithms, "rgb(53, 81, 106);", False)
        self.function.changeStyle(self.ui.shuffle, "rgb(53, 81, 106);", False)
        self._timer_sorting.start()

    def draw_func(self, data):
        y = [v.value for v in data]
        x = range(len(data))
        color = [v.color for v in data]

        self._dynamic_ax.cla()
        self._dynamic_ax.set_xticks([])
        self._dynamic_ax.set_yticks([])
        self._dynamic_ax.set_title(self.func, color="w")
        self._dynamic_ax.bar(x, y, color=color, width=0.5)
        self._dynamic_ax.figure.canvas.draw()

    def _update_canvass(self):
        if self.flag: return
        try:
            self.data = next(self.generator)
            self.draw_func(self.data)
        except:
            self.draw_func(self.data)

            self._timer_sorting.stop()
            self.flag = False
            self.function.startStop(*self.sorting_buttons)

            self.function.changeStyle(self.ui.algorithms, "rgb(255, 255, 255)", True)
            self.function.changeStyle(self.ui.shuffle, "rgb(255, 255, 255)", True)

class AddColor(object):
    def __init__(self, value):
        self.value = value
        self.add_color()

    def add_color(self, color=None):
        if color == None:
            #color = "#929591"
            color = "#4b647a"
        self.color = color