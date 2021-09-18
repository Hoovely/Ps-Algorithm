# 자료구조 과제 4

import sys
input = sys.stdin.readline

n = int(input())
building = []
for _ in range(n):
    building.append(list(map(int, input().split())))
building.sort()
