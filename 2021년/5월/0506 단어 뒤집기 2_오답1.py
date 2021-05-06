# 백준17413_단어 뒤집기 2_문자열_실버 3

import sys

input = sys.stdin.readline

S = list(input().strip())
tag = 0
word = ''
result = ''

for i in S:
    if tag == 0:
        if i == '<':
            tag = 1
            word = word + i
        elif i == ' ':
            word = word + i
            result = result + word
            word = ''
        else:
            word = i + word

    else:
        word = word + i
        if i == '>':
            tag = 0
            result = result + word
            word = ''
print(result+word)
