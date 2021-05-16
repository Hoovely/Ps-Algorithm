# 코드업6098_성실한 개미_python 기초 100제

def move(x,y):
    if graph[x][y] == 2:
        graph[x][y] = 9
        return
    graph[x][y] = 9

    if graph[x][y+1] != 1:
        move(x,y+1)
    elif graph[x][y+1] == 1 and graph[x+1][y] != 1:
        move(x+1,y)
    
graph = []
for i in range(10):
    graph.append(list(map(int, input().split())))
    
move(1,1)

for i in graph:
    for j in i:
        print(j, end=' ')
    print()
