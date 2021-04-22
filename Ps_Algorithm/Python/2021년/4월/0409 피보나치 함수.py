# 백준1003_피보나치 함수_dp_실버 3
# 규칙을 찾아서 푸는 방법

for _ in range(int(input())):
    n = int(input())
    zero = 1
    one = 0
    for _ in range(n):
        temp = one
        one = temp + zero
        zero = temp
    print(zero, one)

    
