# 백준_11899_괄호 끼워넣기_스택_실버 4

lst = input()
stack = []
for i in range(len(lst)):
    if lst[i] == ')':
        if len(stack) == 0:
            stack.append(')')
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    else:
        stack.append('(')

print(len(stack))