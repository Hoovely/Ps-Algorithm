# 백준_2407_조합_DP_실버 2

def fac(n):
    if dp[n-1]:
        return dp[n-1]*n
    else:
        dp[n-1] = fac(n-1)
        return dp[n-1]*n


n, m = map(int, input().split())
dp = [0]*101
dp[0] = 1
dp[1] = 1
dp[2] = 2
print(fac(n)//(fac(n-m)*fac(m)))
