# 백준_15655_N과 M (6)_백트래킹_실버 3
# 2차원 list에서 set 변환하려면 tuple로 1차원 list의 원소를 바꿔줘야함!

import itertools

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = itertools.permutations(nums, m)

result = []
for i in nums:
    result.append(tuple(sorted(i)))

for i in sorted(list(set(result))):
    for j in i:
        print(j, end=' ')
    print()
