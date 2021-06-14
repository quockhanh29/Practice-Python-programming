#coding: utf-8

import random

fortune = random.randint(0,4)

if fortune == 0:
    print('大吉')
elif fortune == 1:
    print('中吉')
elif fortune == 2:
    print('小吉')
elif fortune == 3:
    print('凶')
elif fortune == 4:
    print('大凶')
    