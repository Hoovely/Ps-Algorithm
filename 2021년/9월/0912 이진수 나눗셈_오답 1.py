# 백준_22950_이진수 나눗셈_수학_브론즈 1
# 오답 1

n = int(input())
m = input()
k = int(input())

if k == 0:
    print("YES")
    exit(0)

if '1' not in m:
    print("YES")
    exit(0)

cnt = 0
for i in range(n-1, -1, -1):
    if m[i] == '0':
        cnt += 1
    else:
        break
if cnt >= k:
    print("YES")
else:
    print("NO")
