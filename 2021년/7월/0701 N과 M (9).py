# 백준_15663_N과 M (9)_백트래킹_실버 2
# itertools 사용한 풀이

import itertools

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = sorted(list(set(itertools.permutations(nums, m))))
for num in result:
    print(' '.join(map(str, num)))
