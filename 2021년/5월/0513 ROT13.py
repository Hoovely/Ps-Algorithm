# 백준11655_ROT13_문자열_브론즈 1

S = list(input())
for i in range(len(S)):
    if S[i].isupper():
        s = ord(S[i]) + 13
        if s > 90:
            s = s - 26
        S[i] = chr(s)
    elif S[i].islower():
        s = ord(S[i]) + 13
        if s > 122:
            s = s - 26
        S[i] = chr(s)

for i in S:
    print(i,end='')