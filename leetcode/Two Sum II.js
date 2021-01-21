// LEETCODE 167 Two Sum II
twoSum_twoPointers = (nums, target) => {
    let left = 0
    let right = nums.length - 1
    while (left !== right) {
        if (nums[left] + nums[right] > target) {
            right -= 1
        } else if (nums[left] + nums[right] < target) {
            left -= 1
        } else {
            return [left + 1, right + 1]
        }
    }
    return -1
}

twoSums_binarySearch = (nums, target) => {
    for (let element of nums.entries()) {
        let k = element[0]
        let v = element[1]
        let left = k + 1
        let right = nums.length - 1
        let expected = target - v
        while (left <= right) {
            let mid = Math.floor((left + right) / 2)
            if (nums[mid] < expected) {
                left = mid + 1
            } else if (nums[mid] > expected) {
                right = mid - 1
            } else {
                return [k + 1, mid + 1];
            }
        }
    }
}