# 백준1181_단어 정렬_문자열_실버 5

import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(input())

lst = sorted(list(set(lst)))
lst.sort(key=len)

for i in lst:
    print(i)