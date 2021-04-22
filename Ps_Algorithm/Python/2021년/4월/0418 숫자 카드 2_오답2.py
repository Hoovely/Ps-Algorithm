# 백준10816_숫자 카드 2_이분 탐색_실버 4

import sys

def binary_search(start, end, target):
    mid = (start+end)//2
    if n_nums[mid] == target:
        return n_nums[start:end+1].count(target)
    
    if n_nums[mid] > target:
        return binary_search(start, mid-1, target)
    
    if n_nums[mid] < target:
        return binary_search(mid+1, end, target)

n = int(sys.stdin.readline())
n_nums = list(map(int,sys.stdin.readline().split()))
n_nums.sort()
m = int(sys.stdin.readline())
m_nums = list(map(int,sys.stdin.readline().split()))

num_dic = {}

for i in n_nums:
    if i not in num_dic:
        num_dic[i] = binary_search(0, n-1, i)

for i in m_nums:
    if i in num_dic:
        print(num_dic[i], end=" ")
    else:
        print(0, end=" ")