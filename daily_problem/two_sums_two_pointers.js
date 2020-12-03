// Two Sums using two pointers, leetcode #1

twoSums = (nums, target) => {
    left = 0, right = nums.length - 1

    while (!left==right) {
        // 합이 타겟보다 크면 오른쪽에서 왼쪽으로
        if (nums[left] + nums[right] < target) {
            left += 1
        } else if (nums[left] + nums[right] > target) {
            right -= 1
        } else {
            return [left, right]
        }
    }
}