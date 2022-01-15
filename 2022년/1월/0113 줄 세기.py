# 백준_4806_줄 세기_브루트포스_브론즈 2

cnt = 0
while 1:
    try:
        sign = input()
    except:
        break

    if sign == ' ':
        continue
    else:
        cnt += 1
print(cnt)
