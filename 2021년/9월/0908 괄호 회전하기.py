# 프로그래머스_스택_괄호 회전하기_레벨 2

from collections import deque


def func(arr, n):
    if arr[0] == ']' or arr[0] == '}' or arr[0] == ')':
        return False
    ss = []
    for i in range(n):
        if ss:
            if ss[-1] == '[':
                if arr[i] == ']':
                    ss.pop()
                else:
                    ss.append(arr[i])
            elif ss[-1] == '{':
                if arr[i] == '}':
                    ss.pop()
                else:
                    ss.append(arr[i])
            elif ss[-1] == '(':
                if arr[i] == ')':
                    ss.pop()
                else:
                    ss.append(arr[i])
        else:
            ss.append(arr[i])

    if ss:
        return False
    else:
        return True


def solution(s):
    result = 0
    lst = deque(s)
    for i in range(len(s)):
        if i == 0:
            if func(lst, len(s)):
                result += 1
        else:
            lst.append(lst.popleft())
            if func(lst, len(s)):
                result += 1

    return result


print(solution("[](){}"))
