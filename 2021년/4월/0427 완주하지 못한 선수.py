# 프로그래머스_완주하지 못한 선수_해시_레벨 1
# 시도 1, list를 dictionary사용하여 key : value = "이름" : "이름의 갯수" 로 participant를 변환
# completion과 곂치는 이름이 있을경우 해당 value의 값을 -1
# value가 1인 key를 answer에 대입 
# O(n^2)이라서 시간초과
# 시도 2, 두 list를 정렬하고 하나씩 비교한다.
# 다른값이 존재할경우 그 값을 return
# for문이 종료되어도 다른값이 없을경우 마지막값을 return

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[i+1]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]	
print(solution(participant, completion))

