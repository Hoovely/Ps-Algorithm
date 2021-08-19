# 백준_17142_연구소 3_bfs_골드 4
# 시간복잡도 많이 줄인버젼

import sys
from itertools import combinations
from collections import deque
read = sys.stdin.readline


def solution():
    N, M = map(int, read().split())
    _map = [list(map(int, read().split())) for _ in range(N)]
    virus_locations = []
    number_to_infect = 0
    for r in range(N):
        for c in range(N):
            if _map[r][c] == 2:
                virus_locations.append((r, c))
            elif _map[r][c] == 0:
                number_to_infect += 1

    if number_to_infect == 0:
        return 0

    combs = combinations(virus_locations, M)
    INF = 51 * 51
    temp_min_time = INF
    drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for comb in combs:
        visited = [
            [1 if _map[r][c] == 1 else 0 for c in range(N)] for r in range(N)]
        q = deque(comb)
        for r, c in comb:
            visited[r][c] = 1
        time = 0
        left_to_infect = number_to_infect
        while q:
            temp_q = deque([])
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        temp_q.append((nr, nc))
                        if _map[nr][nc] == 0:
                            left_to_infect -= 1
            time += 1
            if time > temp_min_time:
                break
            if left_to_infect == 0:
                temp_min_time = min(temp_min_time, time)
                break

            q = temp_q

    if temp_min_time == INF:
        return -1
    else:
        return temp_min_time


print(solution())
