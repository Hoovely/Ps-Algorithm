# 백준2231_분해합_브루트포스 알고리즘_브론즈 2

n = int(input())
result = 1000000
for i in range(1,n+1):
    num = list(map(int,str(i)))
    num_sum = sum(num)
    if n == i + num_sum:
        print(i)
        break
    elif n == i:
        print(0)
