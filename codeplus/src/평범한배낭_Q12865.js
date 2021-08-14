let solution = (input) => {
    let [n, k] = input[0].split(" ").map(Number);
    let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number));
    let w = a.reduce((acc, cur, idx, arr) => {
        acc.push(cur[0]);
        return acc;
    }, [0]);
    let v = a.reduce((acc, cur, idx, arr) => {
        acc.push(cur[1]);
        return acc;
    }, [0]);
    let d = new Array(n + 1).fill(0).map((v) => new Array(k + 1).fill(0));
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= k; j++) {
            d[i][j] = d[i - 1][j];  
            if (j - w[i] >= 0) {
                d[i][j] = Math.max(d[i - 1][j], d[i - 1][j - w[i]] + v[i]);
            }
        };
    };
    return d[n][k];
};

console.log(solution(input))
