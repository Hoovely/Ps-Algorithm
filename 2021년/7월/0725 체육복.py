# 프로그래머스_체육복_그리디_레벨 1

def solution(n, lost, reserve):
    student = [0] + [1] * n
    for i in reserve:
        student[i] = 2
    for i in lost:
        student[i] -= 1

    for i in range(1, n+1):
        if i == 1:
            if student[1] == 2 and student[2] == 0:
                student[1] = 1
                student[2] = 1
        elif i == n:
            if student[n] == 2 and student[n-1] == 0:
                student[n] = 1
                student[n-1] = 1
        else:
            if student[i] == 2:
                if student[i-1] == 0:
                    student[i] = 1
                    student[i-1] = 1
                elif student[i+1] == 0:
                    student[i] = 1
                    student[i+1] = 1

    return student.count(1) + student.count(2)


print(solution(5, [2, 4], [3]))
