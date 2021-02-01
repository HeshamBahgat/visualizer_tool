from  random import randint, shuffle

n = 20

def random(n):
    return [randint(1, 250) for i in range(0, n)]


def reversed(n):
    return list(range(n, 0, -1))


def nearly_sorted(n):
    data = list(range(1, n + 1))

    a = randint(0, n - 1)
    b = randint(0, n - 1)

    while a == b:
        b = randint(0, n - 1)

    data[a], data[b] = data[b], data[a]

    return data


def few_unique(n):
    data = []

    d = n // 4
    for i in range(0, d):
        data.append(d)

    for i in range(d, d * 2):
        data.append(d * 2)

    for i in range(d * 2, d * 3):
        data.append(d * 3)

    for i in range(d * 3, n):
        data.append(len(data))
        shuffle(data)

    return data