# 백준_10826_피보나치 수 4_DP_실버 4

n = int(input())
fibo = [0, 1] + [0]*(n-1)
for i in range(2, n+1):
    fibo[i] = fibo[i-2] + fibo[i-1]

print(fibo[n])
