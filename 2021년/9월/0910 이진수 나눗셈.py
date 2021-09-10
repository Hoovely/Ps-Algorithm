# 백준_22950_이진수 나눗셈_수학_브론즈 1

n = int(input())
m = input()
k = int(input())

if '1' not in m:
    print("YES")
    exit(0)

if k == 0:
    print("YES")
    exit(0)

cnt = 0
for i in range(len(m)-1, -1, -1):
    if m[i] == '1':
        break
    else:
        cnt += 1

if cnt >= k:
    print("YES")
else:
    print("NO")
