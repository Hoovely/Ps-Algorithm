# 백준6064_카잉 달력_수학_실버 1
# 오답 1

import sys
input = sys.stdin.readline


def result(m, n, x, y):
    while m*n >= x:
        if (x-y) % n == 0:
            return x
        x += m
    return -1


for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    print(result(m, n, x, y))
