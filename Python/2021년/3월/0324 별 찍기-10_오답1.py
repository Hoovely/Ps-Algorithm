# 백준2447_별 찍기-10_재귀, 분할 정복_실버 1

def draw_star(lst):
    map = []
    for i in range(3*len(lst)):
        if i // len(lst) == 1:
            map.append(lst[i % len(lst)] + ' ' * len(lst) + lst[i % len(lst)])
        else:
            map.append(lst[i % len(lst)]*3)
    return list(map)
n = int(input())
star = ['***', '* *', '***']
k = 0
while n != 3:
    n /= 3
    k += 1
for i in range(k):
    star = draw_star(star)
for i in star:
    print(i)