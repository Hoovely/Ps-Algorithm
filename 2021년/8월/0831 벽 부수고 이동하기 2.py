# 백준_14442_벽 부수고 이동하기 2_bfs_골드 3
# pypy 제출 메모리 316360kb, 시간 4292ms
# python3 에서는 시간 초과

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    move = deque()
    move.append([0, 0, 0])
    min_dis = sys.maxsize
    while move:
        # z는 벽을 부순 횟수를 나타내는 값이다
        x, y, z = move.popleft()

       # 그래프의 마지막 좌표에 도달하면 가장 작은 마지막 좌표의 값을 저장한다
        if x == n-1 and y == m-1:
            min_dis = min(min_dis, visited[z][x][y])

        # 현재 좌표의 4방향 탐색
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and visited[z][xx][yy] == 0:
                # 다음 좌표가 0 일때 해당 좌표 탐색
                if graph[xx][yy] == 0:
                    visited[z][xx][yy] = visited[z][x][y] + 1
                    move.append([xx, yy, z])
                # k만큼 벽을 부수지 않았고, 다음 좌표가 1일때 해당 좌표의 4방향 탐색
                elif graph[xx][yy] == 1 and z < k:
                    if visited[z+1][xx][yy] == 0:
                        visited[z+1][xx][yy] = visited[z][x][y]+1
                        move.append([xx, yy, z+1])

    if min_dis != sys.maxsize:
        return min_dis
    else:
        return -1


n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 벽을 부수고 방문했는지 알 수 있게 하기위해 visited를 3차원으로 선언한다.
visited = [[[0]*m for _ in range(n)] for _ in range(k+1)]
visited[0][0][0] = 1

# bfs 실행
print(bfs())
