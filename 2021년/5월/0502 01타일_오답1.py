# 백준1904_01타일_DP_실버 3
# 오답 1

n = int(input())
nums = [1,2]
for i in range(2, n):
    nums.append((nums[i-2] + nums[i-1]) % 15746)
if n == 1:
    print(nums[0])
else:
    print(nums[-1])