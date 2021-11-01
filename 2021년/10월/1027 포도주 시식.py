# 백준_2156_포도주 시식_DP_실버 1

import sys
input = sys.stdin.readline

n = int(input())
grape = []
for _ in range(n):
    grape.append(int(input()))
dp = [0]*n

if n < 3:
    print(sum(grape))
else:
    dp[0] = grape[0]
    dp[1] = grape[0] + grape[1]
    dp[2] = max(grape[1]+grape[2], grape[0]+grape[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i-2]+grape[i], dp[i-3]+grape[i]+grape[i-1], dp[i-1])

    print(dp[-1])
