# 백준9461_파도반 수열_DP_실버 3

dp = [0] * 101

def P(n):
    if n < 4:
        return 1
    elif n < 6:
        return 2
    elif dp[n]:
        return dp[n]
    else:
        dp[n] = P(n-5) + P(n-1)
        return dp[n]

for _ in range(int(input())):
    n = int(input())
    print(P(n))

