# 백준_1958_LCS 3_DP_골드 3

a = input()
b = input()
c = input()

LCS = [[[0 for _ in range(len(c)+1)] for _ in range(len(b)+1)]
       for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        for k in range(1, len(c)+1):
            if a[i-1] == b[j-1] == c[k-1]:
                LCS[i][j][k] = LCS[i-1][j-1][k-1] + 1
            else:
                LCS[i][j][k] = max(LCS[i-1][j][k], LCS[i]
                                   [j-1][k], LCS[i][j][k-1])

print(LCS[-1][-1][-1])
