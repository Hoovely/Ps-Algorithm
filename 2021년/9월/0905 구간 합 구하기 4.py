# 백준_11659_구간 합 구하기 4_누적합_실버 3

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
dp = [0]

for i in range(1, n+1):
    dp.append(dp[i-1] + nums[i])

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j]-dp[i-1])
