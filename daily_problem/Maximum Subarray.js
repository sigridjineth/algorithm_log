// LEETCODE #53
maxSubArray = (nums) => {
    return Math.max(...nums.reduce((arr, cur, idx) => {
        if (idx === 0) {
            arr.push(cur)
            return arr
        }
        let sum = cur
        if (arr[idx - 1] > 0) {
            sum += arr[idx - 1]
            arr.push(sum)
            return arr
        }
        arr.push(sum)
        return arr
    }, []))
}

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
console.log(maxSubArray(nums))