# 백준_2740_행렬 곱셈_수학_브론즈 1

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

m, k = map(int, input().split())
B = []
for _ in range(m):
    B.append(list(map(int, input().split())))

C = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        num = 0
        for l in range(m):
            num += A[i][l]*B[l][j]
        C[i][j] = num

for i in range(n):
    print(*C[i])
