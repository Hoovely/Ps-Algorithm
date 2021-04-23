# 백준9663_N-Queen_백트래킹_골드 5
# 오답3 2021-04-05

def queen(i):
    global result
    if n == i:
        result += 1
        return

    for j in range(n):
        if y[j] == 0 and plus[i+j] == 0 and minus[i-j+n-1] == 0:
            y[j] = plus[i+j] = minus[i-j+n-1] = 1
            queen(i+1)
            y[j] = plus[i+j] = minus[i-j+n-1] = 0

n = int(input())

result = 0
y = [0]*n
plus = [0]*(2*n-1)
minus = [0]*(2*n-1)

queen(0)

print(result)