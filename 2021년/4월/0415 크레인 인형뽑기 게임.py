# 프로그래머스_크레인 인형뽑기 게임_스택_레벨 1
# 첫 번째 시도에서 stack에 인형을 다 담고 같은 인형들을 한번에 제거하는 방법 사용했으나, 런타임 에러
# 두 번째 시도에서 stack에 인형을 하나 담을때 마다 앞뒤로 같은 인형들을 제거하는 방법 사용해서 성공!

def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                stack.append(board[j][i-1])
                board[j][i-1] = 0    
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 1
    
    return answer*2

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
moves = list(map(int,input().split()))

print(solution(board, moves))

