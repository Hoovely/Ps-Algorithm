# 백준_1967_트리의 지름_트리_골드 4

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

def dfs(now, dis):
    global result, end_point
    if dis > result:
        result = dis
        end_point = now
    for next, w in tree[now]:
        if visited[next] == 0:
            visited[next] = 1
            dfs(next, dis+w)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[b].append((a,c))
    tree[a].append((b,c))
result = 0
end_point = 0

visited = [0]*(n+1)
visited[1] = 1
dfs(1,0)

visited = [0]*(n+1)
visited[end_point] = 1
dfs(end_point,0)

print(result)