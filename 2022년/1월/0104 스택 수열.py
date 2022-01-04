# 백준_1874_스택 수열_스택_실버 3

import sys
input = sys.stdin.readline

n = int(input())
nums = []
stack = []
i = 1
flag = 0
for _ in range(n):
    num = int(input())
    while i <= num:
        stack.append('+')
        nums.append(i)
        i += 1
    
    if num == nums[-1]:
        nums.pop()
        stack.append('-')
    else:
        flag = 1

if flag:
    print("NO")
else:
    for i in stack:
        print(i)


