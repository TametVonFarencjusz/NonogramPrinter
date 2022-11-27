import numpy
import math


def numberlength(a):
    count = 0
    if a < 0:
        a = abs(a)
        count += 1
    elif a == 0:
        return 1
    return count + math.log10(a + 0.1) + 1

def maxlen(vec):
    maxcount = 0

    for v in vec:
        #print(v)
        count = 0
        for ele in v:
            count += 1
            count += numberlength(ele)
        maxcount = count if count > maxcount else maxcount
    return int(maxcount) - 1

def tostring(vec, length):
    list = []
    for v in vec:
        s = str(v)
        s = s.replace('[', '')
        s = s.replace(']', '')
        s = s.replace(',', '')
        s = ' ' * (length - len(s)) + s + "  "
        list.append(s)
    return list

def tomyvector(vec):
    list = []
    last = -1
    for ele in vec:
        if ele == 0 and last != 0:
            #list.append(0)
            last = 0
        elif ele == 1 and last != 1:
            list.append(1)
            last = 1
        elif ele == 1 and last == 1:
            list[-1] += 1
            last = 1
    if len(list) == 0:
        list.append(0)
    return list


class Board:
    rows = 0
    cols = 0
    board = [[]]

    verticalVector = []
    horizontalVector = []

    def __init__(self, brd = None, pack = None):
        if brd is not None:
            self.rows = len(brd[:])
            self.cols = len(brd[0][:])
            self.board = brd
            self.GenerateNum()
        elif pack is not None:
            self.horizontalVector, self.verticalVector = pack
            self.rows, self.cols = len(self.horizontalVector), len(self.verticalVector)
            self.board = [[0 for r in range(self.cols)] for c in range(self.rows)]

    """def __init__(self, rows, cols):
        board = [[0] * cols] * rows
        verticalVector = [] * cols
        horizontalVector = [] * rows"""

    def GenerateNum(self):
        for y in range(self.rows):
            #print(self.board[y][:])
            self.horizontalVector.append(tomyvector(self.board[y][:]))

        lcl = list(map(list, zip(*self.board)))
        for x in range(self.cols):
            #print(list(lcl[x][:]))
            self.verticalVector.append(tomyvector(lcl[x][:]))

        #print(self.horizontalVector[:])
        #print(self.verticalVector[:])

    def Print(self):
        maxlenhor = maxlen(self.horizontalVector)
        maxlenver = maxlen(self.verticalVector)

        liststrhor = tostring(self.horizontalVector, maxlenhor)
        liststrver = tostring(self.verticalVector, maxlenver)

        #vertical numbers
        for c in range(maxlenver):
            print(' ' * (maxlenhor + 3), end='')
            for n in range(len(liststrver)):
                print(liststrver[n][c] + ' ', end='')
            print()
        #horizontal bar
        print(' ' * (maxlenhor + 1) + '#' * (self.cols*2+1))
        #side
        for i in range(self.rows):
            print(liststrhor[i][0:maxlenhor], end='')
            print(" #", end='')
            for l in self.board[i][:]:
                print(f" {l}", end='')
            print()
