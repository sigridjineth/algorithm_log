case = int(input()) #test case 수를 입력함
result = []

for i in range(case):
    n, m = map(int, input().split(" "))
    element = list(map(int, input().split(" ")))
    diction = list()
    sequence = 0
    for j in range(0, len(element)): #1단계: index 별로 중요도와 함께 분류하여 딕셔너리 형태로 넣기
        elementdic = {'index': j, 'priority': element[j]} #원래 index: 중요도입니다.
        diction.append(elementdic)
    while len(diction) > 1: #2단계: diction에 있는 요소가 모두 출력되기 전까지
        now = diction[-1] #항상 queue의 마지막 끝을 출력하므로, 해당 요소를 now라고 합니다.
        prev = diction[-2]
        if now['priority'] >= prev['priority']: #현재 queue에서 맨 끝에 있는 요소가 바로 앞에 있는 요소보다 중요도가 높다면
            printedValue = diction.pop() #이를 출력합니다.
            sequence += 1 #순서를 1씩 높입니다.
            print("출력되었습니다.")
            if printedValue == m:
                result.append(sequence)
                print("결과입니다.")
                exit(0)
        elif now['priority'] < prev['priority']:
            print("중요도가 조정되었습니다.")
            diction.insert(0, now) #아니라면 해당 요소를 리스트의 맨 앞에 넣고
            diction.pop() #맨 끝에 있는 요소를 제거합니다.
            continue
    if len(diction) == 1:
        diction.pop()
        sequence += 1
        result.append(sequence)

print(result)