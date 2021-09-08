# 프로그래머스_수학_음양 더하기_레벨 1

def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i]:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    return result
