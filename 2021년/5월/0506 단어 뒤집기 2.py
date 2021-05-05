# 백준17413_단어 뒤집기 2_문자열_실버 3
# 1시간 넘게 잡고있다가, 안풀려서 구글링
# flag를 설정해서, <가 나오면 flag true로 해서 정상입력 >로 닫히면 다시 false로 반대로 입력
# word = word + i ==> 정상입력, word = i + word ==> 반대로 입력

import sys

input = sys.stdin.readline

S = list(input().strip())
flag = 0
word = ''
result = ''
for i in S:
    if flag == 0: # 반대로 입력
        if i == '<':
            flag = 1
            word = word + i
        elif i == ' ':
            word = word + i
            result = result + word
            word = ''
        else:
            word = i + word # ab // word = 'a' + '' , word = 'b' + 'a' ==> ba
    else: # 정상 입력
        word = word + i
        if i == '>':
            flag = 0
            result = result + word
            word = ''

print(result+word)