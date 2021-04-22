# 백준2960_에라토스테네스의 체_수학_실버 4
# 잘 모르겠어서 유튜브, 구글링 해봄...

def era(n, k):
    nums = [0 for _ in range(n+1)]
    prime = []
    count = 0
    for i in range(2, n+1):
        if nums[i] == 1: # 합성수일때
            continue
        else:
            prime.append(i)
        for j in range(i, n+1, i):
            if nums[j] == 1: # 6, 12 같은 애들 잡아내는용
                continue
            nums[j] = 1
            count += 1
            if count == k:
                return j

n, k = map(int, input().split())
print(era(n, k))