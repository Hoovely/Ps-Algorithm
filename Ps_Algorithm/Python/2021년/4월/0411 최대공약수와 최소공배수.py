# 백준2609_최대공약수와 최소공배수_수학_실버 5

def min_num(n,m):
    i = max(n,m)
    while 1:
        if n % i == 0 and m % i == 0:
            return i
        i -= 1

n,m = map(int,input().split())

print(min_num(n,m))
print(n//min_num(n,m)*m)