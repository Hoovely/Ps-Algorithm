# 백준1436_영화감독 숌_브루트포스 알고리즘_실버 5
# 처음에 문제 이해를 못 해서 좀 알아봄
# 666, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662 ...

n = int(input())
num = 666
n_count = 0
while 1:
    count = 0
    for i in str(num):
        if int(i) == 6:
            count += 1
            if count == 3:
                n_count += 1
        else:
            count = 0
    if n_count == n:
        break
    else:
        num += 1
print(num)