# 백준_1365_꼬인 전깃줄_이분 탐색_골드 2

import sys
input = sys.stdin.readline


def binary_search(left, right, target):
    while left <= right:
        mid = (left+right)//2
        if dp[mid] == target:
            return target
        elif dp[mid] < target:
            left = mid + 1
        elif dp[mid] > target:
            right = mid - 1

    return left


n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [nums[1]]

for i in range(2, n+1):
    if dp[-1] < nums[i]:
        dp.append(nums[i])
    else:
        idx = binary_search(0, len(dp)-1, nums[i])
        dp[idx] = nums[i]

print(n-len(dp))
