# 백준_9252_LCS 2_DP_골드 5

a = input()
b = input()

a_len = len(a)
b_len = len(b)

LCS = [[0 for _ in range(b_len+1)] for _ in range(a_len+1)]

for i in range(1, a_len+1):
    for j in range(1, b_len+1):
        if a[i-1] == b[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
result = LCS[-1][-1]

x = a_len
y = b_len
LCS_sub = ''
while len(LCS_sub) != result:
    if LCS[x][y] != LCS[x-1][y] and LCS[x][y] != LCS[x][y-1]:
        LCS_sub += str(a[x-1])
        x -= 1
        y -= 1
    elif LCS[x][y] == LCS[x-1][y]:
        x -= 1
    elif LCS[x][y] == LCS[x][y-1]:
        y -= 1

print(result)
print(LCS_sub[::-1])
