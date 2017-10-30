from board import *
from random import randint


class Enemy():
    # do and undo function move the enemy position
    def __do(self, b, x, y):
        for i in range(0, 4):
            b[x][y + i] = 3
            b[x + 1][y + i] = 3

    def __undo(self, b, x, y):
        for i in range(0, 4):
            b[x][y + i] = 0
            b[x + 1][y + i] = 0

    # enemies are initialized using this function which make sure the
    # situation is possible
    def __initialize(self, count, b, s, em):
        while count > 0:
            imp = 1
            while imp == 1:
                k = randint(3, 15)
                k = k * 4
                ki = randint(3, 15)
                ki = ki * 2
                if b[ki][k] == 0 and s[ki][k] == 0:
                    em[count][0] = ki
                    em[count][1] = k
                    self.__do(b, ki, k)
                    imp = 0
            count -= 1
    # it defines the movement of the enemies

    def __move(self, s, bm, em, count):
        flag = 1
        while count > 0:
            imp = 1
            x = em[count][0]
            y = em[count][1]
            if x == 0 and y == 0:
                count -= 1
                continue
            imp = 1
            while imp == 1:
                k = randint(1, 10)
                k = k % 4
                if k == 0:
                    if bm[x - 2][y] == 1:
                        imp = 0
                        count = 0
                        flag = 0
                    if s[x - 2][y] != 1 and bm[x - 2][y] != 2:
                        imp = 0
                        self.__undo(bm, x, y)
                        self.__do(bm, x - 2, y)
                        em[count][0] = x - 2
                        em[count][1] = y
                elif k == 1:
                    if bm[x + 2][y] == 1:
                        imp = 0
                        count = 0
                        flag = 0
                    if s[x + 2][y] != 1 and bm[x + 2][y] != 2:
                        imp = 0
                        self.__undo(bm, x, y)
                        self.__do(bm, x + 2, y)
                        em[count][0] = x + 2
                        em[count][1] = y

                elif k == 2:
                    if bm[x][y - 4] == 1:
                        imp = 0
                        count = 0
                        flag = 0
                    if s[x][y - 4] != 1 and bm[x][y - 4] != 2:
                        imp = 0
                        self.__undo(bm, x, y)
                        self.__do(bm, x, y - 4)
                        em[count][0] = x
                        em[count][1] = y - 4

                elif k == 3:
                    if bm[x][y + 4] == 1:
                        imp = 0
                        count = 0
                        flag = 0
                    if s[x][y + 4] != 1 and bm[x][y + 4] != 2:
                        imp = 0
                        self.__undo(bm, x, y)
                        self.__do(bm, x, y + 4)
                        em[count][0] = x
                        em[count][1] = y + 4
            count -= 1
        return flag
