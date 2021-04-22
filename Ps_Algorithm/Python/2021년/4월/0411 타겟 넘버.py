# 프로그래머스_타겟 넘버_dfs/bfs_레벨 2
# 못품

import sys
sys.setrecursionlimit(10**6)

def dfs(nums, target):
    global answer
    for i in range(len(nums)):
        if sum(nums) == target:
            answer += 1
            return
        else:
            temp = nums[i]
            nums[i] = 0
            dfs(nums, target+temp)
            nums[i] = temp


nums = list(map(int,input().split()))
target = int(input())
answer = 0
dfs(nums,target)
print(answer)


