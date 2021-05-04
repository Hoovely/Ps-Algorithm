# 백준1874_스택 수열_스택_실버 3

import sys    
                
n = int(input())
nums = []
result = []
count = 1
flag = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while num >= count:
        nums.append(count)
        count += 1
        result.append('+')
    if nums[-1] == num:
        nums.pop()
        result.append('-')
    else:
        flag = 0
    
if flag == 0:
    print("NO")
else:
    for i in result:
        print(i)



