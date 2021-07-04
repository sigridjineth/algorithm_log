let n;

const go = (a) => {
    let n = a.length;
    if (n === 2) {
        return 0;
    }
    let answer = 0;
    for (let i = 1; i < n - 1; i++) {
        let energy = a[i - 1] * a[i + 1];
        let b = a.slice(0, i).concat(a.slice(i + 1, a.length));
        energy += go(b);
        if (answer < energy) {
            answer = energy;
        }
    }
    return answer;
}

const solution = (input) => {
    n = Number.parseInt(input[0]);
    let a = input[1].split(" ").map((v) => Number.parseInt(v));
    console.log(go(a));
}

let input = ["4", "1 2 3 4"];
solution(input);