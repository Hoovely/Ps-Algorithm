# 백준3085_사탕 게임_브루트 포스_실버 4
# 오답 2

import sys
input = sys.stdin.readline


def swap(a, b):
    return b, a


def count_x():
    global result
    count = 1
    for i in range(n):
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                count += 1
            else:
                if result < count:
                    result = count
                count = 1
        if result < count:
            result = count
        count = 1


def count_y():
    global result
    count = 1
    for i in range(n):
        for j in range(n-1):
            if candy[j][i] == candy[j+1][i]:
                count += 1
            else:
                if result < count:
                    result = count
                count = 1
        if result < count:
            result = count
        count = 1


n = int(input())
candy = []
result = 0
for _ in range(n):
    candy.append(list(input().strip()))

for i in range(n):
    for j in range(n-1):
        candy[i][j], candy[i][j+1] = swap(candy[i][j], candy[i][j+1])
        count_x()
        count_y()
        candy[i][j], candy[i][j+1] = swap(candy[i][j], candy[i][j+1])

    for j in range(n-1):
        candy[j][i], candy[j+1][i] = swap(candy[j][i], candy[j+1][i])
        count_x()
        count_y()
        candy[j][i], candy[j+1][i] = swap(candy[j][i], candy[j+1][i])

print(result)
