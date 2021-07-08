# 백준_2529_부등호_백트래킹_실버 2
# 이전 풀이에서는 num_str을 다 구해놓고 부등호로 판별하는 방식을 사용하여서 시간초과, 메모리초과가 발생
# 이를 해결하기 위해서 num_str을 넣을때 판별한뒤 부등호를 만족하면 str을 더해주고 만족하지 못하면 다시 재귀함수를 돌리는 방식을 사용

def solve(cnt, num_str):
    global mn,mx
    if cnt == n+1:
        if len(mn) == 0:
            mn = num_str
        else:
            mx = num_str
        return
        
    for i in range(10):
        if visited[i] == 0:
            if cnt == 0 or check(num_str[-1],str(i),lst[cnt-1]): # 올바른 dp 방법
                visited[i] = 1
                solve(cnt+1, num_str+str(i))
                visited[i] = 0

def check(i,j,k):
    if k == '>':
        return i > j
    else:
        return i < j



n = int(input())
lst = list(input().split())
visited = [0]*10
mn, mx = "",""

solve(0,"")

print(mx)
print(mn)
