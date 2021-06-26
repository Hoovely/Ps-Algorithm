# 백준3085_사탕 게임_브루트 포스_실버 4
# 오답 1

import sys
input = sys.stdin.readline


def swap(a, b):
    return b, a


def count_w():
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


def count_h():
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
        count_w()
        count_h()
        candy[i][j], candy[i][j+1] = swap(candy[i][j], candy[i][j+1])

for i in range(n):
    for j in range(n-1):
        candy[j][i], candy[j+1][i] = swap(candy[j][i], candy[j+1][i])
        count_w()
        count_h()
        candy[j][i], candy[j+1][i] = swap(candy[j][i], candy[j+1][i])
print(result)
