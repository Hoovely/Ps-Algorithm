# 백준7568_덩치_브루트포스 알고리즘_실버 5
# 혼자 40분동안 풀어보려고 했으나, 생각이 안 떠올라서 힌트를 봤다.
# '자기보다 덩치 큰(kg >, cm >) 사람이 몇 명인지 count 해서 자기 등수만 정하면 된다' 라는 글귀를 보고 다시 풀었다.

N = int(input())
man = []
result = []
for _ in range(N):
    man.append(list(map(int, input().split())))
for i in range(N):
    count = 0
    for j in range(N):
        if man[i][0] < man[j][0] and man[i][1] < man[j][1]:  
            count += 1
    result.append(count+1)
for i in range(N):
    print(result[i], end = " ")


