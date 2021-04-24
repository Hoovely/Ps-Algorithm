# 백준1259_팰린드롬수_문자열_브론즈 1

while 1:
    num = input()

    if num == '0':
        break
    elif num == num[::-1]:
        print("yes")
    else:
        print("no")  