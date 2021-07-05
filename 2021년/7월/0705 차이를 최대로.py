# 백준_10819_차이를 최대로_백트래킹_실버 2

def solve():
    if n == len(result):
        sum = 0
        for i in range(1, n):
            sum += abs(result[i-1] - result[i])
        sum_num.append(sum)
        return
    for i in range(n):
        if visited[i] == 0:
            result.append(nums[i])
            visited[i] = 1
            solve()
            visited[i] = 0
            result.pop()


n = int(input())
nums = sorted(list(map(int, input().split())))
visited = [0]*n
result = []
sum_num = []

solve()

print(max(sum_num))
