# 백준2751_수 정렬하기 2_정렬_실버 5

def merge_sort(us_lst):
    if len(us_lst) <= 1:
        return us_lst

    mid = len(us_lst) // 2
    left = us_lst[:mid]
    right = us_lst[mid:]

    left1 = merge_sort(left)
    right1= merge_sort(right)

    return merge(left1, right1)

def merge(left, right):
    i = 0
    j = 0
    s_lst = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            s_lst.append(left[i])
            i += 1
        else:
            s_lst.append(right[j])
            j += 1
    
    while i < len(left):
        s_lst.append(left[i])
        i += 1

    while j < len(right):
        s_lst.append(right[j])
        j += 1

    return s_lst

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

for i in merge_sort(nums):
    print(i)