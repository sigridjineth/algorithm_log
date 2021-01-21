solution = (n, m, arr) => {
    const dx = [-1, 0, 1, 0];
    const dy = [0, 1, 0, -1];

    let queue = [];
    queue.shift({
        x: 0,
        y: 0
    });

    while (queue.length > 0) {
        const element = queue.shift();
        for (let i = 0; i < 4; i++) {
            const next_x = element.x + dx[i];
            const next_y = element.y + dy[i];
        }

        // 범위 밖으로 벗어난 경우
        if (next_x < 0 || next_y < 0 || next_x >= n || next_y >= m) {
            continue;
        }

        // 인접 요소가 1인 경우에만 이동
        if (arr[next_x][next_y] !== 1) {
            continue;
        }

        arr[next_x][next_y] = arr[element.x][element.y] + 1;
        queue.shift({
            x: next_x,
            y: next_y
        });

        const answer = arr[n-1][m-1];
        console.log(answer);
    }
}