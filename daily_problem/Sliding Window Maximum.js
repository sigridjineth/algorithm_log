maxSlidingWindow_bruteForce = (nums, k) => {
    if (!nums) {
        return nums
    }
    let result = []
    for (let i = 0; i < nums.length - k + 1; i++) {
        result.push(Math.max(...nums.slice(i, i+k)))
    }
    return result
}

// 큐를 이용한 풀이
let maxSlidingWindow = function(nums, k) {
    let result = []
    let window = []
    let current_max = Number.MAX_SAFE_INTEGER
    for (let num of nums.entries()) {
        let i = num[0]
        let v = num[1]
        window.push(v)
        // if not even 1 cycle done
        if (i < k - 1) {
            continue
        }
        // 새로이 추가된 값이 기존 최댓값보다 클 경우 교체
        if (current_max === Number.MAX_SAFE_INTEGER) {
            current_max = Math.max(...window)
        } else if (v > current_max) {
            current_max = v
        }
        result.push(current_max)
        if (current_max === window.shift()) {
            current_max = Number.MAX_SAFE_INTEGER
        }
    }
    return result
};