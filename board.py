from __future__ import print_function
from termcolor import colored


class Board():
    # creates the permanent walls on the board
    def __mkbrd(self, score, s, bm):
        for i in range(0, 34):
            for j in range(0, 68):
                if i < 2 or j < 4 or i > 31 or j > 63:
                    s[i][j] = 1
                elif (i % 4) < 2 and (j % 8 < 4):
                    s[i][j] = 1
        self.ptbrd(s, bm, score)
    # prints the board

    def ptbrd(self, s, bm, score):
        cnt = 0
        for i in range(0, 34):
            for j in range(0, 68):
                if s[i][j] == 1:
                    print(colored('#', "white"), end='')
                elif bm[i][j] == 3:
                    print(colored('E', "red"), end='')
                elif bm[i][j] == 2:
                    print(colored('/', "magenta"), end='')
                    cnt += 1
                elif bm[i][j] == 1:
                    print(colored('B', "cyan"), end='')
                elif s[i][j] > 10:
                    print(colored(s[i][j] - 11, 'blue'), end='')
                elif s[i][j] == 6:
                    print(colored('e', "yellow"), end='')
                else:
                    print(' ', end='')
            print("")
        return int(cnt / 8)
