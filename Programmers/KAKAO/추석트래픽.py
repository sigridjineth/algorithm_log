import datetime

def solution(lines):
    combined_logs = []
    for log in lines:
        logs = log.split(" ")
        timestamp = datetime.datetime.strptime(logs[0] + " " + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        combined_logs.append((timestamp, -1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))
    combined_logs.sort(key = lambda x: x[0])
    
    accumulated = 0
    max_requests = 1
    
    for (i, element1) in enumerate(combined_logs):
        current = accumulated
        # 1초 미만 윈도우 범위 요청 수 계산
        for element2 in combined_logs[i:]:
            if (element2[0] - element1[0] > 0.999):
                break
            if (element2[1] == 1):
                current += element2[1]
        max_requests = max(max_requests, current)
        accumulated += element1[1]
    
    return max_requests
