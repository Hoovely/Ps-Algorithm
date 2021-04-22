# 백준11725_트리의 부모 찾기_dfs_실버 2

import sys
sys.setrecursionlimit(10**6)

def dfs(i):
    
    for j in tree[i]:
        if visited[j] == 0:
            visited[j] = 1
            result[j] = i
            dfs(j)

n = int(input())
tree = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
result = [0]*(n+1)
for i in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited[1] = 1
dfs(1)
for i in range(2, n+1):
    print(result[i])