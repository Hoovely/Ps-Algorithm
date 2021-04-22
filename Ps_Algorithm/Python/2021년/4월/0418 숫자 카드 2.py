# 백준10816_숫자 카드 2_이분 탐색_실버 4
# 첫 번쨰 시도, count 써서 했으나 시간초과 m*O(n)
# 타겟과 같은 값을 찾는 것은 해결, 같은 값이 여러개 있을경우 count 하는 것을 해결 못 함
# 혼자 1시간 삽질하다가 구글링
# 두 번째 시도, 정렬된 n_nums 의 값들을 이분탐색해서 각 원소의 갯수를 dictionary에 저장시킴
# m_nums 의 값 하나하나당 갯수를 반복문 사용하여 출력
# 메모리 108548kb 시간 4384ms

import sys

def binary_search(start, mid, end, target):
    if n_nums[mid] == target:    
        return n_nums[start:end+1].count(target)
    
    if n_nums[mid] < target:
        return binary_search(mid+1, (mid+1+end)//2, end, target)
    
    if n_nums[mid] > target:
        return binary_search(start, (mid-1+start)//2, mid-1, target)


n = int(sys.stdin.readline())
n_nums = list(map(int,sys.stdin.readline().split()))
n_nums.sort()

m = int(sys.stdin.readline())
m_nums = list(map(int,sys.stdin.readline().split()))

n_dic = {}

for i in n_nums:
    if i not in n_dic:
        n_dic[i] = binary_search(0,(n-1)//2 , n-1, i)

for i in m_nums:
    if i in n_dic:
        print(n_dic[i], end=" ")
    else:
        print(0, end=" ")


