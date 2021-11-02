# 백준_2293_동전 1_DP_실버 1

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] += dp[j-coin[i]]

print(dp[k])
