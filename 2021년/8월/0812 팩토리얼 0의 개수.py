# 백준_1676_팩토리얼 0의 개수_수학_실버 4

import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[0] = 1

for i in range(1, n+1):
    dp[i] = dp[i-1]*i

cnt = 0
lst = str(dp[n])
for i in range(1, len(lst)+1):
    if lst[-i] == '0':
        cnt += 1
    else:
        break
print(cnt)
