// 조합의 합 LEETCODE #39
let combinationSum = function(candidates, target) {
    let result = [];
    function dfs(csum, index, path) {
        // ending condition
        if (csum < 0) {
            return;
        };
        if (csum == 0) {
            result.push(path);
        };
        // List a reflexive call from one to the lower element.
        for (let i = index; i < candidates.length; i++) {
            dfs(csum - candidates[i], i, path.concat(candidates[i]));
        };
    };
    dfs(target, 0, []);
    return result;
};