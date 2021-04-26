# 백준10814_나이순 정렬_정렬_실버 5
# str(i)로 입력되어서 오름차순 정렬하면 9보다 10, 11이 먼저 정렬되게됨
# 람다식으로 풀이 진행

import sys

n = int(sys.stdin.readline())
pipple = []
for i in range(n):
    a,b = sys.stdin.readline().split()
    pipple.append((int(a), b))
pipple_sorted = sorted(pipple, key=lambda x : x[0])
for i in pipple_sorted:
    print(i[0], i[1])
    
