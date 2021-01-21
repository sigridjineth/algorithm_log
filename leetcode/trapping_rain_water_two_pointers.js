// Trapping Rain Water LEETCODE 42
// 투 포인터를 이용한 풀이

solution = (height) => {
    if (height.length == 0) {
        return 0;
    }
    let volume = 0;
    let left = 0;
    let right = height.length - 1;
    let left_max = height[left]
    let right_max = height[right]

    while (left < right) {
        left_max = Math.max(height[left], left_max)
        right_max = Math.max(height[right], right_max)

        // 더 높은 쪽을 향해 투 포인터 이용
        if (left_max <= right_max) {
            volume += left_max - height[left]
            left += 1
        } else {
            volume += right_max - height[right]
            right -= 1
        }
    }

    return volume
}

height = [0,1,0,2,1,0,1,3,2,1,2,1]
console.log(solution(height))