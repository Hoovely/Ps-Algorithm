# 백준11656_접미사 배열_문자열_실버 4

S = input()
lst = []
for i in range(len(S)):
    lst.append(S[i:])
for i in sorted(lst):
    print(i)