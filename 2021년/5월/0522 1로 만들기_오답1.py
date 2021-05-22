# 백준1463_1로 만들기_DP_실버 3
# 오답 1

n = int(input())
dp = [0,0,1,1]

for i in range(4, n+1):
    dp.append(dp[i-1] + 1)

    if i % 2 == 0 and dp[-1] > dp[i//2] + 1:
        dp.pop()
        dp.append(dp[i//2] + 1)
        
    if i % 3 == 0 and dp[-1] > dp[i//3] + 1:
        dp.pop()
        dp.append(dp[i//3] + 1)

print(dp[n]) 
