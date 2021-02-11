def solution(n, t, m, timetable):
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()
    current = 540 # 60 * 9
    for _ in range(n): # 셔틀운행횟수 n
        for _ in range(m): # 최대승객수 m
            # 대기가 있는 경우 1초 전 도착
            if (timetable and timetable[0] <= current):
                candidate = timetable.pop(0) - 1
            else: # 대기가 없는 경우 정시 도착
                candidate = current
        current += t
    h, m = divmod(candidate, 60) # 몫과 나머지 divmod
    return str(h).zfill(2) + ':' + str(m).zfill(2)

solution(1, 1, 5, "[08:00, 08:01, 08:02, 08:03]")