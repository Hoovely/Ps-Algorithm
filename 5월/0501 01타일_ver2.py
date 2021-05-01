# 백준1904_01타일_DP_실버 3
# 같은 것이 있는 순열로 풀었으나, 시간초과

import math

def dp(n):
    result = 0
    if n < 3:
        return n
    
    if n % 2 == 0:
        for i in range(n//2+1):
            if i == 0:
                result += 1
            elif i == n//2:
                result += 1
            else:
                result += math.factorial(n-i) // (math.factorial(i) * math.factorial(n-2*i))
    else:
        for i in range(n//2+1):
            if i == 0:
                result += 1
            else:
                result += math.factorial(n-i) // (math.factorial(i) * math.factorial(n-2*i))
    return result%15746

n = int(input())
print(dp(n))