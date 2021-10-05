# 자료구조 과제_우선순위 큐

import heapq

n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))
    line[i].reverse()

heap = []
for i in range(n):
    if line[i][-1] != 0:
        heapq.heappush(heap, (line[i].pop(), i))

while heap:
    priority, idx = heapq.heappop(heap)
    if line[idx][-1] != 0:
        heapq.heappush(heap, (line[idx].pop(), idx))
    print(priority)
