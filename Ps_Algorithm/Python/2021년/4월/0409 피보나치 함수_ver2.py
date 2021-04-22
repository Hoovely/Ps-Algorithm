# 백준1003_피보나치 함수_dp_실버 3
# 메모이제이션 기법 사용하여 재귀함수 2번 만들어서 해결하는 방법

def fibonacci_zero(zero):
    if zero == 0:
        return 1
    if zero == 1:
        return 0

    if dp_zero[zero] != -1:
        return dp_zero[zero]
    
    dp_zero[zero] = fibonacci_zero(zero-2) + fibonacci_zero(zero-1)
    return dp_zero[zero]

def fibonacci_one(one):
    if one == 0:
        return 0
    if one == 1:
        return 1
    
    if dp_one[one] != -1:
        return dp_one[one]
    
    dp_one[one] = fibonacci_one(one-2) + fibonacci_one(one-1)
    return dp_one[one]

for _ in range(int(input())):
    n = int(input())
    dp_zero = [-1]*(n+1)
    dp_one = [-1]*(n+1)
    print(fibonacci_zero(n), fibonacci_one(n))