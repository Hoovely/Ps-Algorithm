# 백준14500_테트로미노_브루트포스_골드 5
# 오답 1

import sys
input = sys.stdin.readline


def bfs(i, j):
    global result
    for k in range(19):
        count = 0
        for l in range(4):
            x = i + tetromino[k][l][0]
            y = j + tetromino[k][l][1]
            if 0 <= x < n and 0 <= y < m:
                count += graph[x][y]
            else:
                count = 0
                break
        if result < count:
            result = count


n, m = map(int, input().split())
graph = []
result = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

tetromino = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],  # ㅡ자_case1
    [[0, 0], [1, 0], [2, 0], [3, 0]],  # ㅡ자_case2

    [[0, 0], [0, 1], [1, 0], [1, 1]],  # 정사각형_case1

    [[0, 0], [0, 1], [0, 2], [1, 0]],  # L자_case1
    [[0, 0], [0, 1], [0, 2], [1, 2]],  # L자_case2
    [[0, 0], [1, 0], [1, 1], [1, 2]],  # L자_case3
    [[0, 2], [1, 0], [1, 1], [1, 2]],  # L자_case4
    [[0, 0], [1, 0], [2, 0], [2, 1]],  # L자_case5
    [[0, 0], [1, 0], [2, 0], [0, 1]],  # L자_case6
    [[0, 0], [0, 1], [1, 1], [2, 1]],  # L자_case7
    [[0, 1], [1, 1], [2, 1], [2, 0]],  # L자_case8

    [[0, 0], [1, 0], [1, 1], [2, 1]],  # 번개모양_case1
    [[2, 0], [1, 0], [1, 1], [0, 1]],  # 번개모양_case2
    [[0, 0], [0, 1], [1, 1], [1, 2]],  # 번개모양_case3
    [[1, 0], [1, 1], [0, 1], [0, 2]],  # 번개모양_case4

    [[0, 0], [0, 1], [0, 2], [1, 1]],  # ㅗ자_case1
    [[1, 0], [1, 1], [1, 2], [0, 1]],  # ㅗ자_case1
    [[0, 0], [1, 0], [2, 0], [1, 1]],  # ㅗ자_case1
    [[1, 0], [0, 1], [1, 1], [2, 1]],  # ㅗ자_case1
]

for i in range(n):
    for j in range(m):
        bfs(i, j)

print(result)
