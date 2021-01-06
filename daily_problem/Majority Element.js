let majorityElement = function(nums) {
    function count(nums, a) {
        return nums
            .filter((element) => element === a)
            .reduce((acc, cur, idx) => {
                acc += 1
                return acc
            }, 0)
    }
    if (nums.length === 0) return undefined
    if (nums.length === 1) return nums[0]
    let half = Math.floor(nums.length / 2)
    let a = majorityElement(nums.slice(0, half))
    let b = majorityElement(nums.slice(half))
    return [b, a][count(nums, a) > half ? 1 : 0]
};

input = [3,2,3]
console.log(majorityElement(input))