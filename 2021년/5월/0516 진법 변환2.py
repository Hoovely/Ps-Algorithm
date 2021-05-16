# 백준11005_진법 변환2_수학_브론즈 1

T = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N,B = map(int, input().split())
result = ''
while N:
    N, mod = divmod(N, B)
    result += T[mod]    
print(result[::-1])