# 백준15652_N과 M (4)_백트래킹_실버 3
# 조건(A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK)을 중심으로 생각
# 위의 조건을 생각하며 처음짰던 방법이 시간초과나서 구글링..

n, m = map(int,input().split())
visited = [0]*n
nums = []

def dfs():
    if len(nums) == m:
        print(*nums)
        return
    for i in range(n):
        if visited[i] == 0:
            nums.append(i+1)
            dfs()
            visited[i] = 1
            nums.pop()
            for j in range(i+1, n):
                visited[j] = 0

dfs()


