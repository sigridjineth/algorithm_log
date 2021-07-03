// const input = require("fs")
// 	.readFileSync("/dev/stdin")
// 	.toString()
// 	.trim()
// 	.split("\n");

let min = Number.MAX_SAFE_INTEGER;
let max = Number.MIN_SAFE_INTEGER;

const solution = (input) => {
    let n = input[0];
    let a = input[1].split(" ").map(Number);
    let [plus, minus, mul, div] = input[2].split(" ").map(Number);
    cal(a, 1, a[0], plus, minus, mul, div);
    // 자바스크립트에서는 +0, -0이 나올 수 있으므로 추가 처리
    return [max ? max : 0, min ? min : 0];
}

const cal = (a, index, cur, plus, minus, mul, div) => {
    if (index === a.length) {
        max = Math.max(max, cur);
        min = Math.min(min, cur);
        return;
    }
    if (plus > 0) {
        cal(a, index + 1, cur + a[index], plus - 1, minus, mul, div);
    }
    if (minus > 0) {
        cal(a, index + 1, cur - a[index], plus, minus - 1, mul, div);
    }
    if (mul > 0) {
        cal(a, index + 1, cur * a[index], plus, minus, mul - 1, div);
    }
    if (div > 0) {
        // 자바스크립트에서는 음수를 양수로 나눌 때 C++14 기준을 따르지 않는다.
        const result = cur >= 0 ? Math.floor(cur / a[index]) : -Math.floor(-cur / a[index]);
        cal(a, index + 1, result, plus, minus, mul, div - 1);
    }
}

let input = ["6", "1 2 3 4 5 6", "2 1 1 1"];
let input2 = ["3", "3 4 5", "1 0 1 0"];

console.log(solution(input));
