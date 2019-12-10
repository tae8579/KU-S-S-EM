import random
import numpy as np
import matplotlib
import math
import matplotlib.pyplot as plt


def checkIfInside(arr, val):
    if val in arr:
        return True
    return False


def createForest(_p=0.5, _x=10, _y=10):  # create forest
    tabForest = []
    for i in range(1, _x + 1):
        for j in range(1, _y + 1):
            if random.uniform(0, 1) < _p:
                tabForest.append({'x': i, 'y': j, 'tree': True, 'fire': False, 'burned': False})
    return tabForest


def findTree(_dict, _x, _y):  # find tree by position
    for element in _dict:
        if element['x'] == _x and element['y'] == _y:
            return element


def makeFire(_dict, _x, _y):  # fire tree by position
    for element in _dict:
        if not element['burned'] and element['x'] == _x and element['y'] == _y:
            element['fire'] = True


def startFire(_dict):  # start fire
    for element in _dict:
        if element['x'] == 1:
            element['fire'] = True


def returnFire(_dict):  # lista podpalonych drzew
    tabFire = []
    for element in _dict:
        if element['fire'] and not element['burned']:
            tabFire.append([element['x'], element['y']])
    # print tabFire
    return tabFire


def findNextFire(_arr, _dict, _size):  # znajdywanie kolejnych drzew do podpalenia
    tabMove = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    for element in _arr:
        for move in tabMove:
            x = element[0] + move[0]
            y = element[1] + move[1]
            if x >= 1 and y >= 1 and x <= _size and y <= _size:
                for d in _dict:
                    if d['x'] == x and d['y'] == y and not d['burned']:
                        d['fire'] = True


def makeBurned(_dict, _newdict):  # wypalic palace sie drzewa
    for element in _dict:
        if element['fire'] and not element['burned']:
            element['burned'] = True
            _newdict.append(element)  # list of burned trees
            # _dict.remove(element)
            # remove i dodac do innej listy  CZY TO COS PRZYSPIESZY??


def isBurning(_dict):
    a = 0
    for element in _dict:
        if element['fire'] and not element['burned']:
            a = a + 1

    if a > 0:
        return False
    else:
        return True


def showForest(_dict):
    for element in _dict:
        print
        element


def countAllTrees(_dict):
    counter = 0
    for element in _dict:
        counter = counter + 1
    print
    counter


def policzSrednia(_wyniki, _size):
    print("Srednia dla roznych prawdopodobienstw: ")
    for wynik in _wyniki:
        a = 0
        for i in wynik:
            if (i < 1):
                print
                i, ":"
            if (i > 1):
                a = a + i
        print(a / float(_size))


def isKlaster(_dict, _size):
    counter = 0
    for element in _dict:
        if element['x'] == _size:
            counter = counter + 1
    if counter > 0:
        return True
    else:
        return False


def main(_N=100, _size=10):  # pp co 0.1
    # wynik = []
    ppList = []
    klasterList = []
    for j in range(0, 10):
        pp = j / 10.0
        ppList.append(pp)
        # wynik2 = []
        klasterCounter = 0
        for j in range(0, _N):
            burnedList = []
            forest = createForest(pp, _size, _size)
            counter = 0
            isEnd = False
            startFire(forest)
            while (not isEnd):
                # counter = counter + 1
                fireList = returnFire(forest)
                makeBurned(forest, burnedList)
                findNextFire(fireList, forest, _size)
                if isBurning(forest):
                    # wynik2.append(counter)
                    if isKlaster(burnedList, _size):
                        klasterCounter = klasterCounter + 1
                    isEnd = True
        # wynik.append(wynik2)
        klasterList.append(klasterCounter / float(_N))
    # print(wynik)
    # print(ppList)
    # print(klasterList)
    plt.plot(ppList, klasterList)
    plt.show()


def main2(_N=100, _size=10):  # pp co 0.02
    ppList = []
    klasterList = []
    pp = 0.02
    while pp <= 1:
        pp = pp + 0.02
        ppList.append(pp)
        klasterCounter = 0
        for j in range(0, _N):
            burnedList = []
            forest = createForest(pp, _size, _size)
            counter = 0
            isEnd = False
            startFire(forest)
            while (not isEnd):
                fireList = returnFire(forest)
                makeBurned(forest, burnedList)
                findNextFire(fireList, forest, _size)
                if isBurning(forest):
                    if isKlaster(burnedList, _size):
                        klasterCounter = klasterCounter + 1
                    isEnd = True
        klasterList.append(klasterCounter / float(_N))
    plt.plot(ppList, klasterList)
    plt.show()


main2()