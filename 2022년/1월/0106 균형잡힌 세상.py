# 백준_4949_균형잡힌 세상_스택_실버 4

while 1:
    st = input()
    if st == '.':
        break
    stack = []
    flag = 0
    for ch in st:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')' or ch == ']':
            if len(stack) == 0:
                flag = 1
                break
            temp = stack[-1]
            if ch == ')' and temp == '(': stack.pop()
            elif ch == ']' and temp == '[': stack.pop()
            elif ch == ')' and temp == '[': flag = 1
            elif ch == ']' and temp == '(': flag = 1
        if flag: break
    if len(stack) == 0 and flag == 0:
        print('yes')
    else:
        print('no')