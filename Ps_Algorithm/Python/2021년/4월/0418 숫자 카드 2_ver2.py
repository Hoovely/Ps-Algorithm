# 백준10816_숫자 카드 2_이분 탐색_실버 4
# 이분탐색 사용안하고 푸는법
# 메모리 108500kb 시간 952ms

import sys

n = int(sys.stdin.readline())
n_nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_nums = list(map(int, sys.stdin.readline().split()))

result = {}

for i in n_nums:
    if i in result.keys():
        result[i] += 1
    else:
        result[i] = 1

for i in m_nums:
    if i in result.keys():
        print(result[i], end=" ")
    else:  
        print(0, end=" ")
