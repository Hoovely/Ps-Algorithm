# 백준9613_GCD 합_수학_실버 3

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    gcd = 0
    n = len(nums)
    for i in range(1, n):
        for j in range(i+1, n):
            a = max(nums[i], nums[j])
            b = min(nums[i], nums[j])
            while 1:
                temp = a % b
                if temp == 0:
                    gcd += b
                    break
                a = b
                b = temp
    print(gcd)
