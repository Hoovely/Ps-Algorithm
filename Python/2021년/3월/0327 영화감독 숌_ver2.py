# 백준1436_영화감독 숌_브루트포스 알고리즘_실버 5
# 처음에 in 을 반대로 써서 사용 못 했던 방법
# 시간 : 972ms

n = int(input())
num = 666
count = 0
while n != count:
    if '666' in str(num):
        count += 1
    num += 1
print(num-1)