# 백준_6609_모기곱셈_수학_브론즈 3

while 1:
    try:
        m,p,l,e,r,s,n = map(int,input().split())
    except:
        break
    for i in range(n):
        temp = m*e
        m = p//s
        p = l//r
        l = temp
    print(m)