# 프로그래머스_문자열 다루기 기본_문자열_레벨 1

def solution(s):
    if s.isnumeric():
        if len(s) == 4 or len(s) == 6:
            return True
    return False
