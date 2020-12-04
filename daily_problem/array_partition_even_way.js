// 배열 파티션 LEETCODE #561
// 짝수번째식 풀이

solution = (nums) => {
    let sum = 0
    nums.sort(function(a, b) {
        return a > b ? 1 : -1
    });

    // 짝수번째에 항상 작은 값이 위치한다. 그 이유는 pair 단위이기 때문이다.
    for (let i = 0; i < nums.length; i++) {
        // 짝수번째 합 계산
        if (i % 2 == 0) {
            sum += nums[i];
        };
    };

    return sum;
};