# 백준17087_숨바꼭질 6_수학_실버 1
# abs(s-n)의 최솟값을 구하는 문제
# O(n)으로 풀어야하는 문제

import sys


def GCD(a, b):
    while 1:
        temp = a % b
        if temp == 0:
            return b
        a = b
        b = temp


input = sys.stdin.readline

n, s = map(int, input().split())
n_lst = list(map(int, input().split()))
# result = []
for i in range(len(n_lst)):
    n_lst[i] = abs(s-n_lst[i])
if n == 1:
    # result.append(n_lst[0])
    result = n_lst[0]
else:
    result = min(n_lst)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         a = max(n_lst[i], n_lst[j])
    #         b = min(n_lst[i], n_lst[j])
    #         result.append(GCD(a, b))
print(result)
