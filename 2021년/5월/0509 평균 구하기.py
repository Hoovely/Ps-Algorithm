# 프로그래머스_평균 구하기_수학_레벨 1

arr = [1,2,3,4]

def solution(arr):
    result = 0
    for i in arr:
        result += i
    return result / len(arr)

print(solution(arr))