# 백준_1339_단어 수학_그리디_골드 4

import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().strip())

alphabet = [0 for i in range(26)]
for l in lst:
    i = 0
    while l:
        alphabet[ord(l[-1])-ord('A')] += pow(10, i)
        i += 1
        l = l[:-1]

alphabet.sort(reverse=True)
result = 0
for i in range(9, 0, -1):
    result += alphabet[9-i]*i

print(result)
