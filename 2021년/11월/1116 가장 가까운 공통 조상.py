# 백준_3584_가장 가까운 공통 조상_트리_골드 4
# 시간초과 예상한 풀이방법, 더럽게 풀었으나 통과했다

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(m):
    global lst
    if len(tree[m]):
        for k in tree[m]:
            lst.append(k)
            dfs(k)


for _ in range(int(input())):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[b].append(a)
    x, y = map(int, input().split())

    lst = []
    lst.append(x)
    dfs(x)
    x_lst = lst

    lst = []
    lst.append(y)
    dfs(y)
    y_lst = lst

    flag = 0
    if len(x_lst) >= len(y_lst):
        for i in x_lst:
            if flag:
                break
            for j in y_lst:
                if flag:
                    break
                if i == j:
                    print(i)
                    flag = 1
    else:
        for i in y_lst:
            if flag:
                break
            for j in x_lst:
                if flag:
                    break
                if i == j:
                    print(i)
                    flag = 1
