# 백준_9012_괄호_스택_실버 4

for _ in range(int(input())):
    lst = input()
    flag = 0
    stack = []
    for i in range(len(lst)):
        if lst[i] == ')':
            if len(stack) == 0:
                flag = 1
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag = 1
                    break
        else:
            stack.append('(')
    if flag or len(stack):
        print('NO')
    else:
        print('YES')