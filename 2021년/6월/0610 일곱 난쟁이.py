# 백준2309_일곱 난쟁이_브루트 포스_브론즈 2

def brute():
    for i in range(9):
        for j in range(i+1, 9):
            if men_sum - men[i] - men[j] == 100:
                men.pop(i)
                men.pop(j-1)
                men.sort()
                return


men = []
for _ in range(9):
    men.append(int(input()))
men_sum = sum(men)

brute()

for i in men:
    print(i)