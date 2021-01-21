solution = () => {
    let nm = window.prompt().split(" ");
    let n = parseInt(nm[0]);
    let m = parseInt(nm[1]);
    // N개의 화폐 단위 정보를 입력
    let array = [];
    for (let i = 0; i < n; i++) {
        array.push(parseInt(window.prompt().split()));
    }
    // 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
    let d = new Array(10001).fill(10001);
    // 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
    d[0] = 0
    d[Math.min.apply(null, array)] = 1;
    for (let i = Math.min.apply(null, array); i < (m + 1); i++) {
        for (let element of array) {
            if (d[i - element] < 0 || (i - element) < 0) {
                break;
            }
            d[i] = Math.min.apply(null, [d[i], d[i - element] + 1]);
        }
    }
    // 계산된 결과 출력
    if (d[m] == 10001) {
        console.log(-1);
    } else {
        console.log(d[m]);
    }
};
