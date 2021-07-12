# 프로그래머스_시저 암호_문자열_레벨 1

def solution(s, n):
    answer = ""
    for i in range(len(s)):
        ascii_num = ord(s[i]) + n
        if s[i].isupper():
            if ascii_num > 90:
                answer += chr(65 + ascii_num % 91)
            else:
                answer += chr(ascii_num)
        elif s[i].islower():
            if ascii_num > 122:
                answer += chr(97 + ascii_num % 123)
            else:
                answer += chr(ascii_num)
        else:
            answer += s[i]
    return answer

print(solution("a B z",4))