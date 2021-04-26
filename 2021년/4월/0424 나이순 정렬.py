# 백준10814_나이순 정렬_정렬_실버 5

n = int(input())
pipple = []
for i in range(n):
    a,b = input().split()
    pipple.append([int(a),str(i)+b])
pipple.sort()
for i in pipple:
    print(i[0], i[1][1:])
    
