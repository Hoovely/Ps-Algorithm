# 백준6064_카잉 달력_수학_실버 1

import sys
input = sys.stdin.readline


def num(m, n, x, y):
    while x <= m*n:
        if (x-y) % n == 0:
            return x
        x += m
    return -1


for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))
