# 프로그래머스_이상한 문자 만들기_문자열_레벨 1

def solution(s):
    answer = ''
    count = 0
    for i in s:
        if i == ' ':
            answer += ' '
            count = 0
            continue

        if count % 2 == 0:
            answer += i.upper()
        else:
            answer += i.lower()
        count += 1

    return answer