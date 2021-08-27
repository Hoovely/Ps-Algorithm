# 백준_1365_꼬인 전깃줄_이분 탐색_골드 2

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = []

for i in range(1, n+1):
    k = bisect_left(dp, nums[i])
    if k >= len(dp):
        dp.append(nums[i])
    else:
        dp[k] = nums[i]

print(n-len(dp))
