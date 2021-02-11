def solution(dartResult):
    nums = [0]
    
    for s in dartResult:
        if not (s.isnumeric()):
            if s == 'S':
                nums[-1] **= 1
                nums.append(0)
            elif s == 'D':
                nums[-1] **= 2
                nums.append(0)
            elif s == 'T':
                nums[-1] **= 3
                nums.append(0)
            elif s == '*':
                # 이전 값과 그 이전 값 모두 두 배 처리할 것
                if (len(nums) == 2):
                    nums[-2] *= 2
                elif (len(nums) > 2):
                    nums[-2] *= 2
                    nums[-3] *= 2
            elif s == '#':
                nums[-2] *= -1
        else:
            # 자릿수 올림
            nums[-1] = nums[-1] * 10 + int(s)
    return sum(nums)

print(solution("1S*2T*3S"))