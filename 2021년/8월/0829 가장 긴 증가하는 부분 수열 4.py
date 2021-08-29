# 백준_14002_가장 긴 증가하는 부분 수열 4_DP_골드 4

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

idx = max(dp)
print(idx)

lis = []
for i in range(n-1, -1, -1):
    if dp[i] == idx:
        lis.append(nums[i])
        idx -= 1

lis.reverse()
print(*lis)
