# 백준2108_통계학_정렬_실버 4
# 최빈값이 젤 어려워서 구글링해서 Counter 함수 사용해서 시도
# 국어능력이 딸려 최빈값 중 두 번째로 작은 값이라는 것을 이해하지 못함
# 산술평균에서 반올림한 값을 잘 못 구해서 한번 틀림

import sys
from collections import Counter

def avg():
    return round(sum(nums)/len(nums)) # 산술평균 구하는 함수

def mid():
    nums.sort()
    return nums[len(nums)//2] # 정렬 후 중앙값 출력
            
def modefinder():
    cnt = Counter(nums)
    mode = cnt.most_common()
    if len(mode) > 1: # N이 1보다 클 경우
        if mode[0][1] == mode[1][1]: # 최빈값이 여러개 일때, 최빈값 중 두 번째로 작은 값의 값을 출력
            return mode[1][0]
        else:
            return mode[0][0] # 최빈값 출력
    else:
        return mode[0][0] # 최빈값 출력
    
def lst_range(): # 범위를 구하는 함수
    return (nums[-1] - nums[0]) # 제일 큰수 - 제일 작은 수

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
stat = []
stat.append(avg()) # 산술평균
stat.append(mid()) # 중앙값
stat.append(modefinder()) # 최빈값
stat.append(lst_range())

for i in stat:
    print(i)