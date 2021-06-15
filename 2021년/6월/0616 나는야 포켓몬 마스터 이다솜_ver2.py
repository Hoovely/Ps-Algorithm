# 백준1620_나는야 포켓몬 마스터 이다솜_믄자열_실버 4
# isalpha()로 정수, 문자열 판별

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poketmon = [0] * (n+1)
poketmon_dict = {}
for i in range(1, n+1):
    x = input().strip()
    poketmon_dict[x] = i
    poketmon[i] = x

for i in range(m):
    name = input().strip()
    if name.isalpha():
        print(poketmon_dict[name])
    else:
        print(poketmon[int(name)])
