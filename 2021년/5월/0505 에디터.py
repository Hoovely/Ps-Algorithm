# 백준1406_에디터_스택_실버 3
# insert(들어갈위치, 들어갈 값)
# del(삭제할 위치)
# insert와 del을 사용하여 풀었을때, 시간초과가 나오므로 pop, append 만을 사용하여 구현해야함

import sys

input = sys.stdin.readline

string = list(input().strip())
L = []

for _ in range(int(input())):
    cmd = input().strip()
    if cmd[0] == 'P':
        string.append(cmd[2:])
    elif cmd == 'L':
        if len(string) == 0:
            continue
        L.append(string.pop())
    elif cmd == 'D':
        if len(L) == 0:
            continue
        string.append(L.pop())
    elif cmd == 'B':
        if len(string) == 0:
            continue
        string.pop()

print(''.join(string + list(reversed(L))))