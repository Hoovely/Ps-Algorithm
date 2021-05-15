# 백준17087_숨바꼭질 6_수학_실버 1
# abs(s-n)의 최솟값을 구하는 문제
# O(n)으로 풀어야하는 문제

import sys


def GCD(a, b):
    while b:
        mod = a % b
        a = b
        b = mod
    return a


input = sys.stdin.readline

n, s = map(int, input().split())
n_lst = list(map(int, input().split()))
for i in range(len(n_lst)):
    n_lst[i] = abs(s-n_lst[i])
d = min(n_lst)
for i in range(len(n_lst)):
    d = GCD(n_lst[i], d)
print(d)
