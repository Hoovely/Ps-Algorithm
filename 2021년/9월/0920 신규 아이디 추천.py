# 프로그래머스_구현_신규 아이디 추천_레벨 1

def solution(new_id):
    answer = ''
    # 1,2단계
    for i in new_id:
        if i.isupper():
            answer += i.lower()
        elif i.islower() or i == '-' or i.isdigit() or i == '_' or i == '.':
            answer += i

    cnt = 0
    temp = ''
    # 3단계
    for i in answer:
        if i == '.':
            if cnt:
                continue
            else:
                temp += i
                cnt = 1
        else:
            temp += i
            cnt = 0
    answer = temp

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
