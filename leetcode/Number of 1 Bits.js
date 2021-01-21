// LEETCODE #191
let hammingWeight = function(n) {
    count = 0
    while (n !== 0) {
        n &= n - 1
        count += 1
    }
    return count
}

let hammingWeight_recursive = function(n, count) {
    if (n === 0) {
        return count
    }
    return hammingWeight((n &= n - 1), (count += 1))
}

input = 00000000000000000000000000001011
console.log(hammingWeight(input, 0))