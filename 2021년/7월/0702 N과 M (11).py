# 백준_15665_N과 M (11)_백트래킹_실버 2
# dfs 풀이

def solve():
    if m == len(result):
        print(*result)
        return
    for i in range(len(nums)):
        result.append(nums[i])
        solve()
        result.pop()


n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
result = []
solve()
