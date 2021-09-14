# 백준_1863_스카이라인 쉬운거_스택_실버 1
# 오답 1

import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
lst.append([0, 0])

cnt = 0
skyline = []
for i in range(n+1):
    while skyline and skyline[-1] > lst[i][1]:
        cnt += 1
        skyline.pop()
    if skyline and skyline[-1] == lst[i][1]:
        continue
    skyline.append(lst[i][1])

print(cnt)
