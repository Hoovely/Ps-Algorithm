# 백준_13116_30번_트리_실버 4

for _ in range(int(input())):
    a, b = map(int, input().split())
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
    print(a*10)