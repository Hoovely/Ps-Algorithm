# 백준1935_후위 표기식2_스택_실버 3

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
S = deque(list(input().strip()))
num = deque()
i = 0
while S:
    if S[0] == '+' or S[0] == '-' or S[0] == '/' or S[0] == '*':
        if S[0] == '+':
            num.append(num.pop()+num.pop())
            S.popleft()
        elif S[0] == '-':
            num.append((-1)*num.pop()+num.pop())
            S.popleft()
        elif S[0] == '/':
            num.append(1/num.pop()*num.pop())
            S.popleft()
        elif S[0] == '*':
            num.append(num.pop()*num.pop())
            S.popleft()

    else:
        if i < n:
            x = int(input())
        num.append(x)
        S.popleft()
        i += 1

print(format(num[0], ".2f"))
