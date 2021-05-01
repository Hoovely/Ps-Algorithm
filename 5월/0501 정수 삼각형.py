# 백준1932_정수 삼각형_DP_실버 1

import sys

n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n):
    for j in range(len(nums[i])):
        if j == 0:
            nums[i][j] += nums[i-1][j]
        elif j == i:
            nums[i][j] += nums[i-1][j-1]
        else:
            nums[i][j] += max(nums[i-1][j], nums[i-1][j-1]) 
print(max(nums[-1]))