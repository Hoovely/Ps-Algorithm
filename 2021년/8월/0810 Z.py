# 백준_1074_Z_분할 정복_실버 1

def Z(m, size):
    global cnt, r, c
    if m == 1:
        if r == 0 and c == 0:
            print(cnt)
        elif r == 0 and c == 1:
            print(cnt+1)
        elif r == 1 and c == 0:
            print(cnt+2)
        elif r == 1 and c == 1:
            print(cnt+3)
        return
    else:
        if r < size and c < size:
            pass
        elif r < size and c >= size:
            c -= size
            cnt += 4**(m-1)
        elif r >= size and c < size:
            r -= size
            cnt += 4**(m-1)*2
        elif r >= size and c >= size:
            r -= size
            c -= size
            cnt += 4**(m-1)*3
        Z(m-1, size//2)


n, r, c = map(int, input().split())
cnt = 0
Z(n, 2**(n-1))
