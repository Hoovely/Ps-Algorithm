# 백준_10973_이전 순열_수학_실버 3

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
find = False

for i in range(n-1, 0, -1):
    if nums[i-1] > nums[i]:
        for j in range(n-1, 0, -1):
            if nums[i-1] > nums[j]:
                nums[i-1], nums[j] = nums[j], nums[i-1]
                nums = nums[:i] + sorted(nums[i:], reverse=True)
                find = True
                break
    if find:
        print(*nums)
        break

if not find:
    print(-1)
