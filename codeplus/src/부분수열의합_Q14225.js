const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

const solution = (input) => {
    let n = Number.parseInt(input[0]);
    let a = input[1].split(" ").map((v) => v.split(" ").map(Number));
    let c = Array(20 * 100000).fill(false);
    // 비트마스크는 집합 내부의 특정한 원소를 사용한다 or 사용하지 않는다의 경우의 수를 총망라한 것이다.
    for (let i = 0; i < (1 << n); i++) {
        let sum = 0;
        // 하나의 bloc이 끝나면, 하나의 경우의 수가 끝나는 것이다!
        for (let j = 0; j < n; j++) {
            if (i & (1 << j)) {
                sum += Number.parseInt(a[j]);
            }
        }
        c[sum] = true;
    }

    let i = 1;

    while (true) {
        if (c[i] == false) {
            break;
        }
        i += 1;
    }

    return i;
}

console.log(solution(input))