let n = 9;
let BLANK = 0;

const solution = (input) => {
    let a = input.slice(0, n).map((v) => v.split(" ").map(Number));
    let c = Array(3).fill(false).map((x) => Array(n).fill(false).map((x) => Array(10).fill(false)))
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (a[i][j] !== BLANK) {
                c[0][i][a[i][j]] = true;
                c[1][j][a[i][j]] = true;
                c[2][square(i, j)][a[i][j]] = true;
            }
        }
    }
    go(a, c, 0);
}

const square = (x, y) => {
    return (parseInt(x / 3)) * 3 + (parseInt(y / 3));
}

const go = (a, c, z) => {
    if (z === 81) {
        for (let i = 0; i < n; i++) {
            let output = [];
            for (let j = 0; j < n; j++) {
                output.push(a[i][j]);
            }
            console.log(output.join(" "));
        }
        return true;
    }
    let x = parseInt(z / n);
    let y = z % n;
    let square_number = square(x, y);
    if (a[x][y] !== 0) {
        return go(a, c, z + 1); // backtracking
    } else if (a[x][y] === 0) {
        for (let i = 1; i <= 9; i++) {
            if (!c[0][x][i] && !c[1][y][i] && !c[2][square_number][i]) {
                c[0][x][i] = true;
                c[1][y][i] = true;
                c[2][square_number][i] = true;
                a[x][y] = i;
                if (go(a, c, z + 1)) {
                    return true; // backtracking
                }
                a[x][y] = 0;
                c[0][x][i] = false;
                c[1][y][i] = false;
                c[2][square_number][i] = false;
            }
        }
    }
    return false;
}

let input = ["0 3 5 4 6 9 2 7 8", "7 8 2 1 0 5 6 0 9", "0 6 0 2 7 8 1 3 5", "3 2 1 0 4 6 8 9 7", "8 0 4 9 1 3 5 0 6", "5 9 6 8 2 0 4 1 3", "9 1 7 6 5 2 0 8 0", "6 0 3 7 0 1 9 5 2", "2 5 8 3 9 4 7 6 0"];

solution(input)