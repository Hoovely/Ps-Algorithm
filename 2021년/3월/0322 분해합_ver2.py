# 백준2231_분해합_브루트포스 알고리즘_브론즈 2

n = int(input())
for i in range(1, n+1):
    sum = 0
    b = i
    while b>0:
        a = b % 10
        b = b // 10
        sum += a
    if i + sum == n: 
        print(i)
        break
    elif i == n:
        print(0)