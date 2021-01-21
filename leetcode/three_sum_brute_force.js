// 세 수의 합 LEETCODE 3SUM
// 브루트 포스 계산

threeSum = (nums) => {
    results = []
    nums.sort(function(a, b) {
        return a > b ? 1 : -1;
    });
    // 브루트 포스 N^3 반복
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i-1]) {
            continue
        };
        for (let j = i + 1; j < nums.length - 1; j++) {
            if (j > i + 1 && nums[j] == nums[j-1]) {
                continue
            };
            for (let k = j + 1; k < nums.length; k++) {
                if (k > j + 1 && nums[k] == nums[k-1]) {
                    continue
                };
                if (nums[i] + nums[j] + nums[k] == 0) {
                    results.push([nums[i], nums[j], nums[k]]);
                };
            };
        };
    };
    
    return results;
};