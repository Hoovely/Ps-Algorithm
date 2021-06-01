# 백준1309_동물원_DP_실버 1

n = int(input())
dp = [1, 3] + [0] * (n-1)
for i in range(2, n+1):
    dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
print(dp[n])
