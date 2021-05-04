# 백준2579_계단 오르기_DP_실버 3
# 오답 1

import sys

n = int(input())
nums = []
dp = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

if n > 3:
    dp.append(nums[0])
    dp.append(nums[0] + nums[1])
    dp.append(max(nums[1] + nums[2], nums[0] + nums[2]))
    for i in range(3, n):
        dp.append(max(nums[i] + nums[i-1] + dp[i-3], nums[i] + dp[i-2]))
elif n == 1:
    dp.append(nums[0])
elif n == 2:
    dp.append(nums[0] + nums[1])
elif n == 3:
    dp.append(max(nums[0] + nums[2], nums[1] + nums[2]))

print(dp[-1])
