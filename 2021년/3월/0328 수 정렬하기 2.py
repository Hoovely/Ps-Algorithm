# 백준2751_수 정렬하기 2_정렬_실버 5
# 파이썬 내장함수 써도 시간초과 뜸
# 병합정렬 사용 , O(nlogn)

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    mid = len(unsorted_list)//2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)

    return merge(left1, right1)

def merge(left, right):
    i = 0
    j = 0
    sorted_list = []

    while (i<len(left)) and (j<len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    while (i<len(left)):
        sorted_list.append(left[i])
        i += 1
    
    while (j<len(right)):
        sorted_list.append(right[j])
        j += 1
    
    return sorted_list

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

for i in merge_sort(nums):
    print(i)


