# 백준_4150_피보나치 수_DP_실버 4

import sys
sys.setrecursionlimit(10**9)


def fibo(i):
    if i == 1 or i == 2:
        return 1

    if dp[i]:
        return dp[i]
    else:
        dp[i] = fibo(i-1) + fibo(i-2)
        return dp[i]


n = int(input())
dp = [0, 1, 1] + [0] * (n-2)

print(fibo(n))
