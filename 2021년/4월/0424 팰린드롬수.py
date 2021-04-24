# 백준1259_팰린드롬수_문자열_브론즈 1
# 진짜 시간없어서 대충 생각해서 구현한 버젼

while 1:
    num = int(input())
    if num == 0:
        break
    else:
        if num < 10:
            print("yes")
        elif num < 100:
            if num // 10 == num % 10:
                print("yes")
            else:
                print("no")
        elif num < 1000:
            if num // 100 == num % 10:
                print("yes")
            else:
                print("no")
        elif num < 10000:
            if (num // 1000 == num % 10) and ((num % 1000) // 100 == (num % 100) // 10):
                print("yes")
            else:
                print("no")
        elif num < 100000:
            if (num // 10000 == num % 10) and ((num % 10000) // 1000 == (num % 100) // 10):
                print("yes")
            else:
                print("no")