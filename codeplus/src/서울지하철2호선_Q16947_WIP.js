let solution = (input) => {
    let n = input[0];
    let check = new Array(n + 1).fill(-1);
    let dist = new Array(n + 1).fill(-1);
    let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number))
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
    function go(x, p) {
        if (check[x] === 1) {
            return x;
        };
        check[x] = 1;
        if (!a[x]) {
            return -1;
        };
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
    go(0, -1);
    let q = [];
    for (let i = 0; i < n; i++) {
        if (check[i] === 2) {
            dist[i] = 0;
            q.push(i);
        } else {
            dist[i] = -1;
        };
    };
    while (!q.length === 0) {
        let x = q.shift();
        for (let y of a[x]) {
            if (dist[y] === -1) {
                q.push(y);
                dist[y] = dist[x] + 1;
            };
        };
    };
    for (let i = 0; i < n; i++) {
        console.log(dist[i] + " ");
    };
};
