# 백준_1010_다리 놓기_DP_실버 5
# 조합을 구하면 된다!

dp = [0]*31
for i in range(31):
    if i <= 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-1]*i


def combi(n, m):
    x = max(n, m)
    y = min(n, m)
    return dp[x]//(dp[y]*dp[x-y])


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(combi(n, m))
