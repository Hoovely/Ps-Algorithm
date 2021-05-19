# 백준11726_2xN 타일링_DP_실버 3
# n+2 하면서 백트래킹한다는 규칙을 알아내서 n=10까지 for문 써가면서 구현
# 피보나치수열을 따른다는 것을 알아냄

def pibonacci(n):
    if n < 3:
        return n

    if dp[n]:
        return dp[n]
    else:
        dp[n] = pibonacci(n-2) + pibonacci(n-1)
        return dp[n]


n = int(input())
dp = [0]*(n+1)
print(pibonacci(n) % 10007)
