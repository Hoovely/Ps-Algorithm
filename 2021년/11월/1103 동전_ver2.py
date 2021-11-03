# 백준_9084_동전_DP_골드 5
# 시간복잡도 최소화 버젼

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    dp = [0]*(m+1)
    dp[0] = 1
    for i in range(n):
        for j in range(coin[i], m+1):
            dp[j] += dp[j-coin[i]]
    print(dp[m])
