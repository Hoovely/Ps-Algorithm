# 백준3085_퇴사_브루트 포스_실버 4

n = int(input())
workout = []
for _ in range(n):
    workout.append(list(map(int, input().split())))

dp = [0]*(n+1)

for i in range(n-1, -1, -1):
    if workout[i][0] + i <= n:
        dp[i] = max(workout[i][1] + dp[i+workout[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
