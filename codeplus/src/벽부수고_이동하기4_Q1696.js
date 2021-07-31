const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

class Pair {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    };
};

let solution = (input) => {
    let dx = [0, 0, 1, -1];
    let dy = [1, -1, 0, 0];
    let group_size = [];
    
    function bfs(sx, sy) {
        let g = group_size.length; // the higher number assigned as getting into the array earlier
        let queue = [];
        queue.push(new Pair(sx, sy));
        check[sx][sy] = true;
        group[sx][sy] = g; // gth in the group
        let cnt = 1; // newly added group size
        while (queue.length !== 0) {
            let pair = queue.shift();
            let [x, y] = [pair.x, pair.y];
            for (let k = 0; k < 4; k++) {
                let nx = x + dx[k];
                let ny = y + dy[k];
                if (0 <= nx && nx < n && 0 <= y && ny < m) {
                    if (a[nx][ny] === 0 && check[nx][ny] === false) {
                        queue.push(new Pair(nx, ny));
                        check[nx][ny] = true;
                        group[nx][ny] = g;
                        cnt += 1;
                    };
                };
            };
        };
        group_size.push(cnt); // introduce new group to the group_size!
    };
    
    let [n, m] = input[0].split(" ").map((v) => Number(v));
    let check = new Array(n).fill(false).map((v) => new Array(m).fill(false));
    let group = new Array(n).fill(-1).map((v) => new Array(m).fill(-1));
    let a = input.slice(1, n + 1).map((v) => v.split("").map(Number));
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (a[i][j] === 0 && check[i][j] === false) {
                // BFS로 flood exercise
                bfs(i, j);
            };
        };
    };
    
    let ans = "";
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (a[i][j] === 0) {
                ans += "0";
            } else {
                let near = new Set();
                for (let k = 0; k < 4; k++) {
                    let x = i + dx[k];
                    let y = j + dy[k];
                    if (0 <= x && x < n && 0 <= y && y < m) {
                        if (a[x][y] === 0) {
                            near.add(group[x][y]);
                        };
                    };
                };
                let current_size = 1;
                for (let g of near) {
                    current_size += group_size[g];
                };
                ans += (current_size % 10).toString();
            };
        };
        ans += '\n';
    };
    
    return ans;
};

console.log(solution(input))
