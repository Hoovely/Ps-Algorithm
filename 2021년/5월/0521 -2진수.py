# 백준2089_-2진수_수학_실버 4

def mod(n):
    if n == 0:
        result.append(0)
    while n:
        if n % -2:
            result.append(1)
            n = n//-2 + 1
        else:
            result.append(0)
            n //= -2

n = int(input())
result = []
mod(n)
for i in reversed(result):
    print(i, end='')