# 프로그래머스_문자열을 정수로 바꾸기_문자열_레벨 1

def solution(s):
    if s[0] == '-':
        return -1*int(s[1:])
    else:
        return int(s)
