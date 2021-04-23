# 백준11047_동전 0_그리디 알고리즘_실버 2

n, k = map(int,input().split())
money = []
lst_count = []
for i in range(n):
    money.append(int(input()))

while k != 0:
    count = 0
    num = money.pop()
    if k // num:
        count = k // num
        k %= num
    lst_count.append(count)

print(sum(lst_count))