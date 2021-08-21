# 백준_1247_부호_수학_브론즈 3

for _ in range(3):
    n = int(input())
    sum = 0
    for _ in range(n):
        sum += int(input())
    if sum == 0:
        print('0')
    elif sum > 0:
        print('+')
    else:
        print('-')
