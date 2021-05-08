cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]


def solution(n, k, cmd):
    nums = []
    cancel = []
    result = []
    L = []
    answer = ''
    for i in range(n):
        nums.append([str(i), 'O'])
        # result.append('O')

    for i in range(n-k-1):
        L.append(nums.pop())

    for i in cmd:
        if i[0] == 'U':
            for _ in range(int(i[2:])):
                if len(nums) == 0:
                    break
                L.append(nums.pop())

        elif i[0] == 'D':
            for _ in range(int(i[2:])):
                if len(L) == 0:
                    break
                nums.append(L.pop())

        elif i == 'C':
            if len(nums) == 0:
                continue
            nums[-1][1] = 'X'
            cancel.append(int(nums[-1][0]))

        elif i == 'Z':
            if len(cancel) == 0:
                continue
            a = cancel[-1]
            b = int(nums[-1][0])
            if a > b:
                for _ in range(a-b):
                    if len(L) == 0:
                        break
                    nums.append(L.pop())
                nums[cancel.pop()][1] = 'O'
                for _ in range(a-b):
                    L.append(nums.pop())
            else:
                nums[cancel.pop()][1] = 'O'

    for i in range(len(L)):
        nums.append(L.pop())

    for i in nums:
        answer += i[1]

    return answer


print(solution(8, 2, cmd))
