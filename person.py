class Person():
    # bomberman moves left
    def move_left(self, s, bm, x, y):
        if s[x][y - 4] != 1 and (bm[x][y - 4] == 0 or bm[x][y - 4] == 3):
            for i in range(0, 4):
                bm[x][y + i] = 0
                bm[x + 1][y + i] = 0
            if bm[x][y - 4] == 3:
                return 2
            for i in range(0, 4):
                bm[x][y - 4 + i] = 1
                bm[x + 1][y - 4 + i] = 1
            return 1
        return 0
    # bomberman moves right

    def move_right(self, s, bm, x, y):
        if s[x][y + 4] != 1 and (bm[x][y + 4] == 0 or bm[x][y + 4] == 3):
            for i in range(0, 4):
                bm[x][y + i] = 0
                bm[x + 1][y + i] = 0
            if bm[x][y + 4] == 3:
                return 2
            for i in range(0, 4):
                bm[x][y + 4 + i] = 1
                bm[x + 1][y + 4 + i] = 1
            return 1
        return 0
    # bomberman moves up

    def move_up(self, s, bm, x, y):
        if s[x - 2][y] != 1 and (bm[x - 2][y] == 0 or bm[x - 2][y] == 3):
            for i in range(0, 4):
                bm[x][y + i] = 0
                bm[x + 1][y + i] = 0
            if bm[x - 2][y] == 3:
                return 2
            for i in range(0, 4):
                bm[x - 1][y + i] = 1
                bm[x - 2][y + i] = 1
            return 1
        return 0
    # bomberman moves down

    def move_down(self, s, bm, x, y):
        if s[x + 2][y] != 1 and (bm[x + 2][y] == 0 or bm[x + 2][y] == 3):
            for i in range(0, 4):
                bm[x][y + i] = 0
                bm[x + 1][y + i] = 0
            if bm[x + 2][y] == 3:
                return 2
            for i in range(0, 4):
                bm[x + 2][y + i] = 1
                bm[x + 3][y + i] = 1
            return 1
        return 0
