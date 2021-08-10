// top-down 방식으로 풀이한 팰린드롬 문제 접근법
let solution = (input) => {
    let n = parseInt(input[0]);
    let a = input[1].split(" ").map(Number);
    let m = parseInt(input[2]);
    let d = new Array(n).fill(-1).map((v) => new Array(n).fill(-1));

    function go(x, y) {
        if (x === y) {
            return 1;
        } else if (x + 1 === y) {
            if (a[x] === a[y]) {
                return 1;
            } else {
                return 0;
            }
        }
        if (d[x][y] !== -1) {
            return d[x][y];
        }
        if (a[x] !== a[y]) {
            d[x][y] = 0;
            return d[x][y];
        } else {
            d[x][y] = go(x + 1, y - 1);
            return d[x][y];
        }
    }

    let b = input.slice(3, 3 + m + 1).map((v) => v.split(" ").map(Number));
    return b.reduce((acc, cur) => {
        let x = cur[0];
        let y = cur[1];
        acc = acc + go(x - 1, y - 1) + "\n";
        return acc;
    }, "");
}

let input = ["7", "1 2 1 3 1 2 1", "4", "1 3", "2 5", "3 3", "5 7"]
console.log(solution2(input))