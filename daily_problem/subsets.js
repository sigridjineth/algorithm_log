// 부분 집합 LEETCODE #78
let subsets = function(nums) {
    let result = [];
    function dfs(index, path) {
        // appending the result every time
        result.push(path)
        // making a path while doing DFS
        for (let i = index; i < nums.length; i++) {
            dfs(i + 1, path.concat(nums[i]));
        };
    };
    dfs(0, []);
    return result
};