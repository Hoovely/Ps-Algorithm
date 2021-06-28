# 백준_15656_N과 M (7)_백트래킹_실버 3
# 중복순열 ==> product

import itertools

n, m = map(int, input().split())
nums = list(map(int, input().split()))

result = sorted(list(itertools.product(nums, repeat=m)))
for i in result:
    for j in i:
        print(j, end=' ')
    print()
