# 백준_1182_부분수열의 합_백트래킹_실버 2
# combinations 함수를 이용하여 길이가 i인 집합을 구하고 각각의 집합의 합이 s와 같다면 count += 1 해준다

import itertools

n, s = map(int, input().split())
lst = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    for j in list(itertools.combinations(lst, i)):
        if s == sum(j):
            count += 1

print(count)
