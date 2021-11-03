# 백준_2293_동전 1_DP_실버 1
# 오답 1

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1

for i in range(n):
    for j in range(money[i], k+1):
        dp[j] += dp[j-money[i]]

print(dp[k])

