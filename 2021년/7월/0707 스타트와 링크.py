# 백준_14889_스타트와 링크_백트래킹_실버 3

import sys


def dfs(index, start_depth, link_depth):
    global result
    if index == n:
        if start_depth == n//2 and link_depth == n//2:
            sum_start_team = 0
            sum_link_team = 0

            for i in range(n//2):
                for j in range(i+1, n//2):
                    sum_start_team += graph[start_team[i]][start_team[j]
                                                           ] + graph[start_team[j]][start_team[i]]
                    sum_link_team += graph[link_team[i]][link_team[j]
                                                         ] + graph[link_team[j]][link_team[i]]

            result = min(result, abs(sum_start_team-sum_link_team))

        return

    start_team.append(index)
    dfs(index+1, start_depth+1, link_depth)
    start_team.pop()

    link_team.append(index)
    dfs(index+1, start_depth, link_depth+1)
    link_team.pop()


n = int(input())
result = sys.maxsize

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

start_team = []
link_team = []

dfs(0, 0, 0)

print(result)
