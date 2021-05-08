places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                         "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def solution(places):
    dx = [1, -1, 1, -1, 2, -2, 0, 0, 0, 0]
    dy = [1, -1, 0, 0, 0, 0, 1, -1, 2, -2]
    answer = [1, 1, 1, 1, 1]
    place1 = []
    place2 = []
    place3 = []
    place4 = []
    place5 = []
    for i in range(5):
        place1.append(list(places[0][i]))
    for i in range(5):
        place2.append(list(places[1][i]))
    for i in range(5):
        place3.append(list(places[2][i]))
    for i in range(5):
        place4.append(list(places[3][i]))
    for i in range(5):
        place5.append(list(places[4][i]))

    for j in range(5):
        for k in range(5):
            if place1[j][k] == 'P':
                for i in range(10):
                    x = j + dx[i]
                    y = k + dy[i]
                    if 0 <= x < 5 and 0 <= y < 5 and place1[x][y] == 'P':
                        if x == j:  # 직선상에 있는 경우1
                            if abs(dy[i]) == 1:
                                answer[0] = 0
                                break
                            else:
                                if place1[j][(y+k)//2] == 'X':
                                    if 0 < j < 4:
                                        if (place1[j+1][(y+k)//2] == 'X' and place1[j-1][(y+k)//2] == 'X') or (place1[j+1][y] == 'X' and place1[j-1][y] == 'X') or (place1[j+1][k] == 'X' and place1[j-1][k] == 'X'):
                                            pass
                                    else:
                                        if j == 0:
                                            if place1[j+1][(y+k)//2] == 'X' or place1[j+1][y] == 'X' or place1[j+1][k] == 'X':
                                                pass
                                        else:
                                            if place1[j-1][(y+k)//2] == 'X' or place1[j-1][y] == 'X' or place1[j-1][k] == 'X':
                                                pass
                                else:
                                    answer[0] = 0
                                    break
                        elif y == k:  # 직선상에 있는 경우2
                            if abs(dx[i]) == 1:
                                answer[0] = 0
                                break
                            else:
                                if place1[(x+j)//2][k] == 'X':
                                    if 0 < k < 4:
                                        if ((place1[(x+j)//2][k+1] == 'X' and place1[(x+j)//2][k-1] == 'X') or (place1[x][k+1] == 'X' and place1[x][k-1] == 'X') or (place1[j][k+1] == 'X' and place1[j][k-1] == 'X')):
                                            pass
                                    else:
                                        if k == 0:
                                            if place1[(x+j)//2][k+1] == 'X' or place1[x][k+1] == 'X' or place1[j][k+1] == 'X':
                                                pass
                                        else:
                                            if place1[(x+j)//2][k-1] == 'X' or place1[x][k-1] == 'X' or place1[j][k-1] == 'X':
                                                pass
                                else:
                                    answer[0] = 0
                                    break
                        elif x != j and y != k:  # 대각선상에 있는 경우
                            if place1[j+dx[i]][k] == 'X' and place1[j][k+dy[i]] == 'X':
                                pass
                            else:
                                answer[0] = 0
                                break
                place1[j][k] = 'O'
            if answer[0] == 0:
                break
        if answer[0] == 0:
            break

    for j in range(5):
        for k in range(5):
            if place2[j][k] == 'P':
                for i in range(10):
                    x = j + dx[i]
                    y = k + dy[i]
                    if 0 <= x < 5 and 0 <= y < 5 and place2[x][y] == 'P':
                        if x == j:  # 직선상에 있는 경우1
                            if abs(dy[i]) == 1:
                                answer[1] = 0
                                break
                            else:
                                if place2[j][(y+k)//2] == 'X':
                                    if 0 < j < 4:
                                        if (place2[j+1][(y+k)//2] == 'X' and place2[j-1][(y+k)//2] == 'X') or (place2[j+1][y] == 'X' and place2[j-1][y] == 'X') or (place2[j+1][k] == 'X' and place2[j-1][k] == 'X'):
                                            pass
                                    else:
                                        if j == 0:
                                            if place2[j+1][(y+k)//2] == 'X' or place2[j+1][y] == 'X' or place2[j+1][k] == 'X':
                                                pass
                                        else:
                                            if place2[j-1][(y+k)//2] == 'X' or place2[j-1][y] == 'X' or place2[j-1][k] == 'X':
                                                pass
                                else:
                                    answer[1] = 0
                                    break
                        elif y == k:  # 직선상에 있는 경우2
                            if abs(dx[i]) == 1:
                                answer[1] = 0
                                break
                            else:
                                if place2[(x+j)//2][k] == 'X':
                                    if 0 < k < 4:
                                        if (place2[(x+j)//2][k+1] == 'X' and place2[(x+j)//2][k-1] == 'X') or (place2[x][k+1] == 'X' and place2[x][k-1] == 'X') or (place2[j][k+1] == 'X' and place2[j][k-1] == 'X'):
                                            pass
                                    else:
                                        if k == 0:
                                            if place2[(x+j)//2][k+1] == 'X' or place2[x][k+1] == 'X' or place2[j][k+1] == 'X':
                                                pass
                                        else:
                                            if place2[(x+j)//2][k-1] == 'X' or place2[x][k-1] == 'X' or place2[j][k-1] == 'X':
                                                pass
                                else:
                                    answer[1] = 0
                                    break
                        elif x != j and y != k:  # 대각선상에 있는 경우
                            if place2[j+dx[i]][k] != 'X' and place2[j][k+dy[i]] != 'X':
                                answer[1] = 0
                                break
                place2[j][k] = 'O'
            if answer[1] == 0:
                break
        if answer[1] == 0:
            break

    for j in range(5):
        for k in range(5):
            if place3[j][k] == 'P':
                for i in range(10):
                    x = j + dx[i]
                    y = k + dy[i]
                    if 0 <= x < 5 and 0 <= y < 5 and place3[x][y] == 'P':
                        if x == j:  # 직선상에 있는 경우1
                            if abs(dy[i]) == 1:
                                answer[2] = 0
                                break
                            else:
                                if place3[j][(y+k)//2] == 'X':
                                    if 0 < j < 4:
                                        if (place3[j+1][(y+k)//2] == 'X' and place3[j-1][(y+k)//2] == 'X') or (place3[j+1][y] == 'X' and place3[j-1][y] == 'X') or (place3[j+1][k] == 'X' and place3[j-1][k] == 'X'):
                                            pass
                                    else:
                                        if j == 0:
                                            if place3[j+1][(y+k)//2] == 'X' or place3[j+1][y] == 'X' or place3[j+1][k] == 'X':
                                                pass
                                        else:
                                            if place3[j-1][(y+k)//2] == 'X' or place3[j-1][y] == 'X' or place3[j-1][k] == 'X':
                                                pass
                                else:
                                    answer[2] = 0
                                    break
                        elif y == k:  # 직선상에 있는 경우2
                            if abs(dx[i]) == 1:
                                answer[2] = 0
                                break
                            else:
                                if place3[(x+j)//2][k] == 'X':
                                    if 0 < k < 4:
                                        if (place3[(x+j)//2][k+1] == 'X' and place3[(x+j)//2][k-1] == 'X') or (place3[x][k+1] == 'X' and place3[x][k-1] == 'X') or (place3[j][k+1] == 'X' and place3[j][k-1] == 'X'):
                                            pass
                                    else:
                                        if k == 0:
                                            if place3[(x+j)//2][k+1] == 'X' or place3[x][k+1] == 'X' or place3[j][k+1] == 'X':
                                                pass
                                        else:
                                            if place3[(x+j)//2][k-1] == 'X' or place3[x][k-1] == 'X' or place3[j][k-1] == 'X':
                                                pass
                                else:
                                    answer[2] = 0
                                    break
                        elif x != j and y != k:  # 대각선상에 있는 경우
                            if place3[j+dx[i]][k] != 'X' and place3[j][k+dy[i]] != 'X':
                                answer[2] = 0
                                break
                place3[j][k] = 'O'
            if answer[2] == 0:
                break
        if answer[2] == 0:
            break

    for j in range(5):
        for k in range(5):
            if place4[j][k] == 'P':
                for i in range(10):
                    x = j + dx[i]
                    y = k + dy[i]
                    if 0 <= x < 5 and 0 <= y < 5 and place4[x][y] == 'P':
                        if x == j:  # 직선상에 있는 경우1
                            if abs(dy[i]) == 1:
                                answer[3] = 0
                                break
                            else:
                                if place4[j][(y+k)//2] == 'X':
                                    if 0 < j < 4:
                                        if (place4[j+1][(y+k)//2] == 'X' and place4[j-1][(y+k)//2] == 'X') or (place4[j+1][y] == 'X' and place4[j-1][y] == 'X') or (place4[j+1][k] == 'X' and place4[j-1][k] == 'X'):
                                            pass
                                    else:
                                        if j == 0:
                                            if place4[j+1][(y+k)//2] == 'X' or place4[j+1][y] == 'X' or place4[j+1][k] == 'X':
                                                pass
                                        else:
                                            if place4[j-1][(y+k)//2] == 'X' or place4[j-1][y] == 'X' or place4[j-1][k] == 'X':
                                                pass
                                else:
                                    answer[3] = 0
                                    break
                        elif y == k:  # 직선상에 있는 경우2
                            if abs(dx[i]) == 1:
                                answer[3] = 0
                                break
                            else:
                                if place4[(x+j)//2][k] == 'X':
                                    if 0 < k < 4:
                                        if (place4[(x+j)//2][k+1] == 'X' and place4[(x+j)//2][k-1] == 'X') or (place4[x][k+1] == 'X' and place4[x][k-1] == 'X') or (place4[j][k+1] == 'X' and place4[j][k-1] == 'X'):
                                            pass
                                    else:
                                        if k == 0:
                                            if place4[(x+j)//2][k+1] == 'X' or place4[x][k+1] == 'X' or place4[j][k+1] == 'X':
                                                pass
                                        else:
                                            if place4[(x+j)//2][k-1] == 'X' or place4[x][k-1] == 'X' or place4[j][k-1] == 'X':
                                                pass
                                else:
                                    answer[3] = 0
                                    break
                        elif x != j and y != k:  # 대각선상에 있는 경우
                            if place4[j+dx[i]][k] != 'X' and place4[j][k+dy[i]] != 'X':
                                answer[3] = 0
                                break
                place4[j][k] = 'O'
            if answer[3] == 0:
                break
        if answer[3] == 0:
            break

    for j in range(5):
        for k in range(5):
            if place5[j][k] == 'P':
                for i in range(10):
                    x = j + dx[i]
                    y = k + dy[i]
                    if 0 <= x < 5 and 0 <= y < 5 and place5[x][y] == 'P':
                        if x == j:  # 직선상에 있는 경우1
                            if abs(dy[i]) == 1:
                                answer[4] = 0
                                break
                            else:
                                if place5[j][(y+k)//2] == 'X':
                                    if 0 < j < 4:
                                        if (place5[j+1][(y+k)//2] == 'X' and place5[j-1][(y+k)//2] == 'X') or (place5[j+1][y] == 'X' and place5[j-1][y] == 'X') or (place5[j+1][k] == 'X' and place5[j-1][k] == 'X'):
                                            pass
                                    else:
                                        if j == 0:
                                            if place5[j+1][(y+k)//2] == 'X' or place5[j+1][y] == 'X' or place5[j+1][k] == 'X':
                                                pass
                                        else:
                                            if place5[j-1][(y+k)//2] == 'X' or place5[j-1][y] == 'X' or place5[j-1][k] == 'X':
                                                pass
                                else:
                                    answer[4] = 0
                                    break
                        elif y == k:  # 직선상에 있는 경우2
                            if abs(dx[i]) == 1:
                                answer[4] = 0
                                break
                            else:
                                if place5[(x+j)//2][k] == 'X':
                                    if 0 < k < 4:
                                        if (place5[(x+j)//2][k+1] == 'X' and place5[(x+j)//2][k-1] == 'X') or (place5[x][k+1] == 'X' and place5[x][k-1] == 'X') or (place5[j][k+1] == 'X' and place5[j][k-1] == 'X'):
                                            pass
                                    else:
                                        if k == 0:
                                            if place5[(x+j)//2][k+1] == 'X' or place5[x][k+1] == 'X' or place5[j][k+1] == 'X':
                                                pass
                                        else:
                                            if place5[(x+j)//2][k-1] == 'X' or place5[x][k-1] == 'X' or place5[j][k-1] == 'X':
                                                pass
                                else:
                                    answer[4] = 0
                                    break
                        elif x != j and y != k:  # 대각선상에 있는 경우
                            if place5[j+dx[i]][k] != 'X' and place5[j][k+dy[i]] != 'X':
                                answer[4] = 0
                                break
                place5[j][k] = 'O'
            if answer[4] == 0:
                break
        if answer[4] == 0:
            break

    return answer


print(solution(places))
