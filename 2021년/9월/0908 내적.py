# 프로그래머스_수학_내적_레벨 1

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
