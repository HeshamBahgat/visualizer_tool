from numpy import array
from  random import randint
import copy

class ClassifyData(object):

    def __init__(self, value):
        self.value = value
        self.color = "white"  # "#929591"

        self.idx = 0
        self.pos = None

        self.parent = None
        self.left = None
        self.right = None

        self.height = 1

    def addIdx(self, idx):
        self.idx = idx

    def setColor(self, color):
        self.color = color

    def addAxises(self, x, y):
        self.pos = array([x, y])


def generateData(n=100):
    y = [randint(1, 100) for i in range(0, n)]
    return y

class BinaryHeap(object):

    def __init__(self):
        #self.arrData = self.treeData = self.bh = [0]
        self.bh = [0]
        self.idx = 0

        self.root = 0

    def insertON(self, arr):

        for ele in arr:
            yield from self.insert_ele(ele)

    def insertEle(self, ele):
        ele = int(ele)
        val = ClassifyData(ele)
        yield from self.insert_ele(val)

    def insert_ele(self, ele):

        self.bh.append(ele)

        yield self.bh[1:], self.bh[1:]

        self.idx += 1
        yield from self.precup(self.idx)
        yield self.bh[1:], self.bh[1:]

    def precup(self, idx):

        cur_value = self.bh[idx]
        cur_value.setColor("r")

        yield self.bh[1:], self.bh[1:]
        while idx // 2 > 0:
            parent_value = self.bh[idx // 2]
            parent_value.setColor("#F88017")
            yield self.bh[1:], self.bh[1:]
            if cur_value.value < parent_value.value:
                self.bh[idx], self.bh[idx // 2] = self.bh[idx // 2], self.bh[idx]
                yield self.bh[1:],  self.bh[1:]
            idx = idx // 2
            cur_value.setColor("white")
            parent_value.setColor("white")
            yield self.bh[1:], self.bh[1:]
        self.bh[idx].setColor("white")
        yield self.bh[1:], self.bh[1:]

    def removeroot(self):

        if self.idx <= 0: return

        self.bh[1].setColor("#F88017")
        yield self.bh[1:], self.bh[1:]

        self.root = self.bh[1].value

        self.bh[-1].setColor("#4CC417")
        yield self.bh[1:], self.bh[1:]

        self.bh[1], self.bh[-1] = self.bh[-1], self.bh[1]
        self.idx -= 1

        yield self.bh[1:], self.bh[1:]

        self.bh.pop()

        self.arrData = self.bh[1:]
        #self.arrData[self.start].setColor("y")

        yield self.bh[1:], self.bh[1:]

        yield from self.precdwon(1)


    def precdwon(self, idx):

        yield self.bh[1:], self.bh[1:]
        while idx * 2 <= self.idx:

            minchild = self.minChild(idx)

            # change minchild color
            self.bh[minchild].setColor("#3fe0d0")
            self.bh[idx].setColor("#094c72")
            yield self.bh[1:], self.bh[1:]

            if self.bh[idx].value > self.bh[minchild].value:
                # change self.bh[idx], self.bh[minchild] color
                self.bh[idx], self.bh[minchild] = self.bh[minchild], self.bh[idx]
                yield self.bh[1:], self.bh[1:]

            self.bh[idx].setColor("white")
            self.bh[minchild].setColor("white")
            idx = minchild
            yield self.bh[1:], self.bh[1:]



    def minChild(self, idx):
        if 2 * idx + 1 > self.idx:
            return 2 * idx
        else:
            if self.bh[2 * idx].value < self.bh[2 * idx + 1].value:
                return 2 * idx
            else:
                return 2 * idx + 1


    def buildHeap(self, alist, HeapSort):
        idx = len(alist) // 2
        self.idx = len(alist)
        self.bh = [0] + alist[:]

        while idx > 0:
            yield from self.precdwon(idx)
            idx -= 1

        if HeapSort == "HeapSort":
            yield from self.heapSort()

    def heapSort(self):
        idx = self.idx

        self.arrData = copy.deepcopy(self.bh)
        #self.treeData = self.bh[:]
        self.removedItem = []

        while idx > 1:
            yield from self.removeHeap()
            idx -= 1
        self.bh[-1].setColor("#F88017")
        #yield self.bh[1:], self.arrData[1:]
        self.removedItem.append(self.bh.pop())
        yield self.bh[1:], self.removedItem + self.bh[1:]

    def removeHeap(self):

        if self.idx <= 0: return

        self.bh[1].setColor("#F88017")
        yield self.bh[1:], self.removedItem + self.bh[1:]

        self.root = self.bh[1].value

        self.bh[-1].setColor("#4CC417")
        yield self.bh[1:], self.removedItem + self.bh[1:]

        self.bh[1], self.bh[-1] = self.bh[-1], self.bh[1]
        self.removedItem.append(self.bh.pop())
        self.idx -= 1

        yield self.bh[1:], self.removedItem + self.bh[1:]

        #self.arrData = self.bh[1:]
        #self.arrData[self.start].setColor("y")

        yield self.bh[1:], self.removedItem + self.bh[1:]

        yield from self.precdwonHeap(1)

    def precdwonHeap(self, idx):

        yield self.bh[1:], self.removedItem + self.bh[1:]
        while idx * 2 <= self.idx:

            minchild = self.minChild(idx)

            # change minchild color
            self.bh[minchild].setColor("#3fe0d0")
            self.bh[idx].setColor("#094c72")
            yield self.bh[1:], self.removedItem + self.bh[1:]

            if self.bh[idx].value > self.bh[minchild].value:
                # change self.bh[idx], self.bh[minchild] color
                self.bh[idx], self.bh[minchild] = self.bh[minchild], self.bh[idx]
                yield self.bh[1:],  self.removedItem + self.bh[1:]

            self.bh[idx].setColor("white")
            self.bh[minchild].setColor("white")
            idx = minchild
            yield self.bh[1:], self.removedItem + self.bh[1:]




class BinaryHeap1(object):

    def __init__(self):
        self.arrData = self.treeData = self.bh = [0]
        self.idx = 0
        self.root = 0
        self.start = 1
        self.end = 0

    def insertON(self, arr):

        for ele in arr:
            yield from self.insert_ele(ele)

    def insertEle(self, ele):
        ele = int(ele)
        val = ClassifyData(ele)
        yield from self.insert_ele(val)

    def insert_ele(self, ele):

        self.bh.append(ele)

        yield self.bh[1:], self.bh[1:]

        self.idx += 1
        yield from self.precup(self.idx)
        yield self.bh[1:], self.bh[1:]

        # self.end = self.idxSort = self.idx
        self.start = 1
        # self.arrData = copy.deepcopy(self.treeData)

        self.end = self.idx - 1
        self.arrData = copy.deepcopy(self.bh)


    def precup(self, idx):

        cur_value = self.bh[idx]
        cur_value.setColor("r")

        yield self.bh[1:], self.bh[1:]
        while idx // 2 > 0:
            parent_value = self.bh[idx // 2]
            parent_value.setColor("#F88017")
            yield self.bh[1:], self.bh[1:]
            if cur_value.value < parent_value.value:
                self.bh[idx], self.bh[idx // 2] = self.bh[idx // 2], self.bh[idx]
                yield self.bh[1:], self.bh[1:]
            idx = idx // 2
            cur_value.setColor("white")
            parent_value.setColor("white")
            yield self.bh[1:], self.bh[1:]
        self.bh[idx].setColor("white")
        yield self.bh[1:], self.bh[1:]



    def minChild(self, idx):
        if 2 * idx + 1 > self.idx:
            return 2 * idx
        else:
            if self.bh[2 * idx].value < self.bh[2 * idx + 1].value:
                return 2 * idx
            else:
                return 2 * idx + 1

    def precdwon(self, idx):

        print(2)
        print("tree", [i.value for i in self.treeData[1:]])
        print("arr", [i.value for i in self.arrData[1:]])
        print("bh", [i.value for i in self.bh[1:]])
        print("-" * 50)

        yield self.treeData[1:], self.arrData[1:]
        while idx * 2 <= self.idx:

            minchild = self.minChild(idx)

            # change minchild color
            self.bh[minchild].setColor("#3fe0d0")
            self.bh[idx].setColor("#094c72")
            yield self.treeData[1:], self.arrData[1:]

            if self.bh[idx].value > self.bh[minchild].value:
                # change self.bh[idx], self.bh[minchild] color
                self.bh[idx], self.bh[minchild] = self.bh[minchild], self.bh[idx]
                self.treeData = self.bh[:]
                ##########

                print(3-0)
                print("tree", [i.value for i in self.treeData[1:]])
                print("arr", [i.value for i in self.arrData[1:]])
                print(self.start, len(self.bh), len(self.arrData))
                print("bh", [i.value for i in self.bh[1:]])
                print("-" * 50)

                #self.arrData = self.arrData[:self.start] + self.bh[1:]
                self.arrData = self.bh[:]

                print(3-1)
                print("tree", [i.value for i in self.treeData[1:]])
                print("arr", [i.value for i in self.arrData[1:]])
                print("bh", [i.value for i in self.bh[1:]])
                print("-" * 50)

                yield self.treeData[1:], self.arrData[1:]

            self.bh[idx].setColor("white")
            self.bh[minchild].setColor("white")
            idx = minchild
            print(4)
            print("tree", [i.value for i in self.treeData[1:]])
            print("arr", [i.value for i in self.arrData[1:]])
            print("bh", [i.value for i in self.bh[1:]])
            print("-" * 50)
            yield self.treeData[1:], self.arrData[1:]

    def buildHeap(self, alist, HeapSort):
        idx = len(alist) // 2
        self.idx = len(alist)
        self.arrData = self.treeData = self.bh = [0] + alist[:]

        self.start = 0

        while idx > 0:
            print(1-0)
            print("tree", [i.value for i in self.treeData[1:]])
            print("arr", [i.value for i in self.arrData[1:]])
            print("bh", [i.value for i in self.bh[1:]])
            print("-" * 50)

            yield from self.precdwon(idx)
            idx -= 1

        self.end = self.idxSort = self.idx
        self.start = 1
        self.arrData = copy.deepcopy(self.treeData)

        if HeapSort == "HeapSort":
            yield from self.heapSort()

    def heapSort(self):
        while self.idxSort > 1:
            yield from self.removeroot()
            self.idxSort -= 1
        self.arrData[-1].setColor("#F88017")
        yield self.treeData[1:], self.arrData[1:]

    def removeroot(self):

        if self.idx <= 0: return

        self.treeData[1].setColor("#F88017")
        yield self.treeData[1:], self.arrData[1:]

        self.root = self.bh[1].value

        self.treeData[-1].setColor("#4CC417")
        yield self.treeData[1:], self.arrData[1:]

        self.bh[1], self.bh[self.idx] = self.bh[self.idx], self.bh[1]
        self.bh.pop()
        self.idx -= 1

        self.treeData = self.bh[:]
        yield self.treeData[1:], self.arrData[1:]

        print(self.idx, self.start, len(self.arrData), self.end)

        self.arrData = self.arrData[:self.start + 1] + [self.arrData[self.end]] + self.arrData[self.start + 1:self.end]
        self.arrData[self.start].setColor("y")
        self.start += 1
        yield self.treeData[1:], self.arrData[1:]

        yield from self.precdwon(1)