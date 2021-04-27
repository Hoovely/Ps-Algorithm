# 프로그래머스_완주하지 못한 선수_해시_레벨 1
# zip을 이용한 풀이

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]




participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]	
print(solution(participant, completion))
