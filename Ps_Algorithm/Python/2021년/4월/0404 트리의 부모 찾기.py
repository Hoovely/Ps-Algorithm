# 백준11725_트리의 부모 찾기_dfs_실버 2
# 처음엔 graph[x][y] = 1, graph[y][x] = 1 사용해서 풀어봤으나 메모리초과
# 질문 검색 좀 보다가 graph[x].append(y), graph[y].append(x) 사용해서 풀어보니까 런타임 에러
# sys.setrecursionlimit() 사용하여 최대 재귀횟수 늘려줘서 해결함
# python 제출시 sys.setrecursionlimit(10**6)
# pypy 제출시 sys.setrecursionlimit(10**5)

import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 늘려주는 함수, 런타임 에러 방지

def dfs(i):

    for j in graph[i]:
        if visited[j] == 0:
            visited[j] = 1
            result[j] = i
            dfs(j)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
result = [0]*(n+1)
visited = [0]*(n+1)

for i in range(n-1):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited[1] = 1
dfs(1)

for i in range(2, n+1):
    print(result[i])
