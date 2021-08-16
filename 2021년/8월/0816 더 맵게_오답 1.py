# 프로그래머스_더 맵게_힙_레벨 2
# 오답 1

import heapq


def solution(scoville, k):
    cnt = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        spicy = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, spicy)
        cnt += 1

        if scoville[0] >= k:
            return cnt
    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
