# 백준14501_퇴사_브루트 포스_실버 4
# 오답 1

n = int(input())
T = [0]*n
P = [0]*n
dp = [0]*(n+1)
for i in range(n):
    T[i], P[i] = map(int, input().split())

for i in range(n-1, -1, -1):
    if i + T[i] <= n:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
