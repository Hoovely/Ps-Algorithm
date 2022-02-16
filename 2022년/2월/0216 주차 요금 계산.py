# 프로그래머스_주차 요금 계산_카카오_레벨 2

from math import ceil


def solution(fees, records):
    answer = []

    MaxTime = 23*60 + 59
    CarsInfor = [-1]*10001
    for record in records:
        Time = int(record[:2])*60 + int(record[3:5])
        Num = int(record[6:10])
        isInOut = record[11:]

        if CarsInfor[Num] == -1:
            CarsInfor[Num] = 0
        if isInOut == 'IN':
            CarsInfor[Num] += MaxTime - Time
        if isInOut == 'OUT':
            CarsInfor[Num] -= MaxTime - Time

    for Time in CarsInfor:
        if Time == -1:
            continue

        if Time > fees[0]:
            TakeMoney = fees[1] + ceil((Time-fees[0])/fees[2])*fees[3]
            answer.append(TakeMoney)
        else:
            answer.append(fees[1])

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
