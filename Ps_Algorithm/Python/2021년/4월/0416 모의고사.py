# 프로그래머스_모의고사_브루트포스_레벨 1 
# 첫 번째 시도에서 성공 테스트 5개, 실패 테스트 9개 나옴
# 곰곰히 코드 씹어가며 생각하다가, k의 값을 1작게 넣어놓아서 answers의 길이가 길게나오면 값이 잘못나오는걸 확인
# 두 번째 시도때 성공!

numbers = [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 
            [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5], 
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
answers = [1,3,2,4,2]

def solution(answers, numbers):
    answer = []
    solution_sum = 0
    i = 0
    j = 0
    k = 0
    while 1:
        if j == 3:
            break

        if answers[i] == numbers[j][k]:
            solution_sum += 1
        i += 1
        k += 1

        if (j == 0 and k == 10) or (j == 1 and k == 16) or (j == 2 and k == 20):
            k = 0

        if i == len(answers):
            answer.append(solution_sum)
            j += 1
            k = 0
            i = 0
            solution_sum = 0

        
    
    answer_max = max(answer)
    index = []

    for i in range(3):
        if answer_max == answer[i]:
            index.append(i+1)
    
    return index

print(solution(answers, numbers))        



