# 백준17087_숨바꼭질 6_수학_실버 1
# 오답1

import sys


def gcd(a, b):
    while a:
        temp = b % a
        b = a
        a = temp
    return b


input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
d_list = []

for num in nums:
    d_list.append(abs(num-s))

d = min(d_list)
for i in range(len(d_list)):
    d = gcd(d, d_list[i])

print(d)
