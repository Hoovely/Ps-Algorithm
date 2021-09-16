# 알고스팟_록 페스티벌_구현_하

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, l = map(int, input().split())
    days = list(map(int, input().split()))

    min_num = 151616123
    for i in range(n-l+1):
        cnt = 1
        cost = 0
        for j in range(i, n):
            cost += days[j]

            if cnt >= l:
                if cost/cnt < min_num:
                    min_num = cost/cnt

            cnt += 1

    print("{:.12f}".format(min_num))
