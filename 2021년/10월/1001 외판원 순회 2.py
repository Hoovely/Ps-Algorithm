# 백준_10971_외판원 순회 2_브루트포스_실버 2

import sys
INF = sys.maxsize


def dfs(start_city, now_city, sum_cost, cnt):
    global result
    if cnt == n and start_city == now_city:
        result = min(result, sum_cost)
        return

    for next_city in range(n):
        if urban[now_city][next_city] == 0:
            continue
        if visited[next_city] == 0:
            now_cost = urban[now_city][next_city]
            if result > now_cost + sum_cost:

                visited[next_city] = 1
                dfs(start_city, next_city, sum_cost + now_cost, cnt+1)
                visited[next_city] = 0


n = int(input())
urban = []
for i in range(n):
    urban.append(list(map(int, input().split())))
visited = [0]*n
cost = []
result = INF
for i in range(n):
    dfs(i, i, 0, 0)
print(result)
