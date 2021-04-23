# 백준15649_N과 M (1)_백트래킹, dfs_실버 3

def dfs(depth, m):
    if m == depth:
        print(*nums)
        return
    for i in range(len(visited)):
        if visited[i] == 0:
            visited[i] = 1
            nums.append(i+1)
            dfs(depth+1, m)
            visited[i] = 0
            nums.pop()

n,m = map(int, input().split())
visited = [0] * n
nums = []
dfs(0, m)
