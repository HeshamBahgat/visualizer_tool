import time

def bubblesort(frames):
    #result = [frames]
    j = len(frames)
    i = 0
    while j > 0:
        swapped = False
        while i + 1 < j:
            frames[i].add_color("#008081")
            frames[i + 1].add_color("#008081")

            yield frames

            if frames[i].value > frames[i + 1].value:
                frames[i].value, frames[i + 1].value = frames[i + 1].value, frames[i].value
                yield frames
                swapped = True

            frames[i].add_color("#929591")
            frames[i + 1].add_color("#929591")
            i += 1

        frames[i].add_color("#055a8c")
        i = 0
        j -= 1
        if swapped == False:
            for i in range(j, -1, -1):
                frames[i].add_color("#055a8c")
                yield frames
            break

    return


def shellsort(frames):
    n = len(frames)
    gap = n // 2



    while gap > 0:
        r = [i for i in range(gap, n)]
        [frames[i].add_color("#929591") for i in range(n) if i in r]
        [frames[i].add_color("#5ba4cf") for i in range(gap, n) if i not in r]
        yield frames

        for i in range(gap, n):
            cur_obj = frames[i]
            cur_value = cur_obj.value
            pos = i
            cur_obj.add_color("#008081")
            yield frames

            while pos >= gap and frames[pos - gap].value > cur_value:
                frames[pos - gap].add_color("#008081")
                yield frames

                frames[pos - gap], frames[pos] = frames[pos], frames[pos - gap]
                yield frames

                frames[pos].add_color("#055a8c")
                pos = pos - gap
                yield frames

            frames[pos].add_color("#055a8c")
            yield frames

        gap //= 2


    #[frames[i].add_color("r") for i in range(n)]
    #yield frames


def insertionsort(frames):
    frames[0].add_color("#055a8c")
    yield frames

    for i in range(1, len(frames)):
        cur_obj = frames[i]
        cur_value = cur_obj.value
        pos = i
        cur_obj.add_color("#008081")
        yield frames

        while pos > 0 and frames[pos - 1].value > cur_value:
            frames[pos - 1].add_color("#008081")
            yield frames

            frames[pos - 1], frames[pos] = frames[pos], frames[pos - 1]
            yield frames

            frames[pos].add_color("#055a8c")
            pos = pos - 1
            yield frames

        frames[pos].add_color("#055a8c")
        yield frames


def selectionsort(frames):
    for i in range(len(frames)):

        min_value = frames[i].value
        min_index = i
        frames[min_index].add_color("#3975b5")
        yield frames

        for j in range(i+1, len(frames)):

            frames[j].add_color("#008081")
            yield frames

            if frames[j].value < min_value:
                frames[j].add_color("#1034a6")
                frames[min_index].add_color("#929591")
                min_index = j
                min_value = frames[min_index].value
                yield frames

            else:
                frames[j].add_color("#929591")
                yield frames


        if i == min_index:
            frames[i].add_color("#055a8c")
            yield frames

        else:
            frames[i].add_color("#1034a6")
            yield frames
            frames[i], frames[min_index] = frames[min_index], frames[i]
            yield frames
            frames[i].add_color("#055a8c")
            frames[min_index].add_color("#929591")
            yield frames


def mergesort(arr, startindex=0, alldata=None):

    if alldata == None:
        alldata = arr

    if len(arr) > 1:
        mid = len(arr) // 2
        right = startindex + mid
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        yield from mergesort(lefthalf, startindex, alldata)
        yield from mergesort(righthalf, right, alldata)

        left_index = right_index = arr_index = 0

        [i.add_color("#008081") for i in alldata[startindex:right]]
        [i.add_color("#3fe0d0") for i in alldata[right:right + mid]]

        k = startindex

        yield alldata

        while left_index < len(lefthalf) and right_index < len(righthalf):

            if lefthalf[left_index].value < righthalf[right_index].value:
                arr[arr_index] = lefthalf[left_index]
                alldata[k] = lefthalf[left_index]
                yield alldata

                left_index += 1

            else:
                arr[arr_index] = righthalf[right_index]
                alldata[k] = righthalf[right_index]
                yield alldata

                right_index += 1

            yield alldata

            arr_index += 1
            k += 1

        while left_index < len(lefthalf):
            arr[arr_index] = lefthalf[left_index]
            alldata[k] = lefthalf[left_index]

            left_index += 1
            arr_index += 1
            k += 1
            yield alldata

        while right_index < len(righthalf):
            arr[arr_index] = righthalf[right_index]
            alldata[k] = righthalf[right_index]

            right_index += 1
            arr_index += 1
            k += 1
            yield alldata

        [i.add_color("#055a8c") for i in alldata[startindex:right]]
        [i.add_color("#055a8c") for i in alldata[right:right + mid]]

        yield alldata

def quicksort(arr, start=None, end=None):
    if start == None and end == None:
        start = 0
        end = len(arr) - 1

    if start >= end:
        return

    splitpoint = start

    [i.add_color("#929591") for i in arr[start:end + 1]]

    arr[splitpoint].add_color("#3fe0d0")

    yield arr

    pivot = arr[start]
    pivot.add_color("b")
    yield arr

    for i in range(start + 1, end + 1):
        arr[i].add_color("#008081")
        yield arr

        if arr[i].value <= pivot.value:
            splitpoint += 1
            arr[i], arr[splitpoint] = arr[splitpoint], arr[i]
            yield arr

        else:
            arr[i].add_color("#055a8c")

    arr[splitpoint].add_color("#3fe0d0")
    yield arr

    arr[start], arr[splitpoint] = arr[splitpoint], arr[start]
    yield arr

    yield from quicksort(arr, start, splitpoint - 1)
    yield from quicksort(arr, splitpoint + 1, end)

    [i.add_color("#055a8c") for i in arr[start:end + 1]]





# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort(arr, first=None, last=None):
    if first == None and last == None:
        first = 0
        last = len(arr) - 1

    while first < last:
        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion

        if last - first + 1 < 10:
            value = yield from insertion_sort(arr, first, last)
            if value: yield value
            break

        else:
            splitpoint = yield from partition(arr, first, last)

            if splitpoint != None and not isinstance(splitpoint, int):
                if splitpoint: yield splitpoint

            if splitpoint - first < last - splitpoint:
                yield from hybrid_quick_sort(arr, first, splitpoint - 1)
                first = splitpoint + 1
            else:
                yield from hybrid_quick_sort(arr, splitpoint + 1, last)
                last = splitpoint - 1

    [i.add_color("#253e5e") for i in arr]
    yield arr


def insertion_sort(frames, gap, n):
    frames[0].add_color("#055a8c")
    yield frames

    for i in range(gap + 1, n + 1):
        cur_obj = frames[i]
        cur_value = cur_obj.value
        pos = i
        cur_obj.add_color("#008081")
        yield frames

        while pos > gap and frames[pos - 1].value > cur_value:
            frames[pos - 1].add_color("#008081")
            yield frames

            frames[pos - 1], frames[pos] = frames[pos], frames[pos - 1]
            yield frames

            frames[pos].add_color("#055a8c")
            pos = pos - 1
            yield frames

        frames[pos].add_color("#055a8c")
        yield frames


def partition(arr, first, last):
    pivotvalue = arr[first]
    leftmark = first + 1
    rightmark = last

    arr[first].add_color("#055a8c")
    arr[leftmark].add_color("#3fe0d0")
    arr[rightmark].add_color("#3bbdc2")

    yield arr

    done = False

    while not done:
        while leftmark <= len(arr) and leftmark <= rightmark and arr[leftmark].value <= pivotvalue.value:

            #if leftmark == len(arr): break
            arr[leftmark].add_color("#3fe0d0")
            leftmark = leftmark + 1
            yield arr

        while arr[rightmark].value >= pivotvalue.value and rightmark >= leftmark:
            rightmark = rightmark - 1
            if rightmark > 0: arr[rightmark].add_color("#3bbdc2")
            yield arr

        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]
            yield arr

            arr[leftmark].add_color("#094c72")
            arr[rightmark].add_color("#094c72")
            yield arr

    arr[first].add_color("#055a8c")
    arr[rightmark].add_color("#055a8c")
    yield arr

    arr[first], arr[rightmark] = arr[rightmark], arr[first]
    arr[first].add_color("#008081")
    yield arr

    return rightmark