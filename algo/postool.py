#! /usr/bin/python3

from numpy import array



def gethieght(lenght, h=None):
    if h == None:
        h = 0

    if lenght <= 2 ** h:
        return h

    return gethieght(lenght, h + 1)


def levelOrederPrint(nodelist, height):
    # Tracking the nodes from level to another level
    cur_count, next_count = 1, 0
    track_nextNodes = []

    # xaxis the lenght of X-Axis
    # xi the incremant of x depends on the nodes on each hight
    xaxis, xi = (2 ** height), 0

    # to calc the range of increment on the x-axis
    # i will be always incremented by i * 2 as the nodes will be incremented on each higher level
    # n to know how many spaces between nodes when devide the the whole xais on n (xaxis / n)
    # so (xaxis / n) will be wheres the first node should be located
    # n = n + i for the next level

    i, n = 1, 2
    x, y = xaxis / n, height

    track_nextNodespos = [x]

    # here will save the result
    # theses variable later will be passed to the plot func for animation
    edgelist, pos = [], {}

    # will extract each node on the array as a Queue FIFO
    nodelist = [0] + nodelist
    # will start from one not zero cuz on BinaryHeap we start from index 1 to calacaute
    # the left and right children
    # Left(2 * n), right(2 * n + 1)
    # se when we divid either the right or left value // 2 will get easily the parent value for
    # either percUp or percDown

    for idx in range(1, len(nodelist)):

        # to track the end of each tree level or hight

        x = track_nextNodespos[-cur_count]

        cur_count -= 1

        # record the parrent postion
        # ParentNode
        parentNode = nodelist[idx]
        parentNode.addIdx(idx)
        parentNode.addAxises(x, y)
        pos[parentNode.idx] = array([x, y])

        # will increment the value for the next node on the same hight-(Y) but diff x value
        # x += xi

        # try and except will act as a condtion if the node has right or left child as the array index
        # if it exists will add it to edglist
        try:
            # Left Child # will pass if not exists
            leftNode = nodelist[2 * idx]

            # Add it the the Edge List
            parentNode.left = leftNode
            edgelist.append((parentNode, leftNode))
            next_count += 1
            track_nextNodes.append(True)

        except IndexError:
            track_nextNodes.append(False)

        try:
            # Right Child # will pass if not exists
            rightNode = nodelist[2 * idx + 1]

            # Add it the the Edge List
            parentNode.right = rightNode
            edgelist.append((parentNode, rightNode))

            next_count += 1
            track_nextNodes.append(True)

        except IndexError:
            track_nextNodes.append(False)

        if cur_count == 0:

            # decrement the height from level to level
            y = y - 1

            # the values that needs to calc the increment on the X-Axis on the next level
            n = n + i
            i = i * 2
            x = xaxis / n
            xi = x

            track_nextNodespos = []
            for v in track_nextNodes:
                if v == True:
                    track_nextNodespos.append(x)
                    x += xi

                else:
                    x += xi

            track_nextNodes = []

            # the actual nodes numbers on the next level
            cur_count, next_count = next_count, cur_count

    return edgelist, pos