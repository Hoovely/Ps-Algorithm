# 프로그래머스_두 개 뽑아서 더하기_정렬_레벨 1

def solution(numbers):
    answer = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            answer.append(numbers[i] + numbers[j])
    result = list(set(answer))
    result.sort()
    return result

nums = list(map(int, input().split()))
print(solution(nums))
