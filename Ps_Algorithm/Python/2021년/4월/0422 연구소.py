# 백준14502_연구소_bfs, 백트래킹_골드 5
# 백트래킹으로 모든 0 자리에 1을 3개 넣어보고, 이에 따라 bfs로 0의 갯수 구함
# 입력받은 2차원 graph를 1차원 list형태로 고치고 모든 0 자리에 1을 3개 넣는다.
# 1을 입력받은 1차원 list를 bfs함수로 이동시켜 2차원 list형태로 변환하고 bfs 사용하여 바이러스가 퍼지는 것을 구현한다.
# 남은 0의 갯수를 count하고 다음 1차원 list의 경우의 수를 실행시킨다.
# Python3 : 메모리 29080kb, 시간 3340ms
# PyPy3 : 메모리 127248kb, 시간 472ms

import sys

def bfs():
    count = 0

    bfs_maps = []
    for i in range(n):
        bfs_maps.append(new_maps[m*i:m*(i+1)]) # 1차원 list를 2차원 list로 변환
    for i in range(n):
        for j in range(m):
            if bfs_maps[i][j] == 2:
                move.append([i,j]) # 2가 있는 좌표를 추가
    
    while move: # bfs 진행
        a = move[0][0]
        b = move[0][1]
        del move[0]
        for i in range(4):
            x = a + dn[i]
            y = b + dm[i]
            if 0<=x<n and 0<=y<m and bfs_maps[x][y] == 0:
                bfs_maps[x][y] = 2
                move.append([x,y])

    for i in range(n): # 0의 갯수를 count
        for j in range(m):
            if bfs_maps[i][j] == 0:
                count += 1   

    return count


n,m = map(int,sys.stdin.readline().split())

maps = []
result = []
move = []

dn = [1,-1,0,0]
dm = [0,0,1,-1]

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

new_maps = sum(maps, []) # 입력받은 2차원 list를 1차원 list로 변환
for i in range(n*m):
    if new_maps[i] == 0: # i 자리에 0이 있을때 1 집어 넣고 없으면 다음 좌표 실행
        new_maps[i] = 1
    else:
        continue
    for j in range(i+1, n*m):
        if new_maps[j] == 0: # i+1 자리에 0이 있을때 1 집어 넣고 없으면 다음 좌표 실행
            new_maps[j] = 1
        else:
            continue
        for k in range(j+1, n*m): 
            if new_maps[k] == 0: # i+2 자리에 0이 있을때 1 집어 넣고 없으면 다음 좌표 실행
                new_maps[k] = 1
                result.append(bfs()) # 1을 3개 넣었으므로, bfs 함수 진행
                new_maps[k] = 0 # 0 으로 초기화하여 다음 경우의 수 진행
            else:
                continue
        new_maps[j] = 0 # 0 으로 초기화하여 다음 경우의 수 진행
    new_maps[i] = 0 # 0 으로 초기화하여 다음 경우의 수 진행

print(max(result))

