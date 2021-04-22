# 백준2798_블랙잭_브루트포스 알고리즘_브론즈 2
# 첫 번째 했던 방법보다 메모리와 시간 줄이는 방법 사용

n, m = map(int, input().split())
num = list(map(int, input().split()))
num_sum = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if num[i] + num[j] + num[k] > m: # num 리스트 중에서 서로 같지 않은 3개의 정수의 합이 m 보다 클 경우 다음 순서 진행
                continue
            else:
                num_sum = max(num_sum, num[i] + num[j] + num[k]) # num 리스트 중에서 서로 같지 않은 3개의 정수의 합이 m보다 크지 않을때 
print(num_sum)