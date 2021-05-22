# 백준17103_골드바흐 파티션_수학_실버 2
# 오답 1

import sys
input = sys.stdin.readline

nums = [1] * 1000001
prime = []
for i in range(2, 1000001):
    if nums[i] == 0:
        continue
    prime.append(i)
    for j in range(2*i, 1000001, i):
        nums[j] = 0

for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in prime:
        if i > n//2:
            break
        if nums[i] and nums[n-i]:
            count += 1
    print(count)
