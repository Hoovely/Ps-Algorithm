# 백준17103_골드바흐 파티션_수학_실버 2
# 1,000,000까지의 소수를 모두 구해놓고 시작

import sys

input = sys.stdin.readline

nums = [1]*(1000001)
for i in range(2,1000001):
    if nums[i] == 0:
        continue
    for j in range(i*2,1000001,i):
        nums[j] = 0

prime = []
for i in range(2,1000001):
    if nums[i]:
        prime.append(i)

for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(len(prime)):
        if prime[i] > n - prime[i]: # 중복된거 제거용, dp
            break
        if nums[n- prime[i]]:
            count += 1
    print(count)
        
        
    

