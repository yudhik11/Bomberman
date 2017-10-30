from board import *
from random import randint


class Brick():
    # it initializes the bricks on the board of the game keeping sure that the
    # situation is possible
    def __initialize(self, count, b, s):
        while count > 0:
            imp = 1
            while imp == 1:
                k = randint(3, 15)
                k = k * 4
                ki = randint(3, 15)
                ki = ki * 2
                if b[ki][k] == 0 and s[ki][k] == 0:
                    for i in range(0, 4):
                        b[ki][k + i] = 2
                        b[ki + 1][k + i] = 2
                    imp = 0
            count -= 1
