# 백준_1759_암호 만들기_백트래킹_골드 5

def solve(index, depth, cnt1, cnt2):
    if depth == l and cnt1 >= 1 and cnt2 >= 2:
        for i in result:
            print(i, end='')
        print()
        return

    for i in range(index, c):
        result.append(lst[i])
        if lst[i] in alpha:
            solve(i+1, depth+1, cnt1+1, cnt2)
        else:
            solve(i+1, depth+1, cnt1, cnt2+1)
        result.pop()


l, c = map(int, input().split())
lst = sorted(list(input().split()))
alpha = ['a', 'e', 'i', 'o', 'u']
result = []
solve(0, 0, 0, 0)
