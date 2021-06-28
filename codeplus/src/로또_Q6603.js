const solution = (input) => {
    let index = 0;
    while (input[index].length !== 1) {
        let a = input[index].split(" ").map(Number).slice(1);
        solve(a, 0, 0, []);
        console.log();
        index += 1;
    }
}

const solve = (a, index, cnt, lotto) => {
    if (cnt === 6) {
        console.log(...lotto);
        return;
    }
    if (a.length === index) {
        return;
    }
    lotto.push(a[index]);
    solve(a, index + 1, cnt + 1, lotto);
    lotto.pop();
    solve(a, index + 1, cnt, lotto);
}

let input = ["7 1 2 3 4 5 6 7", "8 1 2 3 5 8 13 21 34", "0"]

solution(input);
