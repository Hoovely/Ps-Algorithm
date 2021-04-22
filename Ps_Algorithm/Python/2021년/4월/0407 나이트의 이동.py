# 백준7562_나이트의 이동_bfs_실버 2
# 처음에는 이동한 좌표를 다시 이동할수 있게 코드를 구현했으나 무한 while을 탈출 못해서
# chess[x][y] == 0 조건을 걸어주니까, 시간에 맞게 답이 나옴

import sys

for _ in range(int(sys.stdin.readline())):
    l = int(sys.stdin.readline())
    x, y = map(int,sys.stdin.readline().split())
    move_x, move_y = map(int,sys.stdin.readline().split())
    
    chess = [[0]*l for _ in range(l)]
    move = [[x,y]]
    dx = [1,2,-1,-2,1,2,-1,-2]
    dy = [2,1,-2,-1,-2,-1,2,1]

    while 1:
        a = move[0][0]
        b = move[0][1]
        del move[0]

        if a == move_x and b == move_y:
            break

        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<l and 0<=y<l and chess[x][y] == 0:
                chess[x][y] = chess[a][b] + 1
                move.append([x,y])

    print(chess[a][b])