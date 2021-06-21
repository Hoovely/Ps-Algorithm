# 프로그래머스_핸드폰 번호 가리기_문자열_레벨 1

def solution(phone_number):
    return (len(phone_number)-4) * '*' + phone_number[-4:]


phone_number = "01033334444"
print(solution(phone_number))
