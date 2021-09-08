# 프로그래머스_수학_3진법 뒤집기_레벨 1

def solution(n):
    n_3 = ''
    while n:
        temp, div = divmod(n, 3)
        n_3 += str(div)
        n = temp
    return int(n_3, 3)


print(solution(125))
