# 백준_17216_가장 큰 감소 부분 수열_DP_실버 1

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0]*n

for i in range(n):
    dp[i] = nums[i]
    for j in range(i):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], nums[i] + dp[j])
print(max(dp))
