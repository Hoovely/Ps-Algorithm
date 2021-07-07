# 백준_14889_스타트와 링크_백트래킹_실버 3

import sys
import itertools
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
nums = [i for i in range(n)]
possible_team = []

for team in list(itertools.combinations(nums, n//2)):
    possible_team.append(team)

result = sys.maxsize
for i in range(len(possible_team)//2):

    team = possible_team[i]
    sum_start = 0
    for j in range(n//2):
        for k in range(n//2):
            sum_start += lst[team[j]][team[k]]

    team = possible_team[-i-1]
    sum_link = 0
    for j in range(n//2):
        for k in range(n//2):
            sum_link += lst[team[j]][team[k]]

    result = min(result, abs(sum_start-sum_link))

print(result)
