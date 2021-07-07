# 백준_15661_링크와 스타트_백트래킹_실버 1
# pypy3 제출시만 가능, python에서는 시간초과

import sys


def dfs(index, start_depth, link_depth):
    global result
    if index == n:
        if start_depth >= 2 and link_depth >= 2:
            sum_start_team = 0
            sum_link_team = 0

            for i in range(start_depth):
                for j in range(i+1, start_depth):
                    sum_start_team += graph[start_team[i]][start_team[j]
                                                           ] + graph[start_team[j]][start_team[i]]

            for i in range(link_depth):
                for j in range(i+1, link_depth):
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
