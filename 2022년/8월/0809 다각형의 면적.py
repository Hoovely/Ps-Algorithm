# 백준_다각형의 면적_ _골드 5

import sys
input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0
for i in range(n):
    if i == n-1:
        result += graph[i][0]*graph[0][1] - graph[i][1]*graph[0][0]
    else:
        result += graph[i][0]*graph[i+1][1] - graph[i][1]*graph[i+1][0]

print(round(abs(result)/2, 1))
