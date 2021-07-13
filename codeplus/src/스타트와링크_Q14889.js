const next_permutation = (a) => {
    let i = a.length - 1;
    while (i > 0 && a[i - 1] >= a[i]) {
        i -= 1;
    }
    if (i <= 0) {
        return false;
    }
    let j = a.length - 1;
    while (j > 0 && a[j] <= a[i - 1]) {
        j -= 1;
    }
    if (j <= 0) {
        return false;
    }

    let temp = a[i - 1];
    a[i - 1] = a[j];
    a[j] = temp;

    j = a.length - 1;
    while (i < j) {
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
        i += 1;
        j -= 1;
    }
    return true;
}

const solution = (input) => {
    let n = Number.parseInt(input[0]);
    let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number));
    let b = Array(n / 2).fill(1).concat(Array(n / 2).fill(0));
    b.sort();
    let ans = Number.MAX_SAFE_INTEGER;
    do {
        let first = [];
        let second = [];
        for (let i = 0; i < n; i++) {
            if (b[i] === 0) {
                first.push(i);
            } else {
                second.push(i);
            }
        }
        let one = 0;
        let two = 0;
        for (let i = 0; i < n / 2; i++) {
            for (let j = 0; j < n / 2; j++) {
                if (i === j) continue;
                one += a[first[i]][first[j]];
                two += a[second[i]][second[j]];
            }
        }
        let diff = Math.abs(one - two);
        if (ans > diff) {
            ans = diff;
        }
    } while (next_permutation(b));
    return ans;
}

let input = ["4", "0 1 2 3", "4 0 5 6", "7 1 0 2", "3 4 5 0"];
console.log(solution(input));
