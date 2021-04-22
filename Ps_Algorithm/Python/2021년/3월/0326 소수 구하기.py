# 백준1929_소수 구하기_수학_실버 2
# 에라토스테네스의 체 풀고나서 푸니까 30분 컷

m,n = map(int, input().split())
nums = [0 for _ in range(n+1)] 
prime = []
for i in range(2, n+1): # n 까지의 소수를 구해놓는 코드
    if nums[i] == 1:
        continue
    else:
        prime.append(i)
    for j in range(i, n+1, i):
        nums[j] = 1

for j in prime:
    if j >= m: # n 까지의 소수 중 m 보다 큰 소수값만 출력함 
        print(j)

