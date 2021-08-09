# 백준_1992_쿼드트리_분할 정복_실버 1

import sys
input = sys.stdin.readline


def solution(m, x, y):
    color = maps[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            if color != maps[i][j]:
                result.append('(')
                solution(m//2, x, y)
                solution(m//2, x, y+m//2)
                solution(m//2, x+m//2, y)
                solution(m//2, x+m//2, y+m//2)
                result.append(')')
                return

    if color == '0':
        result.append('0')
    else:
        result.append('1')


n = int(input())
maps = []
for _ in range(n):
    maps.append(list(input().strip()))

result = []
solution(n, 0, 0)
for i in range(len(result)):
    print(result[i], end='')
