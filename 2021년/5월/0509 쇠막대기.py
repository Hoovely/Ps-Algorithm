# 백준10799_쇠막대기_스택_실버 3
# 첫번째시도, O(n^2)나와서 시간초과
# 두번째에도 O(n)을 못짜서 시간초과
# 구글링해서 정답찾음, () 이 나올경우 앞에서의 ( 갯수로 count함

S = list(input())

stick = []
result = 0

for i in range(len(S)):
    if S[i] == '(':
        stick.append('(')
    else:
        if S[i-1] == '(': # () 레이저일경우
            stick.pop()
            result += len(stick)
        else: # (   ()   ) 막대기 종료일경우
            stick.pop()
            result += 1

print(result)
