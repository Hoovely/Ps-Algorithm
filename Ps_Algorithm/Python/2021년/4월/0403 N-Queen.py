# 백준9663_N-Queen_백트래킹_골드 5
# https://rebas.kr/761, https://hellominchan.tistory.com/176 설명 잘 되어있음
# pypy3 으로 제출해야지 시간초과 안나옴

def dfs(i): # i는 바뀌는 행의 값
    global result
    if i == n: # 마지막 행까지 가지치기 뚫고 도착 했을때, +1
        result += 1
        return

    for j in range(n): # j는 바뀌는 열의 값
        if y[j] == 0 and plus[i+j] == 0 and minus[i-j+n-1] == 0:
            # 같은 열에, plus대각선(가로+세로)에, minus대각선에 Queen이 없을때
            y[j] = plus[i+j] = minus[i-j+n-1] = 1 # Queen이 해당좌표에 존재하는 것으로 처리
            dfs(i+1) # 행의 값을 1개 증가 시킴
            y[j] = plus[i+j] = minus[i-j+n-1] = 0 # 열의 값을 바꾸기 전에 Queen 의 좌표를 초기화

n = int(input())
result = 0

y = [0]*n # 같은 열에 Queen이 있는지 확인하는 리스트
plus = [0]*(2*n-1) # plus계수의 대각선에 Queen이 있는지 확인하는 리스트, NxN 리스트에서 대각선의 개수는 2n-1개
minus = [0]*(2*n-1) # minus계수의 대각선에 Queen이 있는지 확인하는 리스트

dfs(0)
print(result)