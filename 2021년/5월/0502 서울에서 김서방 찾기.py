# 프로그래머스_서울에서 김서방 찾기_문자열_레벨 1

seoul = ["Jane", "Kim"]

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 " + str(i) + "에 있다"

print(solution(seoul))