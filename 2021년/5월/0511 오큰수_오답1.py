# 백준17298_오큰수_스택_골드 4
# 오답 1

n = int(input())
nums = list(map(int,input().split()))
stack = []
result = [-1]*n
for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]
    stack.append(i)
print(*result)