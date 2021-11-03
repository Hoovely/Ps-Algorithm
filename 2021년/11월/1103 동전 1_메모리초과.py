# 백준_2293_동전 1_DP_실버 1

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n)]
for i in range(n):
    dp[i][0] = 1
    for j in range(k+1):
        if i == 0:
            if j >= money[0]:
                dp[0][j] = dp[0][j-money[0]]
        else:
            if j >= money[i]:
                dp[i][j] = dp[i-1][j] + dp[i][j-money[i]]
            else:
                dp[i][j] = dp[i-1][j]

print(dp[-1][-1])