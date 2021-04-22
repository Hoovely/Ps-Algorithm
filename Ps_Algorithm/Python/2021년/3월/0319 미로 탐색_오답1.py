# 백준2178_미로 탐색_bfs_실버 1

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, str(input()))))

dn = [1,-1,0,0]
dm = [0,0,1,-1]
move = [[0,0]]

while move:
    a, b = move[0][0], move[0][1]
    del move[0]
    for i in range(4):
        x = a + dn[i]
        y = b + dm[i]
        if 0 <= x < n and 0 <= y < m and maze[x][y] == 1:
            move.append([x, y])
            maze[x][y] = maze[a][b] + 1

print(maze[-1][-1])