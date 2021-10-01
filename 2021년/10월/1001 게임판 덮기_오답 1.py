# 알고스팟_게임판 덮기_브루트포스_하
# 오답 1

import sys
input = sys.stdin.readline

dx = [[0, 1, 1], [0, 1, 0], [0, 1, 1], [0, 0, 1]]
dy = [[0, 0, -1], [0, 0, 1], [0, 0, 1], [0, 1, 1]]


def dfs():
    global result
    isFinish = True
    for i in range(n):
        for j in range(m):
            if not gamemap[i][j]:
                isFinish = False
                a, b = i, j
                break
        if not isFinish:
            break
    if isFinish:
        result += 1
        return

    for i in range(4):
        isPossible = True
        possibleDirection = []
        for j in range(3):
            x = a + dx[i][j]
            y = b + dy[i][j]
            if x < 0 or x >= n or y < 0 or y >= m:
                isPossible = False
                break
            if gamemap[x][y]:
                isPossible = False
                break
            possibleDirection.append([x, y])
        if isPossible:
            for pDx, pDy in possibleDirection:
                gamemap[pDx][pDy] = True
            dfs()
            for pDx, pDy in possibleDirection:
                gamemap[pDx][pDy] = False


for _ in range(int(input())):
    n, m = map(int, input().split())
    gamemap = []
    white_count = 0
    for _ in range(n):
        lst = list(input().rstrip())
        for i in range(m):
            if lst[i] == '#':
                lst[i] = True
            else:
                lst[i] = False
                white_count += 1
        gamemap.append(lst)
    if white_count % 3 != 0:
        print(0)
        continue

    result = 0
    dfs()
    print(result)
