let alpha = new Array(256);

const solution = (input) => {
    let n = Number.parseInt(input[0]);
    let a = input.slice(1, n + 1);
    let letters = [...new Set(input.slice(1, n + 1).map((v) => v.split("")).reduce((a, b) => a.concat(b), []))];
    let m = letters.length;
    let d = Array.from(Array(10).keys()).reverse().slice(0, m);
    d.sort();
    let ans = 0;
    do {
        let now = calc(a, letters, d);
        if (ans < now) {
            ans = now;
        };
    } while (next_permutation(d));
    return ans;
};

const calc = (a, letters, d) => {
    let m = letters.length;
    let sum = 0;
    for (let i = 0; i < m; i++) {
        alpha[letters[i]] = d[i];
    };
    for (let s of a) {
        let now = 0;
        for (let x of s.split("")) {
            now = now * 10 + alpha[x];
        };
        sum += now;
    };
    return sum;
};

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

console.log(solution(input))
