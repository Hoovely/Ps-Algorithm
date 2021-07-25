# 프로그래머스_다트 게임_스택_레벨 1

import math


def solution(dartResult):
    result = []
    num = ''
    for i in range(len(dartResult)):
        if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            if dartResult[i] == 'S':
                result.append(int(num))

            elif dartResult[i] == 'D':
                result.append(math.pow(int(num), 2))

            else:
                result.append(math.pow(int(num), 3))

            num = ''

        elif dartResult[i] == '*' or dartResult[i] == '#':
            if dartResult[i] == '*':
                if len(result) == 1:
                    result[0] *= 2
                else:
                    result[-1] *= 2
                    result[-2] *= 2
            else:
                result[-1] *= -1

        else:
            num += dartResult[i]

    return int(sum(result))


print(solution("1D2S#10S"))
