# 백준_5582_공통 부분 문자열_DP_골드 5

import sys
input = sys.stdin.readline

a = ' ' + input().strip()
b = ' ' + input().strip()

a_len = len(a)
b_len = len(b)

lcs = [[0 for _ in range(b_len)] for _ in range(a_len)]

for i in range(1, a_len):
    for j in range(1, b_len):
        if i == 0 or j == 0:
            lcs[i][j] = 0
        elif a[i] == b[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = 0

max_num = 0
for lst in lcs:
    max_num = max(max_num, max(lst))

print(max_num)
