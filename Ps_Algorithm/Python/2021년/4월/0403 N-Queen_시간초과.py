# 백준9663_N-Queen_백트래킹_골드 5
# 2시간 고민하다가 안돼서 구글링
# 유튜브 코딩랩 강의에서 따온 풀이
# c++ 기반이라 시간초과, 하지만 가지치기 개념 이해함

def go(x,y):

    for i in range(x): # 가지치기
        if x == vx[i]: # 같은 행에 Queen이 있을때
            return 0
        if y == vy[i]: # 같은 열에 Queen이 있을때
            return 0
        if abs(x-vx[i]) == abs(y-vy[i]): # 전에 있던 Queen과의 가로길이와 세로길이가 같을때 즉, 대각선에 있을때
            return 0
    
    if x == n-1: # 가지치기를 뚫고 마지막 행까지 x가 도달했을때
        return 1
    
    vx[x] = x # Queen의 y좌표
    vy[x] = y # Queen의 x좌표

    r = 0
    for i in range(n):
        r += go(x+1,i) # 2번째~n번째 줄까지 바꿔가며 x의 좌표도 for 문으로 계속 이동
    
    return r


n = int(input())
vx = [0]*n
vy = [0]*n
r = 0
for i in range(n):
    r += go(0,i) # 첫 번째 줄의 Queen의 x 좌표를 for문 사용하여 이동

print(r)

