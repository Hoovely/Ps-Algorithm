# 프로그래머스_자릿수 더하기_수학_레벨 1

def solution(n):
    sum = 0
    for num in str(n):
        sum += int(num)
    return sum
