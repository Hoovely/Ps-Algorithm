# 백준_6603_로또_백트래킹_실버 2

import sys
input = sys.stdin.readline


def solve(k):
    if len(nums) == 6:
        result.append(tuple(sorted(nums)))
        return

    for i in range(k):
        if visited[i] == 0:
            nums.append(lst[i])
            visited[i] = 1
            solve(k)
            visited[i] = 0
            nums.pop()


while 1:
    lst = list(map(int, input().split()))
    k = lst[0]
    if k == 0:
        break
    lst = lst[1:]
    visited = [0]*k
    nums = []
    result = []

    solve(k)

    for num in sorted(list(set(result))):
        print(' '.join(map(str, num)))

    print()
