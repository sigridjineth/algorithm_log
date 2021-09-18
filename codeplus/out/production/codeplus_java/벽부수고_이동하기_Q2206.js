const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

class Pair {
    constructor(x, y, z) {
        this.x = x;
        this.y = y;
        this.z = z;
    };
};

let solution = (input) => {
    let dx = [1, -1, 0, 0];
    let dy = [0, 0, 1, -1];
    let [n, m] = input[0].split(" ").map((v) => Number(v));
    let dist = new Array(n).fill(0).map((v) => new Array(m).fill(0).map((v) => new Array(2).fill(0)));
    let a = input.slice(1, n + 1).map((v) => v.split("").map(Number));
    dist[0][0][0] = 1; // n - 1을 정답으로 만든다. 시작하는 칸도 센다.
    let queue = [];
    queue.push(new Pair(0, 0, 0));
    while (queue.length !== 0) {
        let pair = queue.shift();
        let x = pair.x;
        let y = pair.y;
        let z = pair.z;
        for (let k = 0; k < 4; k++) {
            let nx = x + dx[k];
            let ny = y + dy[k];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            };
            if (a[nx][ny] === 0 && dist[nx][ny][z] === 0) {
                // 빈 칸일 때, 지나가고자 하는 부분을 업데이트 하지 않았다면
                dist[nx][ny][z] = dist[x][y][z] + 1;
                queue.push(new Pair(nx, ny, z));
            };
            if (z === 0 && a[nx][ny] === 1 && dist[nx][ny][1] === 0) {
                dist[nx][ny][1] = dist[x][y][z] + 1;
                queue.push(new Pair(nx, ny, z + 1));
            };
        };
    };
    
    let candidates = Math.min(dist[n - 1][m - 1].filter((candidate) => candidate > 0));
    return candidates > 0 ? candidates : -1;
};

console.log(solution(input));
