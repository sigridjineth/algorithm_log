const solution = (input) => {
    let c = Array(101).fill(false).map(x => Array(101).fill(false));
    let dx = [0, -1, 0, 1];
    let dy = [1, 0, -1, 0];

    let n = input[0];
    let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number));
    let ans = 0;

    for (let i = 0; i < n; i++) {
        let [y, x, d, g] = a[i];
        let dirs = curve(d, g);
        c[x][y] = true;

        for (let dir of dirs) {
            x += dx[dir];
            y += dy[dir];
            c[x][y] = true;
        }
    }

    for (let i = 0; i < 100; i++) {
        for (let j = 0; j < 100; j++) {
            if (c[i][j] && c[i][j + 1] && c[i + 1][j] && c[i + 1][j + 1]) {
                ans += 1;
            }
        }
    }

    return ans;
}

const curve = (dir, gen) => {
    let answer = [dir];
    for (let g = 1; g <= gen; g++) {
        let temp = answer.slice().reverse();
        for (let i = 0; i < temp.length; i++) {
            let previous = temp[i];
            temp[i] = (previous + 1) % 4;
        }
        answer.push(...temp);
    }
    return answer;
}

let input = ["3", "3 3 0 1", "4 2 1 3", "4 2 2 1"];

console.log(solution(input));
