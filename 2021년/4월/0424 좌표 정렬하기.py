# 백준11650_좌표 정렬하기_정렬_실버 5

import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    nums.append([a,b])

nums.sort()
for i in nums:
    for j in i:
        print(j, end = " ")
    print()
