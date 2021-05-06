# 백준1406_에디터_스택_실버 3
# 오답 1

import sys

input = sys.stdin.readline

S = list(input().strip())
L = []

for _ in range(int(input())):
    cmd = input().strip()

    if cmd == 'L':
        if len(S) == 0:
            continue
        L.append(S.pop())

    elif cmd == 'D':
        if len(L) == 0:
            continue
        S.append(L.pop())

    elif cmd == 'B':
        if len(S) == 0:
            continue
        S.pop()

    else:
        S.append(cmd[2:])

print(''.join(S + list(reversed(L))))
