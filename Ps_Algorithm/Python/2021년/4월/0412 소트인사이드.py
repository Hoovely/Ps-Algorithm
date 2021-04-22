# 백준1427_소트인사이드_정렬_실버 5

n = str(input())
nums = []
for i in n:
    nums.append(int(i))
for i in range(len(nums)):
    for j in range(0, len(nums)-i-1):
        if nums[j] < nums[j+1]:
            temp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = temp
        
for i in nums:
    print(i,end='')
