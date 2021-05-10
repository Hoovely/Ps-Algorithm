# 백준17298_오등큰수_스택_골드 3

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
result = [-1]*n
nums_dict = Counter(nums)
stack = []

for i in range(len(nums)):
    while stack and nums_dict[nums[stack[-1]]] < nums_dict[nums[i]]:
        result[stack.pop()] = nums[i]
    stack.append(i)

for i in result:
    print(i,end=' ')