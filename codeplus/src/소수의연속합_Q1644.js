const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

let solution = (input) => {
    let n = parseInt(input)
    let check = Array(n + 1).fill(false);
    let primes = [];
    check.reduce((acc, cur, index, arr) => {
        if (cur || index < 2) {
            return acc;
        };
        let j = index * 2;
        primes.push(index);
        while (j <= n) {
            check[j] = true;
            j += index;
        };
        return acc;
    });
    
    let left = 0;
    let right = 0;
    let sum = primes.length === 0 ? 0 : primes[0];
    let answer = 0;
    
    while (left <= right && right < primes.length) {
        if (sum <= n) {
            if (sum === n) {
                answer += 1;
            }
            right += 1;
            if (right < primes.length) {
                sum += primes[right];
            }
        } else {
            sum -= primes[left];
            left += 1;
        };
    };
    return answer;
};

console.log(solution(input))
