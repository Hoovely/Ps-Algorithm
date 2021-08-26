# 백준_2565_전깃줄_DP_실버 1

import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
nums.sort()

dp = [1]*n
for i in range(n):
    for j in range(i):
        if nums[i][1] > nums[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
