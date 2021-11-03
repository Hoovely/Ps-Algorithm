# 백준_9084_동전_DP_골드 5

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    dp = [[0 for _ in range(m+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
        for j in range(m+1):
            if i == 0:
                if j >= coin[i]:
                    dp[i][j] = dp[i][j-coin[i]]
            else:
                if j >= coin[i]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coin[i]]
                else:
                    dp[i][j] = dp[i-1][j]

    print(dp[n-1][m])
