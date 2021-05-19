# 백준11727_2xN 타일링 2_DP_실버 3
# n-2항*2 + n-1인 규칙을 알아냄

def pibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3

    if dp[n]:
        return dp[n]
    else:
        dp[n] = pibonacci(n-2)*2 + pibonacci(n-1)
        return dp[n]


n = int(input())
dp = [0]*(n+1)
print(pibonacci(n) % 10007)
