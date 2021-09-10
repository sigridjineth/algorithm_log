def solution(dartResult):
    # 초기 설정.. nums 첫 원소에 0 넣고 돌리는 이유는 일관성 유지하기 위함임...
    nums = [0]
    for s in dartResult:
        if (s == "S"):
            nums[-1] **= 1
            # S, D, T에만 0을 넣어주는 것은 "새로운 숫자의 시작" 이라는 구분자를 넣어주는 것임
            # 그래야 0에서 시작해서 새로운 숫자 들어오면 기존꺼 10 곱해주고 현재꺼 3 넣어줘서 마지막 원소에 숫자 갱신해주는 논리가 통함
            # *, #은 optional이기 때문에 안오면 구분자로 역할 해줄 수가 없음. 어짜피 S든 * 든 둘 중 하나는 역할을 해줘야 하는데 optional한게 아니라 mandatory한 놈을 넣어야 할 것임.
            nums.append(0)
        elif (s == "D"):
            nums[-1] **= 2
            nums.append(0)
        elif (s == "T"):
            nums[-1] **= 3
            nums.append(0)
        elif (s == "*"):
            # 여기가 -2, -3인 이유도 S, D, T가 mandatory 들어갈 때 0을 이미 뒤에 넣고 보기 때문에 그렇슴... len(nums) > 2인 이유도 거기에 있음.. 1이 아니라 2인 이유가 그거임..
            nums[-2] *= 2
            if (len(nums) > 2):
                nums[-3] *= 2
        elif (s == "#"):
            # 이 놈도 마찬가지... S, D, T의 영향임 ㅇㅇ
            nums[-2] *= (-1)
        else: # 자릿수 올림 해줘야 함... 안 그러면 10 들어갈 때 1 따로보고 0 따로보면 정신 나가게 됨ㅎ
            nums[-1] = nums[-1] * 10 + int(s)
    return sum(nums)
