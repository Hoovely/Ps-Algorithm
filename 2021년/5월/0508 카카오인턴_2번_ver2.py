places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                         "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def bfs(i, j, k, new_places, answer):
    dx = [1, -1, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0]
    dy = [0, 0, 1, -1, 1, -1, 1, -1, 0, 0, 2, -2]
    for l in range(4):
        x = j + dx[l]
        y = k + dy[l]
        if 0 <= x <= 4 and 0 <= y <= 4 and new_places[i][x][y] == 'P':
            answer[i] = 0
            return
    for l in range(4, 12):
        x = j + dx[l]
        y = k + dy[l]
        if 0 <= x <= 4 and 0 <= y <= 4 and new_places[i][x][y] == 'P':
            if x == j:
                if 0 < j < 4:
                    if (new_places[i][j-1][(y+k)//2] == 'X' and new_places[i][j][(y+k)//2] == 'X' and new_places[i][j+1][(y+k)//2] == 'X') or (new_places[i][j][(y+k)//2] == 'X' and new_places[i][j-1][k] == 'X' and new_places[i][j+1][k] == 'X') or (new_places[i][j][(y+k)//2] == 'X' and new_places[i][j-1][y] == 'X' and new_places[i][j+1][y] == 'X'):
                        pass
                    else:
                        answer[i] = 0
                        return
                elif j == 0:
                    if (new_places[i][j][(y+k)//2] == 'X' and new_places[i][j+1][(y+k)//2] == 'X') or (new_places[i][j][(y+k)//2] == 'X' and new_places[i][j+1][k] == 'X') or (new_places[i][j][(y+k)//2] == 'X' and new_places[i][j+1][y] == 'X'):
                        pass
                    else:
                        answer[i] = 0
                        return
                elif j == 4:
                    if (new_places[i][j-1][(y+k)//2] == 'X' and new_places[i][j][(y+k)//2] == 'X') or (new_places[i][j][(y+k)//2] == 'X' and new_places[i][j-1][k] == 'X') or (new_places[i][j][(y+k)//2] == 'X' and new_places[i][j-1][y] == 'X'):
                        pass
                    else:
                        answer[i] = 0
                        return
            elif y == k:
                if 0 < k < 4:
                    if (new_places[i][(x+j)//2][k-1] == 'X' and new_places[i][(x+j)//2][k] == 'X' and new_places[i][(x+j)//2][k+1] == 'X') or (new_places[i][(x+j)//2][k] == 'X' and new_places[i][j][k-1] == 'X' and new_places[i][j][k+1] == 'X') or (new_places[i][(x+j)//2][k] == 'X' and new_places[i][x][k-1] == 'X' and new_places[i][x][k+1] == 'X'):
                        pass
                    else:
                        answer[i] = 0
                        return
                elif k == 0:
                    if (new_places[i][(x+j)//2][k] == 'X' and new_places[i][(x+j)//2][k+1] == 'X') or (new_places[i][(x+j)//2][k] == 'X' and new_places[i][j][k+1] == 'X') or (new_places[i][(x+j)//2][k] == 'X' and new_places[i][x][k+1] == 'X'):
                        pass
                    else:
                        answer[i] = 0
                        return
                elif k == 4:
                    if (new_places[i][(x+j)//2][k-1] == 'X' and new_places[i][(x+j)//2][k] == 'X') or (new_places[i][(x+j)//2][k] == 'X' and new_places[i][j][k-1] == 'X') or (new_places[i][(x+j)//2][k] == 'X' and new_places[i][x][k-1] == 'X'):
                        pass
                    else:
                        answer[i] = 0
                        return
            elif x != j and y != k:
                if new_places[i][x][k] == 'X' and new_places[j][j][y] == 'X':
                    pass
                else:
                    answer[i] = 0
                    return


def solution(places):
    new_places = [[[k for k in j] for j in i] for i in places]
    answer = [1, 1, 1, 1, 1]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if new_places[i][j][k] == 'P' and answer[i] == 1:
                    bfs(i, j, k, new_places, answer)
                    new_places[i][j][k] = 'O'
    return answer


print(solution(places))
