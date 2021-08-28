# 백준_3745_오름세_이분 탐색_골드 2

import sys
from bisect import bisect_left
input = sys.stdin.readline

while 1:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        dp = []

        for num in nums:
            k = bisect_left(dp, num)
            if k >= len(dp):
                dp.append(num)
            else:
                dp[k] = num

        print(len(dp))

    except:
        break
