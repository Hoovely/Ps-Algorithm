# 백준_1240_노드사이의 거리_트리_골드 5

import sys
input = sys.stdin.readline


def dfs(now, last, d):
    global result
    if now == last:
        result = d
        return

    for node in tree[now]:
        next = node[0]
        dist = node[1]
        if visited[next] == 0:
            visited[next] = 1
            dfs(next, last, d+dist)

        if result:
            return


n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

for i in range(m):
    x, y = map(int, input().split())
    visited = [0]*(n+1)
    result = 0
    visited[x] = 1
    dfs(x, y, 0)
    print(result)
