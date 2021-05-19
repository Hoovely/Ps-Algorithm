# 백준14502_연구소_bfs, 백트래킹_골드 5
# Python3 : 메모리 29080kb, 시간 3420ms
# PyPy3 : 메모리 127248kb, 시간 540ms

import sys


def bfs():
    count = 0
    graph_bfs = []

    for i in range(n):
        graph_bfs.append(graph_nm[m*i:m*(i+1)])  # 1차원 list를 2차원 list로 변환

    for i in range(n):
        for j in range(m):
            if graph_bfs[i][j] == 2:
                move.append([i, j])  # 2가 있는 좌표를 추가

    while move:  # bfs 진행
        a = move[0][0]
        b = move[0][1]
        del move[0]
        for i in range(4):
            x = a + dn[i]
            y = b + dm[i]
            if 0 <= x < n and 0 <= y < m and graph_bfs[x][y] == 0:
                graph_bfs[x][y] = 2
                move.append([x, y])

    for i in range(n):  # 0의 갯수를 count
        for j in range(m):
            if graph_bfs[i][j] == 0:
                count += 1

    return count


input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
result = []
move = []

dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

graph_nm = sum(graph, [])  # 입력받은 2차원 list를 1차원 list로 변환

for i in range(n*m):
    if graph_nm[i] == 0:  # i 자리에 0이 있을때 1 대입, 없으면 다음 좌표 실행
        graph_nm[i] = 1
    else:
        continue

    for j in range(i+1, n*m):
        if graph_nm[j] == 0:  # i+1 자리에 0이 있을때 1 대입, 없으면 다음 좌표 실행
            graph_nm[j] = 1
        else:
            continue

        for k in range(j+1, n*m):
            if graph_nm[k] == 0:  # i+2 자리에 0이 있을때 1 대입, 없으면 다음 좌표 실행
                graph_nm[k] = 1
                result.append(bfs())  # 1을 3개 넣었으므로, bfs 함수 진행
                graph_nm[k] = 0  # 0을 대입하고, 다음 경우의 수 진행
            else:
                continue

        graph_nm[j] = 0  # 0을 대입하고, 다음 경우의 수 진행

    graph_nm[i] = 0  # 0을 대입하고, 다음 경우의 수 진행

print(max(result))
