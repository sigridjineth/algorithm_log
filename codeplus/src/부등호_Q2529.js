const solution = (input) => {
    let k = Number.parseInt(input[0]);
    let a = input[1].split(" ");
    let small = Array.from(Array(10).keys());
    let big = Array.from(Array(10).keys()).reverse();
    do {
        if (check(small, a)) {
            break;
        }
    } while (next_permutation(small));
    do {
        if (check(big, a)) {
            break;
        }
    } while(prev_permutation(big));
    console.log(big.slice(0, k + 1).join(''));
    console.log(small.slice(0, k + 1).join(''));
}

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

const prev_permutation = (a) => {
    let i = a.length - 1;
    while (i > 0 && a[i - 1] <= a[i]) {
        i -= 1;
    }
    if (i <= 0) {
        return false;
    }
    let j = a.length - 1;
    while (j > 0 && a[j] >= a[i - 1]) {
        j -= 1;
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

const check = (perm, a) => {
    for (let i = 0; i < a.length; i++) {
        if (a[i] === '<' && perm[i] > perm[i + 1]) {
            return false;
        }
        if (a[i] === '>' && perm[i] < perm[i + 1]) {
            return false;
        }
    }
    return true;
}

let input = ["9", "> < < < > > > < <"]
solution(input);