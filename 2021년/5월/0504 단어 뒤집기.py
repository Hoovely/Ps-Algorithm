# 백준9093_단어 뒤집기_문자열_브론즈 1

import sys

for _ in range(int(input())):
    lst = sys.stdin.readline().split()
    for i in lst:
        print(''.join(reversed(i)), end=" ")
    print()
