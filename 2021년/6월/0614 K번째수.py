# 프로그래머스_K번째수_정렬_레벨 1

def solution(array, commands):
    answer = []
    for command in commands:
        new_array = array[command[0]-1:command[1]]
        new_array.sort()
        answer.append(new_array[command[2]-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
