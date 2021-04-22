# 백준10816_숫자 카드 2_이분 탐색_실버 4

import sys

n = int(sys.stdin.readline())
n_nums = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_nums = list(map(int,sys.stdin.readline().split()))

result = {}

for i in n_nums:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for i in m_nums:
    if i in result:
        print(result[i], end=" ")
    else:
        print(0, end=" ")