const solution = (input) => {
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];
    let [n, m] = input[0].split(" ").map(Number);
    let [x, y, dir] = input[1].split(" ").map(Number);
    let a = input.slice(2, n + 2).map((v) => v.split(" ").map(Number));
    let count = 0;
    // a[x][y] = 0 (청소하지 않은 공간)
    // a[x][y] = 1 (벽)
    // a[x][y] = 2 (청소한 공간)
    while (true) {
        if (a[x][y] === 0) {
            // 1. 현재 위치를 청소한다
            a[x][y] = 2;
        }
        // 2-3, 2-4. 네 방향 모두 청소가 이미 되어있거나 벽인 경우
        if (a[x + 1][y] !== 0 && a[x - 1][y] !== 0 && a[x][y + 1] !== 0 && a[x][y - 1] !== 0) {
            let temp_x = x - dx[dir];
            let temp_y = y - dy[dir];
            if (a[temp_x][temp_y] === 1) {
                // 2-4. 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
                break;
            } else {
                // 2-3. 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
                x = temp_x;
                y = temp_y;
            }
        } else {
            // 2-1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음
            // 2-2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
            dir = (dir + 3) % 4;
            let temp_x = x + dx[dir];
            let temp_y = y + dy[dir];
            if (a[temp_x][temp_y] === 0) {
                x = temp_x;
                y = temp_y;
            }
        }
    }
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (a[i][j] === 2) {
                count += 1;
            }
        }
    }
    return count;
}

let input = ["11 10", "7 4 0", "1 1 1 1 1 1 1 1 1 1", "1 0 0 0 0 0 0 0 0 1", "1 0 0 0 1 1 1 1 0 1", "1 0 0 1 1 0 0 0 0 1", "1 0 1 1 0 0 0 0 0 1", "1 0 0 0 0 0 0 0 0 1", "1 0 0 0 0 0 0 1 0 1", "1 0 0 0 0 0 1 1 0 1", "1 0 0 0 0 0 1 1 0 1", "1 0 0 0 0 0 0 0 0 1", "1 1 1 1 1 1 1 1 1 1"];

console.log(solution(input));