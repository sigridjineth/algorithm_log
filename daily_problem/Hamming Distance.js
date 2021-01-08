// LEETCODE #461
let hammingDistance = function(x, y) {
    return (x^y).toString(2)
                .split("")
                .filter((element) => element === '1')
                .reduce((arr) => {
                    arr += 1
                    return arr
                }, 0)
};