# 백준_15666_N과 M (12)_백트래킹_실버 2

def solve(index):
    if m == len(m_nums):
        result.append(tuple(m_nums))
        return
    for i in range(index, n):
        m_nums.append(nums[i])
        solve(i)
        m_nums.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
m_nums = []
result = []

solve(0)

for num in sorted(list(set(result))):
    print(' '.join(map(str, num)))
