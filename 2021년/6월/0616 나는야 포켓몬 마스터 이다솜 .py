# 백준1620_나는야 포켓몬 마스터 이다솜_믄자열_실버 4
# try except로 정수, 문자열 판별

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poketmon = [0]
poketmon_dict = []
for i in range(1, n+1):
    poketmon.append(input().strip())
    poketmon_dict.append([poketmon[i], i])
poketmon_dict = dict(poketmon_dict)

for i in range(m):
    name = input().strip()
    try:
        name = int(name)
        print(poketmon[name])

    except:
        print(poketmon_dict[name])
