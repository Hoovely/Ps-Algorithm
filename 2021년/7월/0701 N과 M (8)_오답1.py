# 백준_15657_N과 M (8)_백트래킹_실버 3
# 오답 1

def solve(index):
    if m == len(result):
        print(*result)
        return
    for i in range(index, n):
        result.append(nums[i])
        solve(i)
        result.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []
solve(0)
