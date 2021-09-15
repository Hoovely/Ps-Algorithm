# 프로그래머스_여행경로_DFS_레벨 3

answer = ["ICN"]


def dfs(city, tickets, visited, cnt):
    if len(tickets) == cnt:
        return True

    for i in range(len(tickets)):
        if visited[i] == 1:
            continue

        if tickets[i][0] == city:
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


tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))

# T 1 : [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
# ans : ["ICN", "B", "ICN", "A", "D", "A"]

# T 2: [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
# ans : ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]

# T 3 : [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
# ans : ["ICN", "COO", "ICN", "BOO", "DOO"]

# 4번 반례 해결하니 2번 테케 통과했습니다.
# T 4: [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]
# ans : ["ICN", "SFO", "ICN", "SFO", "QRE"]

# 가장 골치아픈 1번테케는 5번반례 해결후 통과했습니다.
# T 5 : [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
# ans : ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
