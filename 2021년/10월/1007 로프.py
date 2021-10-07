# 백준_2217_로프_그리디_실버 4

import sys
input = sys.stdin.readline

n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))
rope.sort()

max_w = 0
for i in range(n):
    max_w = max(max_w, rope[i]*(n-i))

print(max_w)
