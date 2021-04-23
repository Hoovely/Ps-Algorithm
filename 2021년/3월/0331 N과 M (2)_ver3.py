# 백준15650_N과 M (2)_백트래킹_실버 3
# sort를 사용하여 푸는 방법중 깔끔한 방법

def dfs():
    if len(nums) == m:
        if nums == sorted(nums): # 오름차순으로 정렬되어있는 nums 만 출력
            print(*nums)
            return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            nums.append(i+1)
            dfs()
            visited[i] = 0
            nums.pop()

n,m = map(int, input().split())
visited = [0] * n
nums = []
dfs()