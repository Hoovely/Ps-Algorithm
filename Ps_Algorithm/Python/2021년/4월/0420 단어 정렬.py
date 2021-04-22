# 백준1181_단어 정렬_문자열_실버 5
# 1. 문자열의 길이 순으로 정렬 ==> sort(key=len)
# 2. 길이가 같으면 사전 순으로 ==> 문자열을 sort한번 해주면 알파벳 순서로 정렬됨
# 3. 중복된 단어 처리 ==> set으로 한번 처리해주고 다시 list화 해주면됨
# 3 -> 2 -> 1 순서로 진행

import sys

n = int(sys.stdin.readline())
str_list = []
for i in range(n):
    str_list.append(input())
str_list = list(set(str_list))
str_list.sort()
str_list.sort(key=len) 
for i in str_list:
    print(i)

