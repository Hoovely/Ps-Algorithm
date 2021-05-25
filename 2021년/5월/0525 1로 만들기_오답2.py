# 백준1463_1로 만들기_DP_실버 3
# 오답 2

x = int(input())
dp = [0,0,1,1]

for i in range(4, x+1):
    dp.append(dp[i-1] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[x])