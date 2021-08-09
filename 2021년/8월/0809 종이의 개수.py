# 백준_1780_종이의 개수_분할 정복_실버 2

import sys
input = sys.stdin.readline


def paper(m, x, y):
    global minus, zero, one
    number = maps[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            if number != maps[i][j]:
                for k in range(3):
                    paper(m//3, x+k*m//3, y)
                    paper(m//3, x+k*m//3, y+m//3)
                    paper(m//3, x+k*m//3, y+m//3*2)
                return

    if number == -1:
        minus += 1
    elif number == 0:
        zero += 1
    else:
        one += 1


n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

minus, zero, one = 0, 0, 0

paper(n, 0, 0)

print(minus)
print(zero)
print(one)
