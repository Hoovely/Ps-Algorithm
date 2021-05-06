# 백준1874_스택 수열_스택_실버 3

import sys

input = sys.stdin.readline

n = int(input())
nums = []
result = []
i = 1
flag = 0
for _ in range(n):
    num = int(input())
    while i <= num:
        result.append('+')
        nums.append(i)
        i += 1

    if num == nums[-1]:
        nums.pop()
        result.append('-')
    else:
        flag = 1

if flag == 1:
    print("NO")
else:
    for i in result:
        print(i)
