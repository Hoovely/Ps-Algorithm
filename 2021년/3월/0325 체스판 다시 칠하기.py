# 백준1018_체스판 다시 칠하기_브루트포스 알고리즘_실버 5
# 하루종일 고민하다가 8x8로 체스판을 구현하는 것을 못 하겠어서 구글링..
# [0][0] 좌표의 색이 검은색, 흰색 일때의 체스판을 2개 구현 해 놓은다음
# 입력된 체스판의 값과 비교하여 틀린 좌표당 카운트해서 가장 작은 경우에수의 카운트 값을 출력한다.

start_black = []
start_white = []
result_min = 9999999999999 # 최솟값을 비교하기 위해서 큰 값으로 초기화
for i in range(8): # 올바르게 입력된 체스판 2개를 구현
    if i % 2 == 0:
        start_black.append(['B','W','B','W','B','W','B','W'])
        start_white.append(['W','B','W','B','W','B','W','B'])
    else:
        start_black.append(['W','B','W','B','W','B','W','B'])
        start_white.append(['B','W','B','W','B','W','B','W'])

def test(x,y): # 비교할 함수를 구현
    num_x = 0
    num_y = 0
    if x+8<=n and y+8<=m: # 체스판 범위에서 벗어나는지 확인
        for i in range(8):
            for j in range(8):
                if chess[x+i][y+j] != start_black[i][j]: # 체스판과 비교해서 안맞는 좌표의 갯수를 count
                    num_x += 1
                if chess[x+i][y+j] != start_white[i][j]:
                    num_y += 1
        return min(num_x, num_y) # 두개의 count 갯수중 작은것을 반환
    return -1

n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(input())) # 체스판을 2차원list로 구현
for i in range(n):
    for j in range(m):
        result = test(i,j)
        if result != -1: # 함수의 반환값이 -1이 아니고, 지금까지의 최솟값보다 작을때
            if result < result_min:
                result_min = result
print(result_min)



