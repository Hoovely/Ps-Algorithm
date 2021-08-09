# 백준_2630_색종이 만들기_분할 정복_실버 3

import sys
input = sys.stdin.readline


def paper(m, x, y):
    global blue, white
    color = maps[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            if color != maps[i][j]:
                paper(m//2, x, y)
                paper(m//2, x, y+m//2)
                paper(m//2, x+m//2, y)
                paper(m//2, x+m//2, y+m//2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

blue, white = 0, 0
paper(n, 0, 0)
print(white)
print(blue)
