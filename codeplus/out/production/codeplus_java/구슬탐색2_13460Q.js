let dx = [0, 0, 1, -1];
let dy = [1, -1, 0, 0];
const LIMIT = 10;

let gen = (k) => {
    return Array.from({length: 10}, (x, index) => {
        let current = (k & 3);
        k >>= 2;
        return current;
    });
};

class Result {
    constructor(moved, hole, x, y) {
        this.moved = moved;
        this.hole = hole;
        this.x = x;
        this.y = y;
    };
};

let check = (a, dir) => {
    let n = a.length;
    let m = a[0].length;
    
    let hx = 0;
    let hy = 0;
    let rx = 0;
    let ry = 0;
    let bx = 0;
    let by = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (a[i][j] == 'O') {
                hx = i;
                hy = j;
            } else if (a[i][j] == 'R') {
                rx = i;
                ry = j;
            } else if (a[i][j] == 'B') {
                bx = i;
                by = j;
            }
        }
    }

    let count = 0;
    for (let k of dir) {
        count += 1;
        // 빨간 구슬이 구멍에 빠졌는가?
        let hole1 = false;
        // 파란 구슬이 구멍에 빠졌는가?
        let hole2 = false;

        while (true) {
            // 코드상으로는 빨간 구슬을 먼저 굴리고 파란 구슬을 굴린다.
            // 구슬이 RB 순서로 정렬해있을 경우에는 문제가 없다.
            // 그러나 BR 순서로 정렬해있을 경우에는 빨간 구슬을 먼저 굴리는데 파란구슬에 막혀 (움직이지 않음, 구멍에 빠지지 않음)
            // 을 리턴한다.
            // 그래서 어떤 순서에 의해 구슬을 굴리지 못하는 경우가 발생하지 않도록 무한 루프를 이용하여
            // 다음 방향으로 전환을 해야할때에만 루프를 빠져나올 수 있게 한다. 

            // 빨간 구슬을 k 방향으로 이동시켜본다
            let p1 = simulate(a, k, rx, ry);
            // 파란 구슬을 k 방향으로 이동시켜본다
            // simulate 함수는 1) 이동하는가 2) 구멍에 빠졌는가 를 체크한다
            let p2 = simulate(a, k, bx, by);
            rx = p1.x;
            ry = p1.y;
            bx = p2.x;
            by = p2.y;

            // 두 구슬이 다 이동하지 않을 때까지 반복한다
            if (p1.moved === false && p2.moved === false) {
                break;
            }

            // 구멍에 빠졌으면 hole1, hole2를 업데이트 해준다
            if (p1.hole) hole1 = true;
            if (p2.hole) hole2 = true;
        }

        if (hole2) return 987654321;
        if (hole1) return count;
    }
    return -1;
}

let valid = (dir) => {
    let l = dir.length;
    for (let i = 0; i + 1 < l; i++) {
        if (dir[i] === 0 && dir[i + 1] === 1) {
            return false;
        }
        if (dir[i] === 1 && dir[i + 1] === 0) {
            return false;
        }
        if (dir[i] === 2 && dir[i + 1] === 3) {
            return false;
        }
        if (dir[i] === 3 && dir[i + 1] === 2) {
            return false;
        }
        if (dir[i] === dir[i + 1]) {
            return false;
        }
    }
    return true;
}

let simulate = (a, k, x, y) => {
    let n = a.length;
    let m = a[0].length;
    // 구슬이 이미 구멍에 빠진 경우
    if (a[x][y] === ".") {
        return new Result(false, false, x, y);
    }
    let moved = false;
    
    // 기울임 한 번
    while (true) {
        let nx = x + dx[k];
        let ny = y + dy[k];
        // 범위를 벗어나는가?
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
            return new Result(moved, false, x, y);
        }

        let ch = a[nx][ny];
        if (ch == '#') {
            return new Result(moved, false, x, y);
        } else if (ch == 'R' || ch == 'B') {
            return new Result(moved, false, x, y);
        } else if (ch == '.') {
            let temp = a[nx][ny];
            a[nx][ny] = a[x][y];
            a[x][y] = temp;
            x = nx;
            y = ny;
            moved = true;
            // 기울임 한 번은 계속된다. 더 이상 움직이지 않을 때까지 기울임의 효과는 적용된다.
        } else if (ch == 'O') {
            // 이동에 대한 처리를 모두 하고 나서 구멍에 대한 이해를 하고 있다. 일단 이동을 다 시켜보고 검사한다.
            // if 빨간색 구멍 빠짐, and 파란색 구멍 안 빠짐 -> 빨강은 빠졌지만 파랑은 구멍에 빠졌는지 안빠졌는지 알 수 없음????
            // 만약 뒤쪽에서 파란색이 또 빠졌으면 -1 return
            // 빨간색 구멍 빠짐 -> 아예 보드에서 빨간색을 지워버림. 그러니까 빨간색 위치를 빈칸으로 바꾼다.
            // 보드 위치에서 빨간색이 아예 사라졌으므로
            // 그래서 파란색을 시도하는 다음 단계에서 빨간색이 이미 빈칸이 되어 버렸기 때문에 어 왜 이 새끼는 빨간색 구슬이 있다고 하는데 빈칸이지? 하고 바로 return 해버리는 것이다.
            a[x][y] = '.';
            moved = true;
            return new Result(moved, true, x, y);
        }
    }
}

let solution = (input) => {
    let n = parseInt(input[0].split(" ")[0]);
    let m = parseInt(input[0].split(" ")[1]);
    let map = input.slice(1, n + 1).map((v) => v.split(""));
    let a = Array(n).fill(false).map((v) => Array(m).fill(false));
    let answer = 987654321;

    for (let k = 0; k < (1 << LIMIT * 2); k++) {
        let dir = gen(k);
        if (!valid(dir)) {
            continue;
        }
        for (let i = 0; i < n; i++) {
            a[i] = map[i];
        }
        let cnt = check(a, dir);
        if (cnt === -1) continue;
        answer = Math.min(answer, cnt)
    }
    answer = answer === 987654321 ? -1 : answer
    return answer;
}
