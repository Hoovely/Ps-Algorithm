# 백준_16947_서울 지하철 2호선_DFS_골드 3

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(now_idx, cnt, start):
    global flag
    for i in range(len(graph[now_idx])):
        next_idx = graph[now_idx][i]
        if visited[next_idx] == 0:
            visited[next_idx] = 1
            dfs(next_idx, cnt+1, start)

            if flag:
                check[now_idx] = 0
                return

        else:
            if cnt >= 3 and next_idx == start:
                flag = 1
                check[now_idx] = 0
                return


def sum_distance(now_idx, distance):
    for i in range(len(graph[now_idx])):
        next_idx = graph[now_idx][i]

        if visited[next_idx] != 0:
            continue

        if check[next_idx] == 0:
            print(distance, end=' ')
            return
        else:
            visited[next_idx] = 1
            sum_distance(next_idx, distance+1)


n = int(input())
graph = [[] for _ in range(n+1)]
check = [1]*(n+1)
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

flag = 0
for i in range(1, n+1):
    visited = [0]*(n+1)
    visited[i] = 1
    dfs(i, 1, i)
    if flag:
        break

for i in range(1, n+1):
    if check[i] == 0:
        print(0, end=' ')
    else:
        visited = [0]*(n+1)
        visited[i] = 1
        sum_distance(i, 1)
