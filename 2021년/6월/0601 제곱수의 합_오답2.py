# 백준1699_제곱수의 합_DP_실버 3
# 오답 2

import math

n = int(input())
dp = [0] + [i for i in range(1, n+1)]
for i in range(1, n+1):
    x = int(math.sqrt(i))
    for j in range(1, x+1):
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1

print(dp[n])
