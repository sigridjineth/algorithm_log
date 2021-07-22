let n;
let check;
let dist;
let a;

let solution = (input) => {
    n = parseInt(input[0]);
    check = new Array(n + 1).fill(-1);
    dist = new Array(n + 1).fill(0);
    a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number))
                    .reduce((acc, cur, idx, arr) => {
                        if (!acc[cur[0]]) {
                            acc[cur[0]] = new Array();
                        };
                        if (!acc[cur[1]]) {
                            acc[cur[1]] = new Array();
                        };
                        acc[cur[0]].push(cur[1]);
                        acc[cur[1]].push(cur[0]);
                        return acc;
                    }, new Array());
    go(1, -1);
    let q = [];
    for (let i = 1; i < n + 1; i++) {
        if (check[i] === 2) {
            dist[i] = 0;
            q.push(i);
        } else {
            dist[i] = -1;
        };
    };
    while (q.length !== 0) {
        let x = q.shift();
        for (let y of a[x]) {
            if (dist[y] === -1) {
                q.push(y);
                dist[y] = dist[x] + 1;
            };
        };
    };
    return dist.slice(1, n + 1).join(" ");
};

function go(x, p) {
    if (check[x] === 1) {
        return x;
    };
    check[x] = 1;
    for (let y of a[x]) {
        if (p === y) {
            continue;
        };
        let res = go(y, x);
        if (res === -2) {
            return -2;
        };
        if (res >= 0) {
            check[x] = 2;
            if (x === res) {
                return -2;
            } else {
                return res;
            };
        };
    };
    return -1;
};

let input = ["6", "1 2", "3 4", "6 4", "2 3", "1 3","3 5"];
solution(input);