# 백준_15663_N과 M (9)_백트래킹_실버 2
# 오답 1

def solve():
    if len(m_nums) == m:
        result.append(tuple(m_nums[:]))
        return
    for i in range(n):
        if visited[i] == 0:
            m_nums.append(nums[i])
            visited[i] = 1
            solve()
            visited[i] = 0
            m_nums.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
m_nums = []
visited = [0]*n
result = []

solve()

for num in sorted(list(set(result))):
    print(' '.join(map(str, num)))
