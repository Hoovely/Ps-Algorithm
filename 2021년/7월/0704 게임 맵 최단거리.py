# 프로그래머스_게임 맵 최단거리_bfs_레벨 2

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    move = [[0, 0]]
    dn = [1, -1, 0, 0]
    dm = [0, 0, 1, -1]

    while move:
        a, b = move[0][0], move[0][1]
        del move[0]
        for i in range(4):
            x = a + dn[i]
            y = b + dm[i]
            if 0 <= x < n and 0 <= y < m and maps[x][y] == 1 and visited[x][y] == 0:
                maps[x][y] = maps[a][b] + 1
                visited[x][y] = 1
                move.append([x, y])

    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))
