# 백준_1248_맞춰봐_백트래킹_골드 3

def solve(depth,num):
    if depth == n:

    
    if depth == 0:
        if s[0] == '+':
            nums.append()        
        elif s[0] == '-':
        
        elif s[0] == '0':

    for i in range(-10,10,1):
        if check(i,depth,num)
            nums.append(i)
            solve(depth+1,num)
            nums.pop()

def check(depth, i):
    if depth = 0:

    sum = 0
    for k in range(depth+1+num):
        sum += nums[k]



    for i in range(n):
        sum = 0
        for j in range(i,n):
            if i == j:
                if nums[i] > 0:
                    if s[] == '+':
                        return True
                    else:
                        return False

                elif nums[i] < 0:
                    if s[] == '-':
                        return True
                    else:
                        return False

                elif nums[i] == 0:
                    if s[] == '0':
                        return True
                    else:
                        return False
                continue

            sum += nums[i] + nums[j]
            if sum > 0:
                if s[] == '+':
                    return True
                else:
                    return False

            elif sum < 0:
                if s[] == '-':
                    return True
                else:
                    return False

            elif sum == 0:
                if s[] == '0':
                    return True
                else:
                    return False



n = int(input())
lst = list(input())
s = []
num_list = 0

for i in range(n,0,-1):
    s.append(lst[num_list:num_list+i])
    num_list += i

nums = []

solve(0,num)