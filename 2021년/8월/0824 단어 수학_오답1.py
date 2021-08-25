# 백준_1339_단어 수학_그리디_골드 4
# 오답 1

n = int(input())
lst = []
for _ in range(n):
    lst.append(input())

alphabet = [0 for _ in range(26)]

for i in range(n):
    j = 0
    while j != len(lst[i]):
        alphabet[ord(lst[i][-j-1])-ord('A')] += pow(10, j)
        j += 1

alphabet.sort(reverse=True)
result = 0
for i in range(9, 0, -1):
    result += alphabet[9-i]*i

print(result)
