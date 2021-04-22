# 백준15650_N과 M (2)_백트래킹_실버 3
# sort를 사용안해도 되는 풀이법, 시간복잡도가 작다

def dfs():
    if len(nums) == m:
        print(*nums)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            nums.append(i+1)
            dfs()
            nums.pop()
            for j in range(i+1, n):
                visited[j] = 0

n, m = map(int, input().split())
visited = [0] * n
nums = []
dfs()



