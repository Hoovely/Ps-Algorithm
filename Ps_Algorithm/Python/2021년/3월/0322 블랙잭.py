# 백준2798_블랙잭_브루트포스 알고리즘_브론즈 2
# n의 최댓값이 100이라서 O(n^3)이지만 시간초과 안뜸

n,m = map(int, input().split())
num = list(map(int, input().split()))
sum = []
for i in num:
    for j in num:
        for k in num:
            if i != j and i != k and j != k and i+j+k <= m: # num 리스트 중에서 서로 같지 않은 3개의 정수의 합이 m보다 크지않을때
                sum.append(i+j+k)
print(max(sum)) # sum 리스트 중에서 가장 큰 값을 출력

