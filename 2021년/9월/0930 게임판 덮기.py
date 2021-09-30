# 알고스팟_게임판 덮기_브루트포스_하

import sys
input = sys.stdin.readline

dx = [[0, 1, 1], [0, 1, 0], [0, 1, 1], [0, 0, 1]]
dy = [[0, 0, -1], [0, 0, 1], [0, 0, 1], [0, 1, 1]]


def dfs():
    global result
    isFinish = True
    for i in range(h):
        for j in range(w):
            if gamemap[i][j] == False:
                isFinish = False
                a, b = i, j
                break
        if isFinish == False:
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
            if x < 0 or x >= h or y < 0 or y >= w:
                isPossible = False
                break
            if gamemap[x][y]:
                isPossible = False
                break
            possibleDirection.append([x, y])
        if isPossible:
            for possible_x, possible_y in possibleDirection:
                gamemap[possible_x][possible_y] = True

            dfs()

            for possible_x, possible_y in possibleDirection:
                gamemap[possible_x][possible_y] = False


for _ in range(int(input())):
    h, w = map(int, input().split())
    case1 = h*w
    gamemap = []
    for i in range(h):
        lst = list(input().rstrip())
        for j in range(w):
            if lst[j] == '#':
                lst[j] = True
                case1 -= 1
            else:
                lst[j] = False
        gamemap.append(lst)
    if case1 % 3 != 0:
        print(0)
        continue

    result = 0
    dfs()
    print(result)
