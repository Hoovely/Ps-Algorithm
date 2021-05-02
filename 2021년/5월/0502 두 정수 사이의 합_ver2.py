# 프로그래머스_두 정수 사이의 합_수학_레벨 1
# 시간복잡도 최소화한 풀이방법

def solution(a,b):
    if a == b:
        return a
    elif a > b:
        return (a*(a+1)//2) - (b*(b-1)//2)
    elif a < b:
        return (b*(b+1)//2) - (a*(a-1)//2)
        
a,b = map(int, input().split())
print(solution(a,b))