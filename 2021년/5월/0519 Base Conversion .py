# 백준11576_Base conversion_수학_실버 5
# a진수 10진수로 변환, 10진수 b진수로 변환

a, b = map(int, input().split())
m = int(input())
nums_a = list(map(int, input().split()))

nums_a.reverse()
num_10 = 0
for i in range(len(nums_a)):  # a진수를 10진수로 변환
    num_10 += nums_a[i]*(a**i)

nums_b = []

while num_10:  # 변환한 10진수를 b진수로 변환
    nums_b.append(num_10 % b)
    num_10 //= b

nums_b.reverse()
print(*nums_b)
