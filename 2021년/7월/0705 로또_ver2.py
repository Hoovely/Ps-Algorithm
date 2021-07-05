# 백준_6603_로또_백트래킹_실버 2

import sys
input = sys.stdin.readline


def solve(index, depth):
    if depth == 6:
        print(*result)
        return

    for i in range(index, len(lst)):
        result.append(lst[i])
        solve(i+1, depth+1)
        result.pop()


while 1:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    del lst[0]
    result = []
    solve(0, 0)
    print()
