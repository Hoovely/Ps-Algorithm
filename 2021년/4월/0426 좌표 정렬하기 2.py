# 백준11651_좌표 정렬하기 2_정렬_실버 5

import sys

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int,sys.stdin.readline().split())))
sort_maps = sorted(maps, key=lambda x : (x[1],x[0]))
for i in sort_maps:
    print(i[0], i[1])

