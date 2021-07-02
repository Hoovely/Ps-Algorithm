# 백준_15665_N과 M (11)_백트래킹_실버 2
# itertools 풀이

import itertools

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
result = sorted(list(itertools.product(nums, repeat=m)))

for num in result:
    print(' '.join(map(str, num)))
