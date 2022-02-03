# 프로그래머스_n^2 배열 자르기_월간 코드 챌린지_레벨 2

def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        x = i//n + 1
        y = i % n + 1
        if x > y:
            answer.append(x)
        else:
            answer.append(y)

    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         if i > j:
    #             answer.append(i)
    #         else:
    #             answer.append(j)

    return answer


print(solution(4, 7, 14))
