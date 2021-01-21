class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # exception process
        if not nums:
            return -1
        # 최솟값을 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while (left < right):
            mid = (left + right) // 2
            if (nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid
        pivot = left
        # 피벗 기준 이진 탐색
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            mid_pivot = (mid + pivot) % len(nums)
            if (nums[mid_pivot] < target):
                left = mid + 1
            elif (nums[mid_pivot] > target):
                right = mid - 1
            else:
                return mid_pivot
        return -1