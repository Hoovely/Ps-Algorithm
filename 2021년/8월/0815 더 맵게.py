# 프로그래머스_더 맵게_힙_레벨 2

import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        num1, num2 = heapq.heappop(scoville), heapq.heappop(scoville)
        result = num1 + num2*2
        heapq.heappush(scoville, result)
        cnt += 1
        if scoville[0] >= K:
            return cnt
    return -1


print(solution([1, 2, 3, 9, 10, 12], 999))
