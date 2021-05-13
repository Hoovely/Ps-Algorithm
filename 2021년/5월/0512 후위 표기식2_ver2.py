# 백준1935_후위 표기식2_스택_실버 3
# deque 사용안하는 풀이방법

import sys

input = sys.stdin.readline

n = int(input())
S = list(input().strip())
nums = []
string = []
result = 0
for _ in range(n):
    nums.append(int(input()))

for s in S:
    if 'A' <= s <= 'Z':
        string.append(nums[ord(s) - ord('A')])
    else:
        a = string.pop()
        b = string.pop()

        if s == '+':
            result = b + a
        elif s == '-':
            result = b - a
        elif s == '/':
            result = b / a
        elif s == '*':
            result = b * a
        
        string.append(result)

print(format(result, ".2f"))
