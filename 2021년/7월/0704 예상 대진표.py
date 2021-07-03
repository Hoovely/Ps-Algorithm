# 프로그래머스_예상 대진표_수학_레벨 2

def solution(n, a, b):
    count = 0
    while a != b:
        count += 1
        a = (a+1)//2
        b = (b+1)//2

    return count


print(solution(8, 4, 7))
