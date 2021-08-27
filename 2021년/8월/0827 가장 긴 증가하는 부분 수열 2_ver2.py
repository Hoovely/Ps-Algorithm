# 백준_12015_가장 긴 증가하는 부분 수열 2_이분 탐색_골드 2
# 이분 탐색 직접 구현한 버젼

import sys
input = sys.stdin.readline


def binary_search(left, right, target):
    while left <= right:
        mid = (left+right)//2
        if dp[mid] == target:
            return mid
        if dp[mid] > target:
            right = mid - 1
        elif dp[mid] < target:
            left = mid + 1

    return left


n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]

for i in range(n):
    if dp[-1] < nums[i]:
        dp.append(nums[i])
    else:
        idx = binary_search(0, len(dp)-1, nums[i])
        dp[idx] = nums[i]

print(len(dp))
