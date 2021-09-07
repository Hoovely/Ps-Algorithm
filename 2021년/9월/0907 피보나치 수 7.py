# 백준_15624_피보나치 수 7_DP_실버 3

n = int(input())
fibo = [0, 1] + [0]*(n-1)
for i in range(2, n+1):
    fibo[i] = (fibo[i-2] + fibo[i-1]) % 1000000007

print(fibo[n])
