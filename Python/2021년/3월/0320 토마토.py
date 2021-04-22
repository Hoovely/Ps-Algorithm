# 백준7576_토마토_bfs_실버 1
# 시간초과 계속나서 구글링 해보니 in 함수의 시간복잡도가 O(n)이기 때문에 전체 시간복잡도가 O(n^3)이였다;;
# del 함수도 O(n)이라서 시간복잡도가 O(1)인 popleft 사용하니 해결

from sys import stdin # 시간초과 때문에 혹시 몰라 stdin.readline() 사용
from collections import deque

m,n = map(int, stdin.readline().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, stdin.readline().split())))
dn = [1,-1,0,0]
dm = [0,0,-1,1]
ik_to = deque()
flag = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1: # 처음 토마토가 심어진 좌표를 ik_to에 추가
            ik_to.append([i,j])

while ik_to:
    a,b = ik_to.popleft()
    for i in range(4):
        x = a + dn[i]
        y = b + dm[i]
        if 0<=x<n and 0<=y<m and tomato[x][y] == 0:
            tomato[x][y] = tomato[a][b] + 1
            ik_to.append([x,y])
            flag = 1
tomato_max = []

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0: # tomato에 아직 0 이 존재하면 flag -1
            flag = -1
    tomato_max.append(max(tomato[i]))
if flag == -1: # tomato에 0이 존재하여 -1 출력
    print(-1)
elif flag == 1: # tomato가 한번이라도 옮겨 심어졌기 때문에 최대값출력
    print(max(tomato_max)-1)
elif flag == 0: # tomato가 한번도 안 옮겨졌기 때문에 0 출력
    print(0)

