# 백준1904_01타일_DP_실버 3
# 피보나치수열의 점화식과 동일

n = int(input())
a,b = 1,2
for i in range(n-2):
    a,b = b, (a+b)%15746

if n == 1:
    print(1)
else:
    print(b)
