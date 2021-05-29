# 백준1002_터렛_수학_실버 4
# 두원의 접점의 갯수를 구하는 문제

import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    count = 0
    d = math.sqrt((max(x1, x2)-min(x1, x2))**2 + (max(y1, y2)-min(y1, y2))**2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    elif r1+r2 == d or max(r2, r1) == d+min(r1, r2):
        print(1)
        continue
    elif r1+r2 > d and max(r1, r2) < d+min(r1, r2):
        print(2)
        continue
    else:
        print(0)
        continue
