# 백준15649_N과 M (1)_백트래킹_실버 3
# 8 중 for 문??
# 씨발 모르겠다

def dfs(dp, m):
    if dp == m:
        for i in nums:
            print(str(i), end = ' ')
        print()
        # print(*nums)
        return    
    for i in range(len(visited)):
        if visited[i] == 0:
            visited[i] = 1
            nums.append(i+1)
            dfs(dp+1, m)
            visited[i] = 0
            nums.pop()

n,m = map(int, input().split())
visited = [0]*n
nums = []
dfs(0, m)
