# 백준2447_별 찍기-10_재귀_실버 1
# 진짜 절대 못 풀 것 같아서 구글링..
# 이해하는데 2시간 걸림;
# 오답 3번 쓰기

def draw_star(n):
    map = []
    for i in range(3 * len(n)): # n 만큼 반복
        if i // len(n) == 1: # i 가 (len(n) ~ 2 * len(n) - 1) 일떄 까지
            map.append(n[i % len(n)] + ' ' * len(n) + n[i % len(n)]) 
        else:
            map.append(n[i % len(n)] * 3) # i 가 len(n)-1 까지는 n[i]*3 출력
    return(list(map))

star = ['***', '* *', '***']
n = int(input())
k = 0
while n != 3: # k = log3(n)-1 을 만드는 while 문
    n = int(n / 3)
    k += 1
for i in range(k): 
# n이 9 이상일때 부터 실행, 첫번째 실행일때 초기 star을 재귀해서 다음과 같이 나옴
# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********
# 2번 이상 반복시 위의 패턴을 재귀해서 똑같이 323 으로 나옴
    star = draw_star(star)
for i in star: # n == 3 즉 k == 0 이면 star을 바로 출력, 그 이상일때 재귀해서 얻은 star의 값을 출력
    print(i)