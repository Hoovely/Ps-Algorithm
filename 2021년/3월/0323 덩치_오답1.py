# 백준7568_덩치_브루트포스 알고리즘_실버 5

n = int(input())
big = []
rank = []
for i in range(n):
    big.append(list(map(int, input().split())))
for i in range(n):
    count = 0
    for j in range(n):
        if big[i][0] < big[j][0] and big[i][1] < big[j][1]:
            count += 1
    rank.append(count)

for i in rank:
    print(i+1, end = ' ')