# 백준_2805_나무 자르기_이분 탐색_실버 3

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def binary_search(start, end):
    global flag
    if flag:
        return

    if start > end:
        return
    h = 0
    mid = (start+end)//2
    for tree in forest:
        if tree - mid > 0:
            h += tree - mid
    if h == m:
        flag = mid
        return
    if h > m:  # mid를 오른쪽으로 이동
        result.append(mid)
        return binary_search(mid+1, end)
    if h < m:  # mid를 왼쪽으로 이동
        return binary_search(start, mid-1)


n, m = map(int, input().split())
forest = list(map(int, input().split()))

flag = 0
result = [0]
binary_search(0, max(forest))

if flag:
    print(flag)
else:
    print(max(result))
