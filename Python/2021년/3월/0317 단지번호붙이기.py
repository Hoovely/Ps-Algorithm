# 백준2667_단지번호붙이기_bfs_실버 1

def bfs(a,b):
    bfs_count = 0
    while move:
        a,b = move[0][0], move[0][1] # 정사각형에서의 y좌표와 x좌표를 a,b에 넣어줌
        del move[0]
        for i in range(4):
            x = a + dx[i] # a 좌표에서 아래위로 이동
            y = b + dy[i] # b 좌표에서 왼쪽, 오른쪽으로 이동
            if 0 <= x < n and 0 <= y <n and sq[x][y] == 1 and visit[x][y] == 0: # 리스트 안에 들어있고, edge와 방문 하지 않았을때 true
                bfs_count += 1 
                move.append([x,y]) # 상하좌우중 1이 입력되어있는 좌표주소를 move에 추가
                visit[x][y] = 1 # 방문하였음
            else: # 반례
                if sq[a][b] == 1 and visit[a][b] == 0: # 상하좌우에 1이 없고, 자신만 1인 경우 
                    bfs_count += 1
                    visit[a][b] = 1
    return bfs_count


n = int(input()) # 정사각형의 크기 입력
sq = []
for _ in range(n):
    sq.append(list(map(int, str(input())))) # 2차원 리스트로 정사각형 구현
visit = [[0]*n for _ in range(n)] # 방문 여부 2차원 리스트 초기화 시켜줌
result = [] # 정답 리스트 생성
dx = [1,-1,0,0] # 정사각형에서 세로 이동
dy = [0,0,-1,1] # 정사각형에서 가로 이동
count = 0 # 몇 덩이 있는지 count
for i in range(n):
    for j in range(n):
        if sq[i][j] == 1 and visit[i][j] == 0: # 방문을 안했고, edge가 있을때 bfs진행
            move = [[i,j]] # 해당 좌표로 이동
            count += 1
            result.append(bfs(i,j))
            
print(count)
result = sorted(result) # 오름차순 배열 
for i in range(count):
    print(result[i])
