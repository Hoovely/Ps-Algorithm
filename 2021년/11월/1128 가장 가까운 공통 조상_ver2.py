# 백준_3584_가장 가까운 공통 조상_트리_골드 4
# 최적화된 방법

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    parent = [0] * (n+1)
    for i in range(n-1):
        a,b = map(int,input().split())
        parent[b] = a
    x,y = map(int,input().split())
    x_list = [0,x] 
    y_list = [0,y] 

    while parent[x]:
        x_list.append(parent[x])
        x = parent[x]

    while parent[y]:
        y_list.append(parent[y])
        y = parent[y]

    cnt = 1
    while x_list[-cnt] == y_list[-cnt]:
        cnt += 1
    
    print(x_list[-cnt+1])