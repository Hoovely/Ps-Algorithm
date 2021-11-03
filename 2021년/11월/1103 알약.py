# 백준_4811_알약_DP_골드 5

import sys
input = sys.stdin.readline

factorial_num = [0]*61
factorial_num[0] = 1
factorial_num[1] = 1
for i in range(2, 61):
    factorial_num[i] = factorial_num[i-1]*i


def catalan(x):
    return (factorial_num[2*x]//factorial_num[x]**2)-((factorial_num[2*x])//(factorial_num[x+1]*factorial_num[x-1]))


for _ in range(1001):
    n = int(input())
    if n == 0:
        break
    print(catalan(n))
