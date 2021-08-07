class Pair {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

let solution = (input) => {
    let d = new Array(50).fill(0).map((v) => new Array(50).fill(0));
    let room = new Array(50*50).fill(-1);
    let dx = [0, -1, 0, 1];
    let dy = [-1, 0, 1, 0];

    let [m, n] = input[0].split(" ").map(Number);
    let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number));
    let rooms = 0;
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            // at starting point, d is initalized as zero. by doing bfs, d would be updated after it executes.
            if (d[i][j] === 0) {
                rooms += 1;
                room[rooms] = bfs(i, j, rooms);
            }
        }
    }

    function bfs(sx, sy, rooms) {
        let q = [];
        q.push(new Pair(sx, sy));
        d[sx][sy] = rooms;
        let cnt = 0;

        while (q.length !== 0) {
            let pair = q.shift();
            let [x, y] = [pair.x, pair.y];
            cnt += 1;

            for (let k = 0; k < 4; k++) {
                let nx = x + dx[k];
                let ny = y + dy[k];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }
                if (d[nx][ny] !== 0) {
                    continue;
                }
                if ((a[x][y] & (1 << k)) > 0) {
                    continue;
                }
                q.push(new Pair(nx, ny));
                d[nx][ny] = rooms;
            }
        }

        return cnt;
    }

    let answer = "";

    answer = rooms + "\n";

    let temp_2 = 0;
    for (let i = 1; i < rooms; i++) {
        temp_2 = Math.max(temp_2, room[i]);
    }

    answer = answer + temp_2 + "\n";

    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            let x = i;
            let y = j;
            let s = 0;
            for (let k = 0; k < 4; k++) {
                let nx = x + dx[k];
                let ny = y + dy[k];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }
                if (d[nx][ny] === d[x][y]) {
                    continue;
                }
                if (((a[x][y] & (1 << k)) > 0) && s === 0) {
                    if (ans < room[d[x][y]]+room[d[nx][ny]]) {
                        ans = room[d[x][y]]+room[d[nx][ny]];
                        s += 1;
                    }
                }
            }
        }
    }

    answer = answer + ans;
    return answer;
}

let input = ["7 4", "11 6 11 6 3 10 6", "7 9 6 13 5 15 5", "1 10 12 7 13 7 5", "13 11 10 8 10 12 13"];
console.log(solution(input));
