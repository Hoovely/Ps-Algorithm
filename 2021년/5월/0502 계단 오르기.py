# 백준2579_계단 오르기_DP_실버 3
# 맨 마지막 계단은 꼭 밟아야된다 ==> 뒤에서 부터 연산 준비

import sys

input = sys.stdin.readline
n = int(input())
nums = []
dp = []
for _ in range(n):
    nums.append(int(input()))
if n > 3:    
    dp.append(nums[0])
    dp.append(max(nums[1], nums[0] + nums[1]))
    dp.append(max(nums[0] + nums[2], nums[1] + nums[2]))
    for i in range(3, n):
        dp.append(max(nums[i] + nums[i-1] + dp[i-3], nums[i] + dp[i-2]))
elif n == 3:
    dp.append(nums[0])
    dp.append(max(nums[1], nums[0] + nums[1]))
    dp.append(max(nums[0] + nums[2], nums[1] + nums[2]))
elif n == 2:
    dp.append(nums[0])
    dp.append(max(nums[1], nums[0] + nums[1]))
elif n == 1:
    dp.append(nums[0])

print(dp[-1])
