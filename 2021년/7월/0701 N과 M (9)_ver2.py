# 백준_15663_N과 M (9)_백트래킹_실버 2
# dfs를 사용한 풀이
# 2차원 list 중복된 값 제거 ==> 1차원 list의 형식을 tuple로 변환한뒤 list 전체를 set으로 변환

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
visited = [0]*n
m_nums = []
result = []

solve()

for num in sorted(list(set(result))):
    print(' '.join(map(str, num)))
