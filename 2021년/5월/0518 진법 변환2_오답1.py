# 백준11005_진법 변환2_구현_브론즈 1
# 오답1

n, b = map(int, input().split())
string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
while n:
    result += string[n % b]
    n //= b
print(result[::-1])
