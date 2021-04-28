# 프로그래머스_소수 찾기_수학_레벨 1
# 에라토스테네스의 체 사용

n = int(input())

def solution(n):
    nums = [1]*(n+1)
    nums[0],nums[1] = 0,0
    for i in range(2, n+1):
        if i^2 <= n and nums[i]:
            for j in range(2, n+1):
                if i*j <= n:
                    nums[i*j] = 0
                else:
                    break
    return print(nums.count(1))

solution(n)
