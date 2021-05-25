# 백준11052_카드 구매하기_DP_실버 1
# 오답 2

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(1, i//2 + 1):
        if dp[i] < dp[i-j] + dp[j]:
            dp[i] = dp[i-j] + dp[j]

print(dp[n])