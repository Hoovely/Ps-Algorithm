# 백준_1248_맞춰봐_백트래킹_골드 3

def check(index):
    sum = 0
    for i in range(index,-1,-1):
        sum += nums[i]
        if s[i][index] == 0 and sum != 0:
            return False
        elif s[i][index] == 1 and sum <= 0:
            return False
        elif s[i][index] == -1 and sum >= 0:
            return False
    return True
        

def solve(index):
    if index == n:
        return True
    
    if s[index][index] == 0:
        nums[index] = 0
        return check(index) and solve(index+1)

    for i in range(1,11):
        nums[index] = s[index][index] * i
        if check(index) and solve(index+1):
            return True
    
    return False

        
n = int(input())
lst = list(input())
s = [[0]*n for i in range(n)]
nums = [0]*n

for i in range(n):
    for j in range(i,n):
        temp = lst.pop(0)
        if temp == '+':
            s[i][j] = 1
        elif temp == '-':
            s[i][j] = -1
        elif temp == '0':
            s[i][j] = 0 

solve(0)

print(*nums)

