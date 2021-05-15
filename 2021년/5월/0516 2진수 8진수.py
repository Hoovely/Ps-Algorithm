# 백준1373_2진수 8진수_수학_브론즈 2
# 2진수 -> 10진수 -> 8진수 == 시간초과
# 파이썬 내장함수 사용

import sys

input = sys.stdin.readline
num_2 = '0b' + str(input().strip())
print(format(int(num_2, 2), 'o'))
