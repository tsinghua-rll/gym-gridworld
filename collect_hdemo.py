#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# File Name : collect_hdemo.py
# Creation Date : 12-04-2019
# Created By : Jeasine Ma [jeasinema[at]gmail[dot]com]

import gym
import gym_gridworld
import sys
import tty
import termios


class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def get():
    inkey = _Getch()
    while(1):
        k = inkey()
        if k != '':
            break
    print(k)
    if k == '\x1b[A':
        # print("up")
        return 1
    elif k == 'www':
        return 5
    elif k == '\x1b[B':
        # print("down")
        return 2
    elif k == 'sss':
        return 6
    elif k == '\x1b[C':
        # print("right")
        return 4
    elif k == 'ddd':
        return 8
    elif k == '\x1b[D':
        # print("left")
        return 3
    elif k == 'aaa':
        return 7
    elif k == '000':
        return 0
    else:
        # print("not an arrow key!")
        return None


def main():
    env = gym.make('gridworldrandom-v0')
    env.verbose = True
    r_sum = 0
    while True:
        ret = get()
        if ret is None:
            continue
        else:
            a, b, c, d = env.step(ret)
            r_sum += b
            print('r: {} r_sum: {}'.format(b, r_sum))
            if c == True:
                env.reset()
                print('game done, r: {}'.format(r_sum))
                r_sum = 0


if __name__ == '__main__':
    main()
