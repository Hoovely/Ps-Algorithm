# 백준15650_N과 M (2)_백트래킹_실버 3
# 처음에 풀었던 방법이, ㅈㄴ 더러워서 시간초과 뜬다고 예상했으나 통과 ㅇㅅㅇ

def dfs(dp,n,m):
    if dp == m:
        sort_nums = sorted(nums)
        for i in nums_old:
            if i == sort_nums:
                return
        nums_old.append(sort_nums)
        print(*nums)
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            nums.append(i+1)
            dfs(dp+1,n,m)
            visited[i] = 0
            nums.pop()

n, m = map(int, input().split())
visited = [0] * n
nums = []
nums_old = []
dfs(0,n,m)

# nums = [8,3,4,6]
# sort_nums = sorted(nums)
# print(sort_nums)
# print(nums)