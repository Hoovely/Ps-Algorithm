# 백준_11048_이동하기_DP_실버 1
# 다이나믹이 뭐예요? 에서 가중치가 추가된 버젼!

n, m = map(int, input().split())
dp = []
for i in range(n+1):
    if i == 0:
        dp.append([0]*(m+1))
    else:
        dp.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1:
            dp[i][j] += dp[i][j-1]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n][m])
