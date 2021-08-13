# 프로그래머스_문자열 내 p와 y의 개수_문자열_레벨 1

def solution(s):
    p_count = s.count('p') + s.count('P')
    y_count = s.count('y') + s.count('Y')
    if p_count == y_count:
        return True
    else:
        return False
