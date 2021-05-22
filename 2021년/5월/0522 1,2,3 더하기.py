# 백준9095_1,2,3 더하기_DP_실버 3

nums = [0,1,2,4]
for i in range(4, 12):
        nums.append(nums[i-3] + nums[i-2] + nums[i-1]) 
for _ in range(int(input())):
    print(nums[int(input())])
    
