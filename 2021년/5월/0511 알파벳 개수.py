# 백준10808_알파벳 개수_문자열_브론즈 2

S = list(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    print(S.count(i), end=' ')
