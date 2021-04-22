# 백준2447_별 찍기-10_재귀_실버 1

def draw_star(lst):
    new_star = []
    for i in range(3*len(lst)):
        if i // len(lst) == 1:
            new_star.append(lst[i % len(lst)] + ' ' * len(lst) + lst[i % len(lst)])
        else:
            new_star.append(lst[i % len(lst)] * 3)
    return new_star

star = ['***','* *','***']
n = int(input())
k = 0
while n != 3:
    n /= 3
    k += 1
for i in range(k):
    star = draw_star(star)
for i in star:
    print(i)