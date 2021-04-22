# 백준1012_유기농 배추_bfs_실버 2

def bfs(a,b):
    baechu[a][b] = 0

    while move:
        a,b = move[0][0],move[0][1]
        del move[0]
        for i in range(4):
            x = a + dx[i] # 아래위로 이동
            y = b + dy[i] # 왼쪽, 오른쪽 이동
            if 0<=x<m and 0<=y<n and baechu[x][y] == 1: # n,m 범위안에서 상하좌우에 1 거리에 길이 존재할때 실행
                move.append([x,y]) # 이동한 좌표 move로 입력
                baechu[x][y] = 0 # 이동 완료한 배추밭 좌표 0으로 초기화

for _ in range(int(input())):
    m,n,k = map(int, input().split())

    baechu = [[0]*n for _ in range(m)] # n*m 넓이의 배추밭 0으로 초기화
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    move = [[0,0]]
    count = 0
    for _ in range(k):
        x,y = map(int, input().split())
        baechu[x][y] = 1 # 배추 심어진 x,y 좌표 1 입력
    
    for i in range(m):
        for j in range(n):
            if baechu[i][j] == 1:
                move = [[i,j]]
                count += 1 # 배추밭 한 덩어리 count
                bfs(i,j)
    print(count)
    

     