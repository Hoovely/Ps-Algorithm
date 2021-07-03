# 백준_10972_다음 순열_수학_실버 3

import sys
input = sys.stdin.readline


def solve():
    if len(lse) == n:
        print(*result)
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] == 1
            solve()
            lst.pop()


n = int(input())
lst = list(map(int, input().split()))

if lst == list(reversed([i for i in range(1, n+1)])):
    print(-1)
else:
    visited = [0]*n
    for i in lst:
        visited[i] = 1
    solve()
    # print(result)
