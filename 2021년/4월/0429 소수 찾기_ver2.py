# 프로그래머스_소수 찾기_수학_레벨 1
# ver1의 방법보다 빠른 방법

n = int(input())

def solution(n):
    nums = [0 for _ in range(n+1)] 
    prime = []
    for i in range(2, n+1): 
        if nums[i] == 1:
            continue
        else:
            prime.append(1)
        for j in range(i, n+1, i):
            nums[j] = 1
    return print(prime.count(1))

solution(n)