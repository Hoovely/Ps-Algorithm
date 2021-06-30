# 프로그래머스_정수 제곱근 판별_수학_레벨 1

import math


def solution(n):
    num = math.sqrt(n)
    if num == int(num):
        return (num+1)**2
    else:
        return -1


print(solution(3))
