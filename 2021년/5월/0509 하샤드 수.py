# 프로그래머스_하샤드 수_수학_레벨 1

def solution(x):
    num_sum = 0
    for num in str(x):
        num_sum += int(num)
    
    if x % num_sum == 0:
        return True
    else:
        return False

print(solution(10))