# 백준1292_쉽게 푸는 문제_수학_실버 5

nums = [0]
for i in range(1, 1001):
    for _ in range(i):
        if len(nums) > 1000:
            break
        nums.append(i)
    if len(nums) > 1000:
        break

a, b = map(int, input().split())

print(sum(nums[a:b+1]))
