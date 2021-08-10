// 어디에서 왔는가를 기준으로 점화식을 작성하는 경우
let solution = (input) => {
    let n = Number.parseInt(input[0]);
    let a = input[1].split(" ").map(Number);
    let d = new Array(n).fill(-1);

    d[0] = 0;
    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (d[j] !== -1 && (i - j) <= a[j]) {
                if (d[i] === -1 || d[i] > d[j] + 1) {
                    d[i] = d[j] + 1;
                }
            }
        }
    }

    return d[n - 1];
}

// 어디로 갈 수 있는가를 기준으로 점화식을 작성하는 경우 2
let solution2 = (input) => {
    let n = Number.parseInt(input[0]);
    let a = input[1].split(" ").map(Number);
    let d = new Array(n).fill(-1);

    d[0] = 0;
    for (let i = 0; i < n - 1; i++) {
        if (d[i] === -1) {
            continue;
        }
        for (let j = 1; j <= a[i]; j++) {
            if ((i + j) >= n) {
                break;
            }
            if (d[i + j] === -1 || d[i + j] > d[i] + 1) {
                d[i + j] = d[i] + 1;
            }
        }
    }

    return d[n - 1];
}

let input = ["10", "1 2 0 1 3 2 1 5 4 2"]
console.log(solution2(input))