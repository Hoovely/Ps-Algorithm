# 백준_1629_곱셈_분할 정복_실버 1

import sys
sys.setrecursionlimit(10**8)


def powpow(x, y):
    if y == 1:
        return x
    elif y % 2 == 1:
        return powpow(x, y-1)*x
    elif y % 2 == 0:
        half = powpow(x, y//2) % c
        return (half*half) % c


a, b, c = map(int, input().split())
if b == 0:
    print(1)
else:
    print(powpow(a, b) % c)
