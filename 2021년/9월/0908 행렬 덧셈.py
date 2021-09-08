# 백준_2738_행렬 덧셈_수학_브론즈 1

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = []
arr2 = []

for i in range(n*2):
    if i < n:
        arr1.append(list(map(int, input().split())))
    else:
        arr2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        arr1[i][j] += arr2[i][j]

for i in range(n):
    print(*arr1[i])
