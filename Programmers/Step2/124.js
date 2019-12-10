function solution(n) {
    var result = "";
    while (n > 0) {
        var c = n % 3;
        n = Math.floor((n - 1) / 3)
        result = [4, 1, 2][c] + result
    }
    return result
};