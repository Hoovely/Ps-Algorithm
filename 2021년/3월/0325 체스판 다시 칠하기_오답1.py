# 백준1018_체스판 다시 칠하기_브루트포스 알고리즘_실버 5

def test(x,y):
    x_count = 0
    y_count = 0
    if x+8 <= n and y+8 <= m:
        for i in range(x, x+8):
            for j in range(y, y+8):
                if start_black[i-x][j-y] != chess[i][j]:
                    x_count += 1
                if start_white[i-x][j-y] != chess[i][j]:
                    y_count += 1
        return min(x_count,y_count)
    return -1


result_min = 9999999999999
start_black = []
start_white = []
for i in range(8):
    if i % 2 == 0:
        start_black.append(['B','W','B','W','B','W','B','W'])
        start_white.append(['W','B','W','B','W','B','W','B'])
    else:
        start_black.append(['W','B','W','B','W','B','W','B'])
        start_white.append(['B','W','B','W','B','W','B','W'])

n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        result = test(i,j)
        if result != -1:
            result_min = min(result, result_min)
print(result_min)