// LEETCODE #198
let rob = function(nums) {
    function _rob(i) {
        if (i < 0) return 0
        return Math.max(...[_rob(i - 1), _rob(i - 2) + nums[i]])
    }
    return _rob(nums.length - 1)
}

let rob_dynamic = function(nums) {
    if (nums.length === 0) return 0
    if (nums.length <= 2) return Math.max(...nums)
    const sums = nums.reduce((arr, cur, idx) => {
        if (idx === 0) {
            arr[0] = nums[0]
            return arr
        }
        if (idx === 1) {
            arr[1] = Math.max(...[nums[0], nums[1]])
            return arr
        } else {
            arr[idx] = Math.max(...[arr[idx - 1], arr[idx - 2] + cur])
            return arr
        }
    }, {})
    return sums[Object.keys(sums).length-1]
}

console.log(rob_dynamic([0,0]))