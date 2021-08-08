class Pair {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

let solution = (input) => {
    let dx = [0, 0, 1, -1];
    let dy = [1, -1, 0, 0];
    let [n, m] = input[0].split(" ").map(Number);
    let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number));
    let candidate = [];
    let answer = -1;
    let d = new Array(50).fill(-1).map((v) => new Array(50).fill(-1));

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (a[i][j] === 2) {
				// 차이 1 (연구소 2는 a[i][j] = 0; 이 적혀있음)
                candidate.push(new Pair(i, j));
            };
        };
    };

    function go(index, count) {
        if (index === candidate.length) {
            if (count === m) {
                bfs();
            };
        } else {
            let x = candidate[index].x;
            let y = candidate[index].y;
            a[x][y] = 3; // active
            go(index + 1, count + 1);
            a[x][y] = 2; // 차이 2 remain inactive
            go(index + 1, count);
        };
    };

    function bfs() {
		d = new Array(50).fill(-1).map((v) => new Array(50).fill(-1));
        let q = [];
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (a[i][j] === 3) {
                    q.push(new Pair(i, j));
                    d[i][j] = 0;
                };
            };
        };
        while (q.length !== 0) {
            let pair = q.shift();
            let x = pair.x;
            let y = pair.y;
            for (let k = 0; k < 4; k++) {
                let nx = x + dx[k];
                let ny = y + dy[k];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (a[nx][ny] !== 1 && d[nx][ny] === -1) {
                        d[nx][ny] = d[x][y] + 1;
                        q.push(new Pair(nx, ny));
                    };
                };
            };
        };
        let cur = 0;
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (a[i][j] === 0) { // 차이 3
                    if (d[i][j] === -1) return;
                    if (cur < d[i][j]) {
                        cur = d[i][j];
                    };
                };
            };
        };
        if (answer === -1 || answer > cur) {
			answer = cur;
        };
    };
    go(0, 0);
    return answer;
};
