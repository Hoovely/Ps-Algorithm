# 백준2108_통계학_정렬_실버 4

from collections import Counter

def average():
    return round(sum(nums)/n)

def mid():
    nums.sort()
    return nums[n//2]

def many():
    new_nums = Counter(nums)

def nums_range():
    return (nums[-1]-nums[0])


n = int(input())
nums = []
result = []
for _ in range(n):
    nums.append(int(input()))



result.append(average())
result.append(mid())
result.append(many())
result.append(nums_range())

# 산술평균
# 중앙값
# 최빈값
# 범위