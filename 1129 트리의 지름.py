# 백준_1167_트리의 지름_트리_골드 3

import sys
input = sys.stdin.readline

def dfs(now, dis):
    global result, end_point
    if dis > result:
        result = dis
        end_point = now
    for next, w in tree[now]:
        if visit[next] == 0:
            visit[next] = 1
            dfs(next, dis+w)

v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    lst = list(map(int,input().split()))
    for i in range(1, len(lst)-1, 2):
        tree[lst[0]].append((lst[i], lst[i+1]))
result = 0
end_point = 0

visit = [0]*(v+1)
visit[1] = 1
dfs(1, 0)

visit = [0]*(v+1)
visit[end_point] = 1
dfs(end_point, 0)

print(result)