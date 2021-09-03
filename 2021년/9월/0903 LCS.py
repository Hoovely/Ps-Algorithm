# 백준_9251_LCS_DP_골드 5

a = input()
b = input()

a_len = len(a)
b_len = len(b)

lcs = [[0 for _ in range(b_len+1)]for _ in range(a_len+1)]

for i in range(1, a_len+1):
    for j in range(1, b_len+1):
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])
