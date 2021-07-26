# 백준_9465_스티커_DP_실버 2

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = []
    dp.append(list(map(int, input().split())))
    dp.append(list(map(int, input().split())))

    for i in range(1, n):
        if i == 1:
            dp[0][1] += dp[1][0]
            dp[1][1] += dp[0][0]
        else:
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
