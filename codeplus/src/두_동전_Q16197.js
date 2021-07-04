let dx = [0, 0, 1, -1];
let dy = [1, -1, 0, 0];
let a;

const go = (step, x1, y1, x2, y2, n, m) => {
    if (step === 11) {
        return -1
    }
    let first_coin_fall = false;
    let second_coin_fall = false;
    if (x1 < 0 || x1 >= n || y1 < 0 || y1 >= m) {
        first_coin_fall = true;
    }
    if (x2 < 0 || x2 >= n || y2 < 0 || y2 >= m) {
        second_coin_fall = true;
    }
    if (first_coin_fall === true && second_coin_fall === true) {
        return -1
    }
    if (first_coin_fall === true || second_coin_fall === true) {
        return step;
    }
    let answer = -1;
    for (let k = 0; k < 4; k++) {
        let nx1 = x1 + dx[k];
        let ny1 = y1 + dy[k];
        let nx2 = x2 + dx[k];
        let ny2 = y2 + dy[k];
        
        if (0 <= nx1 && nx1 < n && 0 <= ny1 && ny1 < m && a[nx1][ny1] === '#') {
            nx1 = x1;
            ny1 = y1;
        }

        if (0 <= nx2 && nx2 < n && 0 <= ny2 && ny2 < m && a[nx2][ny2] === '#') {
            nx2 = x2;
            ny2 = y2;
        }

        let temp = go(step + 1, nx1, ny1, nx2, ny2, n, m);
        if (temp === -1) {
            continue;
        }
        if (answer === -1 || answer > temp) {
            a[x1][y1] = ".";
            a[x2][y2] = ".";
            a[nx1][ny1] = "o";
            a[nx2][ny2] = "o";
            answer = temp;
        }
    }
    return answer;
}

const solution = (input) => {
    let [n, m] = input[0].split(" ").map(Number);
    let x1 = -1;
    let y1 = -1;
    let x2 = -1;
    let y2 = -1;
    a = input.slice(1, n + 1).map((v) => v.split(""));
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (a[i][j] === 'o') {
                if (x1 === -1) {
                    x1 = i;
                    y1 = j;
                } else {
                    x2 = i;
                    y2 = j;
                }
                // a[i][j] = '.';
            }
        }
    }
    return go(0, x1, y1, x2, y2, n, m);
}

let input = ["6 2", ".#", ".#", ".#", "o#", "o#", "##"];
let input2 = ["5 3", "###", ".o.", "###", ".o.", "###"];
console.log(solution(input2));
