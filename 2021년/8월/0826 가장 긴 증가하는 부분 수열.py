# 백준_11053_가장 긴 증가하는 부분 수열_DP_실버 2
# n의 최대값이 1000 이기 때문에 O(n^2)인 DP로 풀이 작성

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
    for j in range(i+1, n):
        if nums[i] < nums[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))
