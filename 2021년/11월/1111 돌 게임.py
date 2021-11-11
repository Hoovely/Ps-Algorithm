# 백준_9655_돌 게임_DP_실버 5
# 하드코딩으로 복잡하게 풀었다... 좋은 방법은 아님!

def solution(n):
    if n == 1:
        print("SK")
    elif n == 2:
        print("CY")
    elif n % 3 == 0:
        temp = n//3
        if temp % 2 == 0:
            print("CY")
        else:
            print("SK")
    else:
        cnt = 0
        while n > 3:
            n -= 3
            cnt += 1

        if n == 1:
            if cnt % 2 == 0:
                print("SK")
            else:
                print("CY")
        else:
            if cnt % 2 == 0:
                print("CY")
            else:
                print("SK")


solution(int(input()))
