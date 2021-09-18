const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

class Pair {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    };
};

let solution = (input) => {
    let [n, m] = input[0].split(" ").map(Number);
    let dx = [0, 0, 1, -1, 1, 1, -1, -1];
    let dy = [1, -1, 0, 0, 1, -1, 1, -1];
    let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number));
    let d = new Array(n).fill(-1).map((v) => new Array(m).fill(-1));
    
    function go(sx, sy) {
        d = new Array(n).fill(-1).map((v) => new Array(m).fill(-1));
        d[sx][sy] = 0;
        let queue = [];
        queue.push(new Pair(sx, sy));
        
        while (queue.length !== 0) {
            let pair = queue.shift();
            let [x, y] = [pair.x, pair.y];
            for (let k = 0; k < 8; k++) {
                let nx = x + dx[k];
                let ny = y + dy[k];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (d[nx][ny] === -1) {
                        if (a[nx][ny] === 1) {
                            return d[x][y] + 1;
                        } else {
                            queue.push(new Pair(nx, ny));
                            d[nx][ny] = d[x][y] + 1;
                        };
                    };
                };
            };
        };
        return false;
    };

    let answer = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (a[i][j] === 0) {
                let dist = go(i, j);
                if (dist !== false) {
                    answer = Math.max(answer, dist);
                };
            };
        };
    };
    return answer;
};

console.log(solution(input))
