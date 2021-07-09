# 백준_2529_부등호_백트래킹_실버 2
# 오답 1

def solve(depth ,num_str):
    global num_max
    global num_min
    if depth == n+1:
        if len(num_min) == 0:
            num_min = num_str
        else:
            num_max = num_str
        return

    for i in range(10):
        if visited[i] == 0:
            if depth == 0 or check(num_str[-1], str(i), lst[depth-1]):
                visited[i] = 1
                solve(depth+1, num_str + str(i))
                visited[i] = 0

def check(num_str0,num_str1,sign):
    if sign == '>':
        return num_str0 > num_str1
    elif sign == '<':
        return num_str0 < num_str1


n = int(input())
lst = list(input().split())
visited = [0]*10
num_max = ""
num_min = ""

solve(0,"")

print(num_max)
print(num_min)