# 백준10799_쇠막대기_스택_실버 3
# 오답 1

lst = list(input())
stack = []
result = 0
for i in range(len(lst)):
    if lst[i] == '(':
        stack.append('(')    
    elif lst[i] == ')' and lst[i-1] == '(':
        stack.pop()
        result += len(stack)
    else:
        result += 1
        stack.pop()
print(result)