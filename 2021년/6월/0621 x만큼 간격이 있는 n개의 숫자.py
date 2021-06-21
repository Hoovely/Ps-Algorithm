# 프로그래머스_x만큼 간격이 있는 n개의 숫자_자료구조_레벨 1

def solution(x, n):
    answer = []
    sum = x
    for _ in range(n):
        answer.append(sum)
        sum += x
    return answer


print(solution(2, 5))
