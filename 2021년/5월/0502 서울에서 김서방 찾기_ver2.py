# 프로그래머스_서울에서 김서방 찾기_문자열_레벨 1
# index를 사용하여 1줄로 해결한 풀이방법

seoul = ["Jane", "Kim"]

def solution(seoul):
    return "김서방은 " + str(seoul.index("Kim")) + "에 있다"

print(solution(seoul))