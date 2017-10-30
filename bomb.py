class Bomb():
    def __do(self, s, x, y):
        for j in range(0, 4):
            s[x][y + j] = 6
            s[x + 1][y + j] = 6

    class Undo(object):
        def undo(self, s, x, y):
            for j in range(0, 4):
                s[x][y + j] = 0
                s[x + 1][y + j] = 0

    class bundo(object):
        def undo(self, bm, x, y):
            for j in range(0, 4):
                bm[x][y + j] = 0
                bm[x + 1][y + j] = 0

    def __plant(self, s, bm, mvx, mvy, counter):
        for i in range(0, 4):
            s[mvx][mvy + i] = 10 + counter
            s[mvx + 1][mvy + i] = 10 + counter

    def __explode(self, s, bm, x, y):
        for i in range(0, 2):
            if s[x - 2 * i][y] != 1:
                self.__do(s, x - 2 * i, y)
            else:
                break
            if bm[x - 2 * i][y] == 2:  # brick
                break
        for i in range(0, 2):
            if s[x + 2 * i][y] != 1:
                self.__do(s, x + 2 * i, y)
            else:
                break
            if bm[x + 2 * i][y] == 2:
                break
        for i in range(0, 2):
            if s[x][y - 4 * i] != 1:
                self.__do(s, x, y - 4 * i)
            else:
                break
            if bm[x][y - 4 * i] == 2:
                break
        for i in range(0, 2):
            if s[x][y + 4 * i] != 1:
                self.__do(s, x, y + 4 * i)
            else:
                break
            if bm[x][y + 4 * i] == 2:
                break

    __mobj = Undo()
    __bmobj = bundo()

    def callundo(self, funct, s, x, y):
        funct.undo(s, x, y)

    def __func(self, s, em, bm, x, y, count):
        flag = 0
        for i in range(0, 3):
            if s[x - 2 * i][y] == 6:
                self.callundo(self.__mobj, s, x - 2 * i, y)
                if bm[x - 2 * i][y] > 0:
                    if bm[x - 2 * i][y] == 1:
                        flag = 1
                    if bm[x - 2 * i][y] == 3:
                        for j in range(0 + 1, count + 1):
                            if em[j][0] == x - 2 * i and em[j][1] == y:
                                em[j][0] = 0
                                em[j][1] = 0
                    self.callundo(self.__bmobj, bm, x - 2 * i, y)
            else:
                break
        for i in range(1, 3):
            if s[x + 2 * i][y] == 6:
                self.callundo(self.__mobj, s, x + 2 * i, y)
                if bm[x + 2 * i][y] > 0:
                    if bm[x + 2 * i][y] == 1:
                        flag = 1
                    if bm[x + 2 * i][y] == 3:
                        for j in range(0 + 1, count + 1):
                            if em[j][0] == x + 2 * i and em[j][1] == y:
                                em[j][0] = 0
                                em[j][1] = 0

                    self.callundo(self.__bmobj, bm, x + 2 * i, y)
            else:
                break
        for i in range(1, 3):
            if s[x][y - 4 * i] == 6:
                self.callundo(self.__mobj, s, x, y - 4 * i)
                if bm[x][y - 4 * i] > 0:
                    if bm[x][y - 4 * i] == 1:
                        flag = 1
                    if bm[x][y - 4 * i] == 3:
                        for j in range(1, count + 1):
                            if em[j][0] == x and em[j][1] == y - 4 * i:
                                em[j][0] = 0
                                em[j][1] = 0

                    self.callundo(self.__bmobj, bm, x, y - 4 * i)
            else:
                break
        for i in range(1, 3):
            if s[x][y + 4 * i] == 6:
                self.callundo(self.__mobj, s, x, y + 4 * i)
                if bm[x][y + 4 * i] > 0:
                    if bm[x][y + 4 * i] == 1:
                        flag = 1
                    if bm[x][y + 4 * i] == 3:
                        for j in range(0 + 1, count + 1):
                            if em[j][0] == x and em[j][1] == y + 4 * i:
                                em[j][0] = 0
                                em[j][1] = 0

                    self.callundo(self.__bmobj, bm, x, y + 4 * i)
            else:
                break
        return flag
