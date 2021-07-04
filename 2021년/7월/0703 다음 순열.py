# 백준_10972_다음 순열_수학_실버 3
# itertools 사용하려다가 시간초과!

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
find = False

for i in range(n-1,0,-1):
    if lst[i-1] < lst[i]:
        for j in range(n-1,0,-1):
            if lst[i-1] < lst[j]:
                lst[i-1],lst[j] = lst[j],lst[i-1]
                lst = lst[:i] + sorted(lst[i:])
                find = True
                break
    if find:
        print(*lst)
        break
    
if not find:
    print(-1)
