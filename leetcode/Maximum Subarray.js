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

maxSubArray_Kadanes = (nums) => {
    let best_sum = Number.MIN_SAFE_INTEGER
    let current_sum = 0
    nums.forEach((element) => {
        current_sum = Math.max(...[element, current_sum + element])
        best_sum = Math.max(...[best_sum, current_sum])
    })
    return best_sum
}

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
console.log(maxSubArray(nums))