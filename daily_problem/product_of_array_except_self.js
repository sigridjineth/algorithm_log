// 자신을 제외한 배열의 곱 leetcode 238

solution = (nums) => {
    out = []
    p = 1
    
    // 왼쪽 곱셈
    for (let i = 0; i < nums.length; i++) {
        out.push(p)
        p = p * nums[i]
    };

    // 오른쪽 곱셈
    p = 1
    for (let i = nums.length - 1; i > -1; i--) { // i > 0이 아니라 i > -1로 해서 첫 번째 원소(index=0)도 포함시킬 것에 주의함!!
        // 기존 out 변수를 재활용한다면 공간 복잡도 O(1)에 풀이가 가능하다.
        out[i] = out[i] * p
        p = p * nums[i]
    };

    return out
};

nums = [1, 2, 3, 4]
console.log(solution(nums))