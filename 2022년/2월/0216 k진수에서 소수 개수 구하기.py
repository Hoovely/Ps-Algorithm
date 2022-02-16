# 프로그래머스_k진수에서 소수 개수 구하기_카카오_레벨 2

import math


def is_prime_number(x):
    if x < 2:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(n, k):
    answer = 0

    k_num = ''
    while n > 0:
        n, mod = divmod(n, k)
        k_num += str(mod)
    k_num = k_num[::-1]

    StackNum = ''
    for num in k_num:
        if num == '0' and StackNum != '':
            if is_prime_number(int(StackNum)):
                answer += 1
            StackNum = ''
        elif num != '0':
            StackNum += num
    if StackNum != '':
        if is_prime_number(int(StackNum)):
            answer += 1

    return answer


print(solution(110011, 10))
