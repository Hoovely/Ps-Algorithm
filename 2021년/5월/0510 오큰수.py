# 백준17298_오큰수_스택_골드 4
# n의 최대값이 100만이라서 O(n)으로 풀어야함
# index값과 num의 값을 넣은 2차 list로 구현해서 sort로 풀어볼랬으나 시간초과
# result에 값을 넣은다음 대입하는 방법으로 변경 

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
result = [-1]*n
stack = []
for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]
    stack.append(i)

for i in result:
    print(i, end=' ')


