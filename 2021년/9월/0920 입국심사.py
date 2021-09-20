# 프로그래머스_구현_신규 아이디 추천_레벨 1

def solution(new_id):
    answer = ''
    cnt = 0
    # 1,2단계
    for i in new_id:
        if i.isupper():
            answer += i.lower()
        elif i.islower() or i == '-' or i.isdigit() or i == '_':
            answer += i
    # 3단계
    for i in new_id:
        if i == '.':
            cnt += 1
            continue
        else:
            if cnt >= 1:
                answer += '.'
                cnt = 0

    # 4단계
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:-1]
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    if len(answer) < 3:
        while len(answer) != 3:
            answer += answer[-1]

    return answer


print(solution("=.="))
