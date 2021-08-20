# 프로그래머스_기능개발_스택/큐_레벨 2

from collections import deque


def solution(progresses, speeds):
    result = []
    progresses_queue = deque(progresses)
    speeds_queue = deque(speeds)
    cnt = 0
    while 1:
        for i in range(len(progresses_queue)):
            progresses_queue[i] += speeds_queue[i]

        while progresses_queue:
            if progresses_queue[0] >= 100:
                progresses_queue.popleft()
                speeds_queue.popleft()
                cnt += 1
            else:
                if cnt:
                    result.append(cnt)
                cnt = 0
                break

        if len(progresses_queue) == 0:
            result.append(cnt)
            return result


print(solution([96, 99, 98, 97], [1, 1, 1, 1]))
