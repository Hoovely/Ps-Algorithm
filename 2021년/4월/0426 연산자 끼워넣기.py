# 백준14888_연산자 끼워넣기_백트래킹_실버 1
# 모르겠다.. 걍

n = int(input())
nums = list(map(int,input().split()))
operators = list(map(int, input().split()))
result = nums[0]
for i in range(n-1):
    result = result 연산자 nums[i+1]
