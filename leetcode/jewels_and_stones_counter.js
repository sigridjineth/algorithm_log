// Counter로 계산 생략
function solution(j, s) {
    function Counter(array) {
        return array.forEach(val => this[val] = (this[val] || 0) + 1);
    };
    // calculate the frequency of stone
    let freqs = new Counter(s.split(""));
    let count = 0;
    // calculate the frequency of jewels without comparison
    for (let char of j.split("")) {
        count += freqs[char];
    };
    return count;
}