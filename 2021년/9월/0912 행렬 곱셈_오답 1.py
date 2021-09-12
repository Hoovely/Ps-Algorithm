# 백준_2740_행렬 곱셈_수학_브론즈 1
# 오답 1

n, m = map(int, input().split())
arr1 = []
for _ in range(n):
    arr1.append(list(map(int, input().split())))

m, k = map(int, input().split())
arr2 = []
for _ in range(m):
    arr2.append(list(map(int, input().split())))

arr3 = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            arr3[i][j] += arr1[i][l]*arr2[l][j]

for i in range(n):
    print(*arr3[i])
