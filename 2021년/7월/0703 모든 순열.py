# 백준_10974_모든 순열_브루트포스_실버 3

import sys
import itertools
input = sys.stdin.readline

n = int(input())
nums = [i for i in range(1, n+1)]
result = list(itertools.permutations(nums, n))

for num in result:
    print(' '.join(map(str, num)))
