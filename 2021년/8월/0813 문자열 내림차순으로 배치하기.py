# 프로그래머스_문자열 내림차순으로 배치하기_문자열_레벨 1

def solution(s):
    result = ""
    for i in sorted(list(s), reverse=True):
        result += i
    return result


print(solution("Zbcdefg"))
