# 백준_11055_가장 큰 증가하는 부분 수열_DP_실버 2
# n의 최대값이 1000 이기 때문에 O(n^2)인 DP로 풀이 작성

import sys
import copy
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = copy.deepcopy(nums)
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])
print(max(dp))
