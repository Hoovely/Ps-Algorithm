# 백준1935_후위 표기식2_스택_실버 3
# nums의 list좌표값을 ascii코드로 표현하여 푼다.

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
S = deque(list(input().strip()))
num = []
string = []
result = 0
for _ in range(n):
    num.append(int(input()))

while S:
    x = S.popleft()
    if x == '+' or x == '-' or x == '/' or x == '*':
        a = string.pop()
        b = string.pop()

        if str(a).isalpha():
            a = num[ord(a) - ord('A')]
        if str(b).isalpha():
            b = num[ord(b) - ord('A')]

        if x == '+':
            result = b + a
        elif x == '-':
            result = b - a
        elif x == '/':
            result = b / a
        elif x == '*':
            result = b * a
        string.append(result)

    else:
        string.append(x)

print(format(result, ".2f"))
