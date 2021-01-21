// LEETCODE #371
let getSum = function(a, b) {
    if ((a & b) === 0) return a ^ b
    while ((a & b) != 0) {
        let temp = (a & b) << 1
        a = (a ^ b)
        b = temp
    }
    return a ^ b
}

let getSum_twoLine = function(a, b) {
    if ((a & b) === 0) return a ^ b
    return getSum_twoLine((a ^ b), ((a & b) << 1))
}