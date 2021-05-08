s = "one4seveneight"


def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']
    for num in numbers:
        if num in s:
            if num == 'one':
                s = s.replace('one', '1')
            elif num == 'two':
                s = s.replace('two', '2')
            elif num == 'three':
                s = s.replace('three', '3')
            elif num == 'four':
                s = s.replace('four', '4')
            elif num == 'five':
                s = s.replace('five', '5')
            elif num == 'six':
                s = s.replace('six', '6')
            elif num == 'seven':
                s = s.replace('seven', '7')
            elif num == 'eight':
                s = s.replace('eight', '8')
            elif num == 'nine':
                s = s.replace('nine', '9')
            else:
                s = s.replace('zero', '0')
    return s


print(solution(s))
