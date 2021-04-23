# 백준1920_수 찾기_이분 탐색_실버 4
# 이코테 이진 탐색 책 보고 코드 잘 짰으나, 재귀함수 return 값을 주지않아서 20분동안 코드 뜯어봄;

import sys
sys.setrecursionlimit(10**6)

def binary_search(arr, start, end, target):
    if start > end:
        return 0
    
    mid = (start + end) // 2 

    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        return binary_search(arr, mid+1, end, target)
    elif arr[mid] > target:
        return binary_search(arr, start, mid-1, target)

n = int(input())
n_nums = list(map(int,input().split()))
n_nums.sort()

m = int(input())
m_nums = list(map(int,input().split()))

for i in m_nums:
    if binary_search(n_nums, 0, n-1, i):
        print(1)
    else:
        print(0)
