// 배열 파티션 I LEETCODE #561
// 오름차순 풀이

solution = (nums) => {
    let sum = 0
    let pair = []
    nums.sort(function(a, b) {
        return a > b ? 1 : -1
    });

    for (let n of nums) {
        // 앞에서부터 오름차순으로 페어를 만들어서 총합을 계산한다
        pair.push(n);
        if (pair.length == 2) {
            sum += Math.min(...pair);
            pair = [] // 페어 초기화
        };
    };

    return sum;
}