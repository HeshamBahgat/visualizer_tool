
from algo.binaryheap import *
from algo.postool import *
from algo.visualtool import *


## MainWindow
from mainWindow import MainWindow
from app_functions import AppFunctions

### temp
from PyQt5.QtWidgets import QApplication

class TreeAppFunctions(MainWindow):
    def __init__(self):
        super(TreeAppFunctions, self).__init__()


        self.function = AppFunctions(self, "ui")

        # Plot's Layout
        self.function.addLayout("ploting_layout_tree", "frame_visualizing_tree")

        self.function.ctreateFigure(2, 1, ["axTree", "axArray"], "dynamic_canvas_tree")
        self.function.confFigure(objName="dynamic_canvas_tree", facecolor="#35516A",
                                 background="background-color: rgb(53, 81, 106);\n""")
        self.ploting_layout_tree.addWidget(self.dynamic_canvas_tree)

        self.function.removespines(self.axTree, self.axArray)

        # SetUp Buttons

        self._timer = self.function.timerFunc(lambda: self._update("build"), "dynamic_canvas_tree")

        self.buttons = [self.ui.pause_Tree, self.ui.play_Tree, self.ui.stop_Tree]
        self.function.controllers(self._timer, *self.buttons)

        self.heaptype =  ""

        self.ui.inputArr.clicked.connect(lambda: self.functions.toggleMenu(300, 0, "frame_visualizing_lefttree"))
        self.ui.insertArray.clicked.connect(lambda: self.inserArr())
        self.function.changeStyle(self.ui.insertArray, "rgb(75, 100, 122)", False)


        self.ui.play_Tree.clicked.connect(lambda: self._timer.start())
        self.ui.heapsort.clicked.connect(lambda: self._update_canvas_heap())
        self.ui.insert_ele_button.clicked.connect(self.insertElement)
        self.ui.extract_ele_button.clicked.connect(self.removeElement)


        self.function.changeStyle(self.ui.play_Tree, "rgb(75, 100, 122)", False)
        self.function.changeStyle(self.ui.heapsort, "rgb(75, 100, 122)", False)
        self.function.changeStyle(self.ui.insert_ele_button, "rgb(75, 100, 122)", False)
        self.function.changeStyle(self.ui.extract_ele_button, "rgb(75, 100, 122)", False)

        #self.ui.oN.setChecked(True)
        self.ui.oN.toggled.connect(self.onradio)
        self.ui.logN.toggled.connect(self.onradio)




    def removeElement(self):
        self.frames = self.bh.removeroot()
        self.function.changeStyle(self.ui.heapsort, "rgb(15, 57, 112)", True)

        self.flag = True
        self.function.startStop(*self.buttons)

        #self.function.timerFunc(lambda: self._update_canvas("remove"), "dynamic_canvas_tree")
        self._timer = self.function.timerFunc(lambda: self._update_canvas("remove"), "dynamic_canvas_tree")

        self.function.changeStyle(self.ui.heapsort, "rgb(53, 81, 106);", False)
        self.function.changeStyle(self.ui.insertArray, "rgb(53, 81, 106);", False)

        self.function.changeStyle(self.ui.insert_ele_button, "rgb(53, 81, 106);", False)
        self.function.changeStyle(self.ui.extract_ele_button, "rgb(53, 81, 106);", False)

        self._timer.start()

    def insertElement(self):
        ele = self.ui.insert_ele.text()
        if not check_float(ele) or not check_int(ele):
            return


        self.frames = self.bh.insertEle(ele)

        self.function.changeStyle(self.ui.heapsort, "rgb(15, 57, 112)", True)

        self.flag = True
        self.function.startStop(*self.buttons)

        #self.function.timerFunc(lambda:  self._update_canvas("insert"), "dynamic_canvas_tree")
        self._timer = self.function.timerFunc(lambda: self._update_canvas("insert"), "dynamic_canvas_tree")

        self.function.changeStyle(self.ui.heapsort, "rgb(53, 81, 106);", False)
        self.function.changeStyle(self.ui.insertArray, "rgb(53, 81, 106);", False)

        self.function.changeStyle(self.ui.insert_ele_button, "rgb(53, 81, 106);", False)
        self.function.changeStyle(self.ui.extract_ele_button, "rgb(53, 81, 106);", False)


        self._timer.start()


    def _update_canvas_heap(self):
        self.frames = self.bh.heapSort()

        self.function.changeStyle(self.ui.heapsort, "rgb(53, 81, 106);", False)
        self.function.changeStyle(self.ui.insertArray, "rgb(53, 81, 106);", False)

        self.function.changeStyle(self.ui.insert_ele_button, "rgb(53, 81, 106);", False)
        self.function.changeStyle(self.ui.extract_ele_button, "rgb(53, 81, 106);", False)

        self.flag = True
        self.function.startStop(*self.buttons)

        self._timer = self.function.timerFunc(lambda: self._update_canvas("heapsort"), "dynamic_canvas_tree")
        self._timer.start()


        self.function.changeStyle(self.ui.play_Tree, "rgb(53, 81, 106);", False)

    def _update(self, tag):
        self.function.changeStyle(self.ui.insertArray, "rgb(75, 100, 122)", False)
        self._update_canvas(tag)


    def _update_canvas(self, tag):

        self.ui.extract_ele.setText(str(self.bh.root))
        if self.flag: return
        try:
            frames = next(self.frames)

            if isinstance(frames, tuple):
                treeFrames, arrFrames = frames

            else:
                treeFrames = arrFrames = frames
        #except

        except StopIteration:
            if self.heaptype == "build" or tag == "insert" or tag == "remove":
                self.function.changeStyle(self.ui.heapsort, "rgb(15, 57, 112)", True)
                self.function.changeStyle(self.ui.insert_ele_button, "rgb(15, 57, 112)", True)
                self.function.changeStyle(self.ui.extract_ele_button, "rgb(15, 57, 112)", True)
                self.heaptype = "heapsort"
            else:
                #self.function.changeStyle(self.ui.heapsort, "rgb(53, 81, 106);", False)
                #self.function.changeStyle(self.ui.insertArray, "rgb(53, 81, 106);", False)
                pass
            self.function.changeStyle(self.ui.insertArray, "rgb(15, 57, 112)", True)

            self._timer.stop()
            self.flag = False
            self.function.startStop(*self.buttons)
            return

        self.callDraw(treeFrames, arrFrames)

    def callDraw(self, treeFrames, arrFrames):
        self.axTree.cla()
        self.axArray.cla()

        self.function.drawTree(self.axTree, treeFrames)
        self.function.drawArray(drawarr, self.axArray, arrFrames)

        self.axTree.figure.canvas.draw()
        self.axArray.figure.canvas.draw()

    # Build Data
    def type(self):

        if self.ui.checkHeapSort.isChecked():
            self.heaptype = "HeapSort"
        else:
            self.heaptype = "build"

        if self.bigO == "O(N)":
            self.bh = BinaryHeap()
            self.frames = self.bh.insertON(self.data, self.heaptype)

        else:
            self.bh = BinaryHeap()
            self.frames = self.bh.buildHeap(self.data, self.heaptype)




    def inserArr(self):
        self.axTree.cla()
        self.axArray.cla()

        self.data = self.createData()
        self.type()

        self.function.drawArray(drawarr, self.axArray, self.data)
        self.axArray.figure.canvas.draw()

        self.flag = False
        self.function.startStop(*self.buttons)

        self.function.changeStyle(self.ui.heapsort, "rgb(53, 81, 106);", False)

        self.function.changeStyle(self.ui.insert_ele_button, "rgb(53, 81, 106);", False)
        self.function.changeStyle(self.ui.extract_ele_button, "rgb(53, 81, 106);", False)


    def createData(self):
        #self.func = self.ui.heap_type.currentText()
        data = [ClassifyData(num) for num in generateData(15)]
        return data

    def genFrames(self, data, type):
        #self.bh = BinaryHeap()
        frames = self.bh.buildHeap(data, type)
        frames = self.bh.insertON(data)

        return frames

    def onradio(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.function.changeStyle(self.ui.insertArray, "rgb(15, 57, 112)", True)
            self.bigO = radioBtn.text()


def check_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    m = TreeAppFunctions()
    m.show()
    sys.exit(app.exec_())
