# 백준7569_토마토 3차원_bfs_실버 1
# 처음에 2차원 리스트로 풀려했으나, 실패
# 3차원 리스트로 다시 푸니까 해결

from sys import stdin # 시간초과 때문에 혹시 몰라 stdin.readline() 사용
from collections import deque

m,n,h = map(int, stdin.readline().split()) 
tomato = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)] # 3차원 리스트 입력
ik_to = deque()
dn = [1,-1,0,0,0,0]
dm = [0,0,1,-1,0,0]
dh = [0,0,0,0,1,-1] 
flag = -1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1: # 처음 토마토가 심어진 좌표를 ik_to에 추가
                ik_to.append([i,j,k]) 
while ik_to:
    c,a,b = ik_to.popleft()
    for i in range(6): # 3차원이므로 6번 움직임
        x = a + dn[i] # 세로
        y = b + dm[i] # 가로
        z = c + dh[i] # 높이
        if 0<=z<h and 0<=x<n and 0<=y<m and tomato[z][x][y] == 0:
            tomato[z][x][y] = tomato[c][a][b] + 1
            ik_to.append([z,x,y])
            flag = 1
tomato_max = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0: # 아직 토마토 밭에 0이 남아있다면 flag 0
                flag = 0
        tomato_max.append(max(tomato[i][j])) # 토마토 밭 한줄의 최대값 tomato_max에 추가

if flag == 1: # tomato가 한번이라도 옮겨 졌을때 max값 출력 
    print(max(tomato_max)-1)
elif flag == -1: # tomato가 한번도 안 옮겨 졌을때 0출력
    print(0)
elif flag == 0: # tomato에 아직 0이 존재할때 -1 출력
    print(-1)