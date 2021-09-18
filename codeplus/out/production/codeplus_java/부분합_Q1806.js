const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

let solution = (input) => {
    let n = parseInt(input[0].split(" ")[0]);
    let s = parseInt(input[0].split(" ")[1]);
    let a = input[1].split(" ").map((v) => parseInt(v));
    let left = 0;
    let right = 0;
    let sum = a[0];
    let ans = n + 1;
    
    while (left <= right && right < n) {
        if (sum < s) {
            right += 1;
            sum += a[right];
        } else if (sum === s) {
            ans = Math.min(right - left + 1, ans);
            right += 1;
            sum += a[right];
        } else if (sum > s) {
            ans = Math.min(right - left + 1, ans);
            sum -= a[left];
            left += 1;
            if (left > right && left < n) {
                right = left;
                sum = a[left];
            };
        };
    };
 
    if (ans > n) {
        ans = 0;
    }
    return ans;
};

console.log(solution(input));
