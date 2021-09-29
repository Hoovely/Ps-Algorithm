# 알고스팟_소풍_브루트포스_하
# 오답 1

import sys
input = sys.stdin.readline


def dfs():
    global result
    flag = True
    for i in range(n):
        if check[i] == False:
            flag = False
            start_idx = i
            break
    if flag:
        result += 1
        return

    for i in range(start_idx+1, n):
        if check[i] == False and isFriends[start_idx][i]:
            check[i] = check[start_idx] = True
            dfs()
            check[i] = check[start_idx] = False


for _ in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    check = [False]*n
    isFriends = [[False]*n for _ in range(n)]
    for i in range(0, m*2, 2):
        isFriends[lst[i]][lst[i+1]] = True
        isFriends[lst[i+1]][lst[i]] = True

    result = 0
    dfs()
    print(result)
