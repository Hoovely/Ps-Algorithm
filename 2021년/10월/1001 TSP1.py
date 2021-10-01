# 알고스팟_TPS1_구현_하

import sys
input = sys.stdin.readline
INF = sys.maxsize


def dfs(start_city, now_city, sum_cost, cnt):
    global result
    if cnt == n-1:
        result = min(result, sum_cost)
        return

    for next_city in range(n):
        if urban[now_city][next_city] == 0:
            continue
        if not visited[next_city]:
            now_cost = urban[now_city][next_city]
            if result > now_cost + sum_cost:
                visited[next_city] = True
                dfs(start_city, next_city, now_cost + sum_cost, cnt+1)
                visited[next_city] = False


for _ in range(int(input())):
    n = int(input())
    visited = [False]*n
    urban = []
    for _ in range(n):
        urban.append(list(map(float, input().split())))
    result = INF

    for i in range(n):
        visited[i] = True
        dfs(i, i, 0, 0)
        visited[i] = False

    print(result)
