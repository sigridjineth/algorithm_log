const solution = (input) => {
    let [n, l] = input[0].split(" ").map(Number);
    let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number));
    let ans = 0;
    for (let i = 0; i < n; i++) {
        // 행 검사
        let d = Array(n).fill(0);
        for (let j = 0; j < n; j++) {
            d[j] = a[i][j];
        };
        if (go(d, l)) {
            ans += 1;
        };
    }
    for (let j = 0; j < n; j++) {
        // 열 검사
        let d = Array(n).fill(0);
        for (let i = 0; i < n; i++) {
            d[i] = a[i][j];
        };
        if (go(d, l)) {
            ans += 1;
        };
    };
    return ans;
}

const go = (a, l) => {
    // 한 줄 검사
    let n = a.length;
    let c = Array(n).fill(false);
    for (let i = 1; i < n; i++) {
        if (a[i - 1] !== a[i]) {
            // 인접한 칸의 높이가 다르면, 경사로를 놓아야 한다.
            let diff = a[i] - a[i - 1];
            if (diff < 0) {
                diff = -diff;
            }
            if (diff !== 1) {
                // 낮은 칸과 높은 칸의 차이는 1이어야 한다.
                return false;
            }
            if (a[i - 1] < a[i]) {
                // 오른쪽으로 더 높게 경사로를 놓아야 하는 경우
                for (let j = 1; j <= l; j++) {
                    if (i - j < 0) {
                        // 경사로를 놓다가 범위를 벗어나는 경우
                        return false;
                    }
                    if (a[i - 1] !== a[i - j]) {
                        // 낮은 지점의 칸이 모두 같지 않거나, L개가 연속되지 않은 경우
                        return false;
                    }
                    if (c[i - j]) {
                        return false;
                    }
                    c[i - j] = true;
                }
            } else {
                // a[i - 1] > a[i] 왼쪽으로 더 높게 경사로를 놓아야 하는 경우
                for (let j = 0; j < l; j++) {
                    if (i + j >= n) {
                        // 경사로를 놓다가 범위를 벗어나는 경우
                        return false;
                    }
                    if (a[i] !== a[i + j]) {
                        // 낮은 지점의 칸이 모두 같지 않거나, L개가 연속되지 않은 경우
                        return false;
                    }
                    if (c[i + j]) {
                        return false;
                    }
                    c[i + j] = true;
                }
            }
        }
    }
    return true;
}

let input = ["6 2", "3 3 3 3 3 3", "2 3 3 3 3 3", "2 2 2 3 2 3", "1 1 1 2 2 2", "1 1 1 3 3 1", "1 1 2 3 3 2"];

console.log(solution(input))
