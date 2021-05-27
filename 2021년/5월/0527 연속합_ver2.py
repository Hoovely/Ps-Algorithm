# 백준1912_연속합_DP_실버 2

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

for i in range(1, n):
    nums[i] = max(nums[i], nums[i-1] + nums[i])
print(max(nums))