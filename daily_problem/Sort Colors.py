class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        # 중간점인 1을 기준으로 판단하도록 하자.
        while (white < blue):
            if (nums[white] < 1):
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1 # 일단 같이 움직여준다.
            elif (nums[white] > 1):
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else: # (nums[white] == 1) 정상인 경우니까 white 인덱스를 1 증가시킨다.
                white += 1