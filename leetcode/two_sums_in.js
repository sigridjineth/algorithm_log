// Two Sums leetcode 1
// using element-in search

twoSum = (nums, target) => {
    for (let i = 0; i < nums.length; i++) {
        complement = target - nums[i]
    }
    if (nums.slice(i+1).includes(complement)) {
        return [nums.indexOf(nums[i]), nums.slice(i+1).indexOf(complement) + (i+1)]
    }
}