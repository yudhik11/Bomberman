from board import *
from person import *


class bbm(Person):
    # it initializes the bomberman
    def __make(self, i, j, b):
        for k in range(0, 4):
            b[i][j + k] = 1
            b[i + 1][j + k] = 1

    def __score(self, em, count):
        cnt = 0
        while count > 0:
            if em[count][0] != 0 and em[count][1] != 0:
                cnt += 1
            count -= 1
        return cnt
