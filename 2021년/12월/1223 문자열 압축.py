# 프로그래머스_문자열 압축_문자열_레벨 2

def solution(s):
    len_s = len(s)
    min_num = 15161612
    for i in range(1, len_s//2+1):
        cnt = 1
        result = s[:i]
        flag = 0
        for j in range(i, len_s, i):
            if s[j-i:j] == s[j:i+j]:
                temp = s[j:i+j]
                cnt += 1
            else:
                if cnt>1:
                    if flag == 0:
                        result = str(cnt) + temp
                        flag = 1
                        cnt = 1
                    else:
                        result += str(cnt) + temp
                        cnt = 1
                else:
                    if i+j >= len_s:
                        result += s[j:]
                    else:
                        result += s[j:i+j]
        if cnt>1:
            if i == len_s//2:
                result = str(cnt) + temp
            else:
                result += str(cnt) + temp
        print(result)
        min_num = min(len(result), min_num)
    return min_num

print(solution("abcabcdede"))
