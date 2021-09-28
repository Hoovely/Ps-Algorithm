# 알고스팟_소풍_브루트포스_하

import sys
input = sys.stdin.readline


def dfs():
    global result
    flag = True
    for i in range(n):
        if couple[i] == False:
            start_idx = i
            flag = False
            break
    if flag:
        result += 1
        return

    for i in range(start_idx+1, n):
        if couple[i] == False and isFriend[start_idx][i]:
            couple[i] = couple[start_idx] = True
            dfs()
            couple[i] = couple[start_idx] = False


for _ in range(int(input())):
    n, m = map(int, input().split())
    couple = [False for _ in range(n)]
    isFriend = [[False]*n for _ in range(n)]
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        isFriend[lst[i]][lst[i+1]] = True
        isFriend[lst[i+1]][lst[i]] = True

    result = 0
    dfs()
    print(result)
