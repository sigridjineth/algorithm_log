// Two Sums using dictionary leetcode #1

twoSums = (nums, target) => {
    nums_map = {}

    for (let i = 0; i < nums.length; i++) {
        // 키와 값을 서로 바꾸어서 dictionary에 저장한다
        nums_map[nums[i]] = i
    };

    for (let i = 0; i < nums.length; i++) {
        let num = nums[i]
        if (nums_map[target_num] != undefined && nums_map[target-num] != i) {
            return [nums.indexOf(num), nums_map[target-num]]
        }
    }
}

twoSums_modified = (nums, target) => {
    nums_map = {}
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i]
        if (nums_map[target-num] != undefined) {
            return [nums_map[target_num], i]
        }
        nums_map[num] = i
    }
}