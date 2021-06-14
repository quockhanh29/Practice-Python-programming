#coding: utf-8

import random

FORTUNE_CANDIDTES =['大吉','中吉','小吉','吉','末吉', '凶', '大凶']

fortune_max = len(FORTUNE_CANDIDTES) - 1

fortune = random.randint(0, fortune_max)

print(FORTUNE_CANDIDTES[fortune])

