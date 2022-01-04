# 백준_1918_후위 표기식_스택_골드 3

def precedence(ch):
    if ch == '(' or ch == ')': return 0
    elif ch == '+' or ch == '-': return 1
    elif ch == '*' or ch == '/': return 2
    else: return -1

lst = input()
stack = []
result = ''
for i in lst:
    if i == '(':
        stack.append(i)
    elif i == ')':
        while stack:
            temp = stack.pop()
            if temp == '(': break
            else:
                result += temp
    elif i in '+-*/':
        while stack:
            temp = stack[-1]
            if precedence(i) <= precedence(temp):
                result += stack.pop()
            else: break
        stack.append(i)
    else:
        result += i
while stack:
    result += stack.pop()

print(result)