# 프로그래머스_두 정수 사이의 합_수학_레벨 1

def solution(a,b):
    sum = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b,a+1):
            sum += i
    elif a < b:
        for i in range(a,b+1):
            sum += i
    return sum

a,b = map(int, input().split())
print(solution(a,b))