# 백준_14888_연산자 끼워넣기_백트래킹_실버 1

import sys
import itertools
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
cmds = list(set(itertools.permutations(
    ['+']*a + ['-']*b + ['*']*c + ['//']*d, n-1)))

max_num = sys.maxsize*-1
min_num = sys.maxsize

for cmd in cmds:
    sum_num = nums[0]
    for i in range(n-1):
        if cmd[i] == '+':
            sum_num += nums[i+1]
        elif cmd[i] == '-':
            sum_num -= nums[i+1]
        elif cmd[i] == '*':
            sum_num *= nums[i+1]
        elif cmd[i] == '//':
            sum_num = int(sum_num / nums[i+1])
    if sum_num > max_num:
        max_num = sum_num
    if sum_num < min_num:
        min_num = sum_num

print(max_num)
print(min_num)
