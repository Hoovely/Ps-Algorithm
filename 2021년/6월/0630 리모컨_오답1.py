# 백준_1107_리모컨_브루트포스_골드 5
# 오답 1

n = int(input())
m = int(input())
broken = [str(i) for i in range(10)]
if m != 0:
    for num in list(input().split()):
        broken.remove(num)

result = abs(100-n)
for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if num[i] not in broken:
            break
        elif i == len(num) - 1:
            result = min(result, abs(n-int(num)) + len(num))
print(result)
