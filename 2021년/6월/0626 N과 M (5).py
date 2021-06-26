# 백준15654_N과 M (5)_백트래킹_실버 3

import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = sorted(list(itertools.permutations(nums, m)))

for i in result:
    for j in i:
        print(j, end=' ')
    print()
