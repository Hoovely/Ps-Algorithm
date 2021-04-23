# 백준15651_N과 M (3)_백트래킹_실버 3

def dfs():
    if len(nums) == m:
        print(*nums)
        return
    for i in range(n):
        nums.append(i+1)
        dfs()
        nums.pop()

n,m = map(int ,input().split())
nums = []
dfs()
