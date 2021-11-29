# 백준_1967_트리의 지름_트리_골드 4
# 오답 1

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now, dis):
    global result, end_point
    if dis > result:
        result = dis
        end_point = now
    for next, w in tree[now]:
        if visit[next] == 0:
            visit[next] = 1
            dfs(next, dis+w)
            
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[b].append((a,c))
    tree[a].append((b,c))
end_point = 0
result = 0

visit = [0]*(n+1)
visit[1] = 1
dfs(1,0)

visit = [0]*(n+1)
visit[end_point] = 1
dfs(end_point,0)

print(result)