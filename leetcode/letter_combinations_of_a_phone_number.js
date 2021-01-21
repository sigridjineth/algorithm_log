let letterCombinations = function(digits) {
    function dfs(index, path) {
        if (digits.length === path.length) {
            result.push(path);
            return;
        };

        for (let i = index; i < digits.length; i++) {
            for (let j of dic[digits[i]]) {
                dfs(i+1, path+j);
            };
        };
    };
    
    if (digits.length === 0 || digits === undefined) {
        return [];
    };

    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    };
    result = [];
    dfs(0, "");

    return result;
};