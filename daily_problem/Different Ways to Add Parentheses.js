// LEETCODE 241
let diffWaysToCompute = (input) => {
    if (Number.isInteger(input)) return parseInt(input)
    const res = input.split("").reduce((acc, cur, idx) => {
        let op = ['+', '-', '*']
        if (op.includes(cur)) {
            let leftHalf = diffWaysToCompute(input.substring(0, idx))
            let rightHalf = diffWaysToCompute(input.substring(idx + 1))
            leftHalf.forEach((x) => {
                rightHalf.forEach((y) => {
                    if (cur === op[0]) acc.push(x + y)
                    else if (cur === op[1]) acc.push(x - y)
                    else if (cur === op[2]) acc.push(x * y)
                })
            })
        }
        return acc
    }, [])
    if (res.length==0) res.push(parseInt(input));
    return res
}

console.log(diffWaysToCompute("2-1-1"))
