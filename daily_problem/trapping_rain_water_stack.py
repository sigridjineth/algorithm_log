# Trapping Rain Water leetcode 42 stack solution

def solution(height):
  stack = []
  volume = 0

  for i in range(len(height)):
    # 변곡점을 만나는 경우
    while (len(stack) > 0) and (height[i] > height[stack[-1]]):
      # 스택에서 꺼낸다
      top = stack.pop()

      if (len(stack) == 0):
        break
    
      # 이전과의 차이만큼 물 높이 처리
      distance = i - stack[-1] - 1
      waters = min(height[i], height[stack[-1]]) - height[top]

      volume += distance * waters

    stack.append(i)
  
  return volume

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solution(height))