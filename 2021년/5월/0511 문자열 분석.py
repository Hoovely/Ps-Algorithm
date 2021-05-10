# 백준10820_문자열 분석_문자열_브론즈 2

while 1:
    try:
        lower_count = 0
        upper_count = 0
        num_count = 0
        else_count = 0

        
        S = list(input())
        for i in S:
            if i.isupper():
                upper_count += 1
            elif i.islower():
                lower_count += 1
            elif i == ' ':
                else_count += 1
            else:
                num_count += 1
        print(lower_count, upper_count, num_count, else_count)
    except EOFError:
        break