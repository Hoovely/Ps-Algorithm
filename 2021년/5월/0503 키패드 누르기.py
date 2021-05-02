# 프로그래머스_키패드 누르기_구현_레벨 1
# 빨리 풀려고 더럽게 푼 풀이 방법

def solution(numbers, hand):
    answer = ""
    L_move = [[3,0]]
    R_move = [[3,2]]
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7,'*']:
            answer += 'L'
            if numbers[i] == 1:
                L_move.append([0,0])
            elif numbers[i] == 4:
                L_move.append([1,0])
            elif numbers[i] == 7:
                L_move.append([2,0])
            else:
                L_move.append([3,0])

        elif numbers[i] in [3,6,9,'#']:
            answer += 'R'
            if numbers[i] == 3:
                R_move.append([0,2])
            elif numbers[i] == 6:
                R_move.append([1,2])
            elif numbers[i] == 9:
                R_move.append([2,2])
            else:
                R_move.append([3,2])

        else:
            L_xy = L_move[-1]
            R_xy = R_move[-1]
            L_x, L_y = L_xy[0], L_xy[1]
            R_x, R_y = R_xy[0], R_xy[1]
            if numbers[i] == 2:
                if abs(L_x-0) + abs(L_y-1) == abs(R_x-0) + abs(R_y-1):
                    if hand == "right":
                        answer += 'R'
                        R_move.append([0,1])
                    else:
                        answer += 'L'
                        L_move.append([0,1])

                elif abs(L_x-0) + abs(L_y-1) > abs(R_x-0) + abs(R_y-1):
                    answer += 'R'
                    R_move.append([0,1])
                else:
                    answer += 'L'
                    L_move.append([0,1])
                
            elif numbers[i] == 5:
                if abs(L_x-1) + abs(L_y-1) == abs(R_x-1) + abs(R_y-1):
                    if hand == "right":
                        answer += 'R'
                        R_move.append([1,1])
                    else:
                        answer += 'L'
                        L_move.append([1,1])
                        
                elif abs(L_x-1) + abs(L_y-1) > abs(R_x-1) + abs(R_y-1):
                    answer += 'R'
                    R_move.append([1,1])
                else:
                    answer += 'L'
                    L_move.append([1,1])
                
            elif numbers[i] == 8:
                if abs(L_x-2) + abs(L_y-1) == abs(R_x-2) + abs(R_y-1):
                    if hand == "right":
                        answer += 'R'
                        R_move.append([2,1])
                    else:
                        answer += 'L'
                        L_move.append([2,1])
                        
                elif abs(L_x-2) + abs(L_y-1) > abs(R_x-2) + abs(R_y-1):
                    answer += 'R'
                    R_move.append([2,1])
                else:
                    answer += 'L'
                    L_move.append([2,1])
            else:
                if abs(L_x-3) + abs(L_y-1) == abs(R_x-3) + abs(R_y-1):
                    if hand == "right":
                        answer += 'R'
                        R_move.append([3,1])
                    else:
                        answer += 'L'
                        L_move.append([3,1])
                        
                elif abs(L_x-3) + abs(L_y-1) > abs(R_x-3) + abs(R_y-1):
                    answer += 'R'
                    R_move.append([3,1])
                else:
                    answer += 'L'
                    L_move.append([3,1])

    return answer

numbers = list(map(int, input().split()))
hand = input()
print(solution(numbers, hand))


