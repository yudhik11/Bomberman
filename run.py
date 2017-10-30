from __future__ import print_function
from bbm import *
from getchunix import *
from alarmexception import *
from enemy import *
from brick import *
from bomb import *

import sys
import copy
import signal
import time
import os

board = Board()
brick = Brick()
enemy = Enemy()
getch = GetchUnix()
bomb = Bomb()
bbm = bbm()


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


lives = 3
level = 4
lvl_no = an = ans = 0
while lvl_no <= level:
    lvl_no += 1
    # board on which the permanent walls and bomb is saved(including the
    # explosion)
    s = [[0 for _ in range(76)] for j in range(0, 42)]
    # board on which the temporary bricks and enemies are stored and also the
    # bomberman
    em = [[0 for _ in range(10)] for j in range(0, 20)]
    bm = copy.deepcopy(s)
    board._Board__mkbrd(0, s, bm)
    mvx = 2  # initial position of the bomberman
    mvy = 4
    count = 2 + lvl_no * 2
    total_bricks = 7 + lvl_no * 3
    # initializes the bricks on board
    brick._Brick__initialize(total_bricks, bm, s)
    # initializes the enemies on board
    enemy._Enemy__initialize(count, bm, s, em)
    an += ans
    bomyb = ans = bombx = spawn = 0
    counter = -1
    prt = time.time()
    while lives > 0:  # game can be played if you have more than 1 life left
        if spawn == 0:
            mvx = 2
            mvy = 4
            bbm._bbm__make(2, 4, bm)
            spawn = 1
        bmb = 0
        inp = input_to()
        # bomberman tries to move in upward direction
        if inp == 'w':
            tmpp = bbm.move_up(s, bm, mvx, mvy)
            if tmpp == 1:
                mvx -= 2
            if tmpp == 2:
                spawn = 0
                lives -= 1
        # bomberman tries to move in downward direction
        if inp == 's':
            tmpp = bbm.move_down(s, bm, mvx, mvy)
            if tmpp == 1:
                mvx += 2
            if tmpp == 2:
                spawn = 0
                lives -= 1
        # bomberman tries to move in left direction
        if inp == 'a':
            tmpp = bbm.move_left(s, bm, mvx, mvy)
            if tmpp == 1:
                mvy -= 4
            if tmpp == 2:
                spawn = 0
                lives -= 1
        # bomberman tries to move in right direction
        if inp == 'd':
            tmpp = bbm.move_right(s, bm, mvx, mvy)
            if tmpp == 1:
                mvy += 4
            if tmpp == 2:
                spawn = 0
                lives -= 1
        # the game ends as soon as the user presses q
        if inp == 'q':
            exit()
        # it ensures the bomb can be planted only if 'b' is pressed and their
        # is no other bomb planted
        if counter == -1 and inp == 'b':
            counter = 3
            bombx = mvx
            bomby = mvy
        # the bomb is planted with timer set to 3
        if counter == 3:
            bomb._Bomb__plant(s, bm, bombx, bomby, counter)
        # enemies and bomb have the time cycle of 1 second in consecutive
        # movements and timer respectively
        if time.time() - prt >= 1:
            # it ensures the timer is displayed on the bomb
            if counter > 0:
                counter -= 1
                bomb._Bomb__plant(s, bm, bombx, bomby, counter)
            prt = time.time()
            # keeps check if the enemy has killed the bomberman or not
            fl = enemy._Enemy__move(s, bm, em, count)
            if fl == 0:
                lives -= 1
                spawn = 0
        # time for bomb to explode
        if counter == 0 and spawn == 1:
            counter -= 1
            bomb._Bomb__explode(s, bm, bombx, bomby)
            os.system('tput reset')
            board.ptbrd(s, bm, 0)
            # checks if the bomberman is alive or not after the bomb explosion
            dead = bomb._Bomb__func(s, em, bm, bombx, bomby, count)
            bmb = 1
            if dead == 1:
                spawn = 0
                # if the bomberman dies in bomb explosion lives are reduced by
                # one
                lives -= 1
                os.system('tput reset')
                bl = board.ptbrd(s, bm, 0)
                scr = bbm._bbm__score(em, count)
                ans = (total_bricks - bl) * 20 + (count - scr) * 100
                print(
                    "lives : ",
                    lives,
                    "enemies left : ",
                    scr,
                    " score: ",
                    an + ans)
                print("Current level : ", lvl_no)
                print("Died in bomb explosion")
        # if no more enemies are left ,then it is time for next level to start
        if bbm._bbm__score(em, count) == 0:
            break
        # it ensures that if the bomb is exploded than the explosion should be
        # visible
        if bmb == 0:
            os.system('tput reset')
            bl = board.ptbrd(s, bm, 0)
            scr = bbm._bbm__score(em, count)
            ans = (total_bricks - bl) * 20 + (count - scr) * 100
            print("Current level : ", lvl_no)
            print(
                "lives : ",
                lives,
                "enemies left : ",
                scr,
                " score: ",
                ans + an)
        # game quits itself if bomberman doesn't have a life
        if lives < 1:
            exit()
