# 백준1912_연속합_DP_실버 2

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = [nums[0]]
sum = nums[0]
for i in range(1, n):
    if nums[i] < sum + nums[i]:
        sum += nums[i]
    else:
        sum = nums[i]
    dp.append(sum)

print(max(dp))