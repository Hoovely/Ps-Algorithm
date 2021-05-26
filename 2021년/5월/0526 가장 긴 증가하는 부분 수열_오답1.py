# 백준11053_가장 긴 증가하는 부분 수열_DP_실버 2
# 오답 1

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))