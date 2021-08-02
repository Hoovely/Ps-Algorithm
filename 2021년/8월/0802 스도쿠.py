# 백준_2580_스토쿠_백트래킹_골드 4

import sys
input = sys.stdin.readline


def check(x, y):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if maps[x][i] in nums:
            nums.remove(maps[x][i])
        if maps[i][y] in nums:
            nums.remove(maps[i][y])

    x //= 3
    y //= 3
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if maps[i][j] in nums:
                nums.remove(maps[i][j])

    return nums


def dfs(count):
    if count == len(zero_lst):
        for i in range(9):
            print(*maps[i])
        exit(0)

    x, y = zero_lst[count]
    nums = check(x, y)
    for num in nums:
        maps[x][y] = num
        dfs(count+1)
        maps[x][y] = 0


maps = []
for _ in range(9):
    maps.append(list(map(int, input().split())))

zero_lst = []
for i in range(9):
    for j in range(9):
        if maps[i][j] == 0:
            zero_lst.append([i, j])

dfs(0)
