# 백준15651_N과 M (3)_백트래킹_실버 3

import sys

def dfs(index):
    if m == index:
        print(*nums)
        return
    for i in range(n):
        nums[index] = i+1
        dfs(index+1)

n, m = list(map(int,sys.stdin.readline().split()))
nums = [0]*m
dfs(0)