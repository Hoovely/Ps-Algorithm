# 백준_10971_외판원 순회 2_백트래킹_실버 2

import sys
input = sys.stdin.readline


def dfs(first, last, sum, cnt):
    global min_num
    if cnt == n and first == last:
        if min_num > sum:
            min_num = sum
        return

    for i in range(n):
        if urban[last][i] == 0 or visited[last]:
            continue

        if urban[last][i] > 0 and visited[last] == 0:
            sum += urban[last][i]
            visited[last] = 1

            if min_num >= sum:
                dfs(first, i, sum, cnt+1)

            visited[last] = 0
            sum -= urban[last][i]


n = int(input())
urban = []
min_num = 10000001

visited = [0]*n
for _ in range(n):
    urban.append(list(map(int, input().split())))

for i in range(n):
    dfs(i, i, 0, 0)

print(min_num)
