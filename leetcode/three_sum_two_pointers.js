// 세 수의 합 LEETCODE #35
// 투 포인터를 이용하여 풀이한다

threeSum = (nums) => {
    results = [];
    nums.sort(function(a, b) {
        return a > b ? 1 : -1
    });
    for (let i = 0; i < nums.length; i++) {
        // 중복된 값 건너뛰기
        if (i > 0 && nums[i] == nums[i-1]) {
            continue;
        };
    };
    // 간격을 좁혀가며 합을 계산
    left = i + 1, right = nums.length - 1;
    while (left < right) {
        sum = nums[i] + nums[left] + nums[right];
        if (sum < 0) {
            left += 1
        } else if (sum > 0) {
            right -= 1
        } else {
            // sum = 0인 경우로 정답으로 처리한다
            results.push([nums[i], nums[left], nums[right]]);
            // 좌우로 동일한 값이 있을 경우 스킵한다
            while (left < right && nums[left] == nums[left+1]) {
                left += 1
            };
            while (left < right && nums[right] == nums[right-1]) {
                right -= 1
            };
            left += 1
            right -= 1
        };
    };

    return results;
};