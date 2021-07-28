# 백준_1535_안녕_DP_실버 2
# 오답 1

import sys
input = sys.stdin.readline

n = int(input())
hp = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(100)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(100):
        if hp[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(happy[i] + dp[i-1][j-hp[i]], dp[i-1][j])

print(dp[n][99])
