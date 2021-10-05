# 자료구조 과제_우선순위 큐
# ver2

import heapq

n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))
lst_idx = [0]*n

heap = []
for i in range(n):
    if line[i][0] != 0:
        heapq.heappush(heap, (line[i][0], i))

while heap:
    priority, idx = heapq.heappop(heap)
    lst_idx[idx] += 1
    next_idx = lst_idx[idx]
    if line[idx][next_idx] != 0:
        heapq.heappush(heap, (line[idx][next_idx], idx))
    print(priority)
