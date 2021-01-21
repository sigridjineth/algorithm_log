// 구간 병합 LEETCODE #56
// 정렬하여 병합
let merge = function(intervals) {
    let merged = []
    intervals.sort((a,b) => a[0]-b[0]);
    for (let i of intervals) {
        let lastIndex = merged.length - 1
        if (merged.length > 0 && i[0] <= merged[lastIndex][1]) {
            merged[lastIndex][1] = Math.max(...[merged[lastIndex][1], i[1]]);
        } else {
            merged.push(i);
        };
    };
    return merged;
};

console.log(merge([[1,3], [2,6], [8,10], [15,18]]));