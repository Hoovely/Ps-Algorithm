# 프로그래머스_여행경로_DFS_레벨 3

def dfs(now, answer, tickets):
    answer.append(now)
    lst = []
    for i in range(len(tickets)):
        if tickets[i][1] == 'visit':
            continue
        if tickets[i][0] == now:
            lst.append([tickets[i][1], i])
    if lst:
        lst.sort()
        next = lst[0][0]
        tickets[lst[0][1]][1] = 'visit'
        dfs(next, answer, tickets)


def solution(tickets):
    answer = []
    dfs("ICN", answer, tickets)
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
