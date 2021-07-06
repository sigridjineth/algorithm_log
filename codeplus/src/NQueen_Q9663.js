let n;
let a;
let check_col;
let check_dig;
let check_dig2;

const solution = (input) => {
    n = Number.parseInt(input);
    a = Array(15).fill(false).map(x => Array(15).fill(false));
    check_col = Array(15).fill(false);
    check_dig = Array(40).fill(false);
    check_dig2 = Array(40).fill(false);
    return calc(0); 
}

const calc = (row) => {
    if (row === n) {
        return 1;
    }
    let answer = 0;
    for (let col = 0; col < n; col++) {
        if (check(row, col)) {
            check_dig[row + col] = true;
            check_dig2[row - col + n] = true;
            check_col[col] = true;
            a[row][col] = true;
            answer += calc(row + 1);
            check_dig[row + col] = false;
            check_dig2[row - col + n] = false;
            check_col[col] = false;
            a[row][col] = false;
        }
    }
    return answer;
}

const check = (row, col) => {
    if (check_col[col] === true) {
        return false;
    }
    if (check_dig[row + col] === true) {
        return false;
    }
    if (check_dig2[row - col + n] === true) {
        return false;
    }
    return true;
}

let input = 8;
console.log(solution(input));