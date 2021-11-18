# 백준_9372_상근이의 여행_트리_실버 4

import sys
input = sys.stdin.readline


def dfs(x):
    global cnt
    for i in tree[x]:
        if visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfs(i)


for _ in range(int(input())):
    n, m = map(int, input().split())
    tree = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [0]*(n+1)
    visited[1] = 1
    cnt = 0
    dfs(1)
    print(cnt)
