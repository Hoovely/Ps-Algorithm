# 프로그래머스_튜플_문자열_레벨 2

def solution(s):
    nums = []
    num_str = ''
    for i in s:
        if i == '{' or i == '}' or i == ",":
            if num_str != '':
                nums.append(int(num_str))
                num_str = ''
        else:
            num_str += i 
    result = []
    nums_count = []
    numbers = set(nums)
    for i in numbers:
        nums_count.append([nums.count(i), i])

    nums_count.sort(reverse=True)
    for i in nums_count:
        result.append(i[1])
    return result

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
