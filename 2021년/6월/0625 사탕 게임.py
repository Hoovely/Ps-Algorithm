# 백준3085_사탕 게임_브루트 포스_실버 4

import sys
input = sys.stdin.readline


def temp(a, b):
    return b, a


def candy_count_x():
    global result
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candy[j+1][i] == candy[j][i]:
                cnt += 1
            else:
                if cnt > result:
                    result = cnt
                cnt = 1
        if cnt > result:
            result = cnt


def candy_count_y():
    global result
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candy[i][j+1] == candy[i][j]:
                cnt += 1
            else:
                if cnt > result:
                    result = cnt
                cnt = 1
        if cnt > result:
            result = cnt


n = int(input())
candy = []
result = 0

for _ in range(n):
    candy.append(list(input().strip()))

for i in range(n):
    for j in range(n-1):
        candy[i][j], candy[i][j+1] = temp(candy[i][j], candy[i][j+1])
        candy_count_x()
        candy_count_y()
        candy[i][j], candy[i][j+1] = temp(candy[i][j], candy[i][j+1])

for i in range(n):
    for j in range(n-1):
        candy[j][i], candy[j+1][i] = temp(candy[j][i], candy[j+1][i])
        candy_count_x()
        candy_count_y()
        candy[j][i], candy[j+1][i] = temp(candy[j][i], candy[j+1][i])

print(result)
