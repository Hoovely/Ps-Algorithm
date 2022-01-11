# 백준_9934_완전 이진 트리_트리_실버 1

import sys
sys.setrecursionlimit(10**8)

def InsertTree(depth, start, end):
    if start >= end: return

    mid = (start+end)//2
    tree[depth].append(lst[mid])
    InsertTree(depth+1, start, mid)
    InsertTree(depth+1, mid+1, end)

n = int(input())
lst = list(map(int,input().split()))
tree = [[] for _ in range(n)]

InsertTree(0, 0, 2**n-1)

for leaf in tree:
    print(*leaf)

