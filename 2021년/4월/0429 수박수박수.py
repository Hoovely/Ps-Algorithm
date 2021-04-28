# 프로그래머스_소수 찾기_문자열_레벨 1

n = int(input())

def solution(n):
    if n % 2 == 0: # 짝수인경우
        return "수박"*(n//2) 
    else: # 홀수인경우
        return "수박"*(n//2) + "수"

print(solution(n))
