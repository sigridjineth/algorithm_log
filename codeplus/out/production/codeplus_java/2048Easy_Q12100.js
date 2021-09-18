const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

let LIMIT = 5;

let gen = (k) => {
    return Array.from({length: 10}, (x, index) => {
        let current = (k & 3);
        k >>= 2;
        return current;
    });
};

let check = (a, dirs) => {
    let n = a.length;
    let d = a.slice();
    let merged;
    // 0: down, 1: up, 2: left, 3: right
    for (let dir of dirs) {
        let ok;
        merged = Array(a.length).fill(false).map((v) => Array(a.length).fill(false));
        while (true) {
            ok = false;
            if (dir === 0) {
                for (let i = n - 2; i >= 0; i--) {
                    for (let j = 0; j < n; j++) {
                        if (d[i][j] === 0) {
                            continue;
                        } else if (d[i + 1][j] === 0) {
                            d[i + 1][j] = d[i][j];
                            merged[i + 1][j] = merged[i][j];
                            d[i][j] = 0;
                            ok = true;
                        } else if (d[i + 1][j] === d[i][j]) {
                            if (merged[i][j] === false && merged[i + 1][j] === false) {
                                d[i + 1][j] *= 2;
                                merged[i + 1][j] = true;
                                d[i][j] = 0;
                                ok = true;
                            };
                        };
                    };
                };
            } else if (dir === 1) {
                for (let i = 1; i < n; i++) {
                    for (let j = 0; j < n; j++) {
                        if (d[i][j] === 0) {
                            continue;
                        } else if (d[i - 1][j] === 0) {
                            d[i - 1][j] = d[i][j];
                            merged[i - 1][j] = merged[i][j];
                            d[i][j] = 0;
                            ok = true;
                        } else if (d[i - 1][j] === d[i][j]) {
                            if (merged[i][j] === false && merged[i - 1][j] === false) {
                                d[i - 1][j] *= 2;
                                merged[i - 1][j] = true;
                                d[i][j] = 0;
                                ok = true;
                            };
                        };
                    };
                };
            } else if (dir === 2) {
                for (let j = 1; j < n; j++) {
                    for (let i = 0; i < n; i++) {
                        if (d[i][j] === 0) {
                            continue;
                        } else if (d[i][j - 1] === 0) {
                            d[i][j - 1] = d[i][j];
                            merged[i][j - 1] = merged[i][j];
                            d[i][j] = 0;
                            ok = true;
                        } else if (d[i][j - 1] === d[i][j]) {
                            if (merged[i][j - 1] === false && merged[i][j - 1] === false) {
                                d[i][j - 1] *= 2;
                                merged[i][j - 1] = true;
                                d[i][j] = 0;
                                ok = true;
                            };
                        };
                    };
                };
            } else if (dir === 3) {
                for (let j = n - 2; j >= 0; j--) {
                    for (let i = 0; i < n; i++) {
                        if (d[i][j] === 0) {
                            continue;
                        } else if (d[i][j + 1] === 0) {
                            d[i][j + 1] = d[i][j];
                            merged[i][j + 1] = merged[i][j];
                            d[i][j] = 0;
                            ok = true;
                        } else if (d[i][j + 1] === d[i][j]) {
                            if (merged[i][j] === false && merged[i][j + 1] === false) {
                                d[i][j + 1] *= 2;
                                merged[i][j + 1] = true;
                                d[i][j] = 0;
                                ok = true;
                            };
                        };
                    };
                };    
            };
            if (ok === false) {
                break;
            };
        };
    };
    let answer = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (answer < d[i][j]) {
                answer = d[i][j];
            };
        };
    };
    return answer;
};

let solution = (input) => {
    let n = parseInt(input[0]);
    let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number));
    let ans = 0;
    for (let k = 0; k < (1 << (LIMIT * 2)); k++) {
        let dirs = gen(k);
        let cur = check(a, dirs);
        if (ans < cur) ans = cur;
    };
    return ans;
};

console.log(solution(input))
