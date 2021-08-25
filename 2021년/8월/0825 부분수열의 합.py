# 백준_14225_부분수열의 합_브루트포스_실버 1

import itertools

n = int(input())
S = list(map(int, input().split()))
nums = []
for i in range(2, n+1):
    nums.append(list(itertools.combinations(S, i)))

for num in nums:
    for i in range(len(num)):
        S.append(sum(num[i]))

S = sorted(list(set(S)))
result = 0
for i in range(len(S)):
    if S[i] != i+1:
        result = i+1
        break

if result:
    print(result)
else:
    print(max(S)+1)
