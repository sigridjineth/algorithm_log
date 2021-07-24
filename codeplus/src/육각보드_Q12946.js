const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

let solution = (input) => {
    let n = parseInt(input[0]);
    let a = input.slice(1, n + 1).map((v) => v.split(""));
    let color = new Array(50).fill(-1).map((v) => new Array(50).fill(-1));
    let dx = [-1, -1, 0, 0, 1, 1];
    let dy = [0, 1, -1, 1, -1, 0];
    let ans = 0;
    
    function dfs(x, y, c) {
        color[x][y] = c;
        ans = Math.max(ans, 1);
        
        for (let k = 0; k < 6; k++) {
            let nx = x + dx[k];
            let ny = y + dy[k];
            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                if (a[nx][ny] === 'X') {
                    if (color[nx][ny] === -1) {
                        dfs(nx, ny, 1 - c);
                        ans = Math.max(ans, 2);
                    } else if (color[nx][ny] === c) {
                        ans = Math.max(ans, 3);
                        return;
                    };
                };
            };
        };
    };
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (a[i][j] === 'X' && color[i][j] === -1) {
                // 색칠해야 하지만 아직 안한 경우이다
                dfs(i, j, 0);
            };
        };
    };
    
    return ans;
};

console.log(solution(input))
