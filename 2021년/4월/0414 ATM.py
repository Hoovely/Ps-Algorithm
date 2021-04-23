# 백준11399_ATM_그리디 알고리즘_실버 3

n = int(input())

people = list(map(int,input().split()))
people.sort()

time_sum = 0
result = 0

for i in people:
    time_sum += i
    result += time_sum
    
print(result) 