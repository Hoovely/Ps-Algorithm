# 백준_12015_가장 긴 증가하는 부분 수열 2_이분 탐색_골드 2
# n의 최댓값이 100만 이기 때문에 이분 탐색을 사용한 문제풀이를 진행하였다.
# 이분탐색 라이브러리인 bisect 사용

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = []
for i in nums:
    k = bisect_left(dp, i)
    # 증가하는 수열일때
    if len(dp) <= k:
        dp.append(i)
    # 감소하는 수열일때
    else:
        dp[k] = i

print(len(dp))
