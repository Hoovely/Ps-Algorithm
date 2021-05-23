# 백준11052_카드 구매하기_DP_실버 1

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(i-1, 0, -1):
        if i > 2*j:
            break
        if dp[j] + dp[i-j] > dp[i]:
            dp[i] = dp[j] + dp[i-j]


print(dp[n])