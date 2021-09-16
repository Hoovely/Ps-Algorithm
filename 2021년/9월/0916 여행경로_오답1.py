# 프로그래머스_여행경로_DFS_레벨 3
# 오답 1

answer = ["ICN"]


def dfs(now, tickets, visited, cnt):
    if cnt == len(tickets):
        return True

    for i in range(len(tickets)):
        if visited[i] == 1:
            continue

        if tickets[i][0] == now:
            visited[i] = 1
            answer.append(tickets[i][1])
            flag = dfs(tickets[i][1], tickets, visited, cnt+1)
            if flag:
                return True
            visited[i] = 0

    answer.pop()
    return False


def solution(tickets):
    tickets.sort()
    visited = [0 for _ in range(len(tickets)+1)]
    dfs("ICN", tickets, visited, 0)
    return answer
