# 백준_충돌의 수_ _실버 4

import sys
input = sys.stdin.readline

l, n, t = map(int, input().split())
lst = []
for _ in range(n):
    x, d = input().split()
    lst.append([int(x), d])

cnt = 0
for _ in range(t+1):
    flag = []
    for i in range(n):
        if lst[i][0] == 1 and lst[i][1] == 'L':
            lst[i][1] = 'R'
        elif lst[i][0] == l and lst[i][1] == 'R':
            lst[i][1] = 'L'
        else:
            if i in flag:
                continue
            for j in range(n):
                if lst[i][0] == lst[j][0] and lst[i][1] != lst[j][1]:
                    flag.append(j)
                    temp = lst[i][1]
                    lst[i][1] = lst[j][1]
                    lst[j][1] = temp
                    cnt += 1
                    break
            if lst[i][1] == 'R':
                lst[i][0] += 1
            else:
                lst[i][0] -= 1

print(cnt)
