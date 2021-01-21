const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

solution = () => {
    let n = rl.question("정수 n을 입력하세요.", function (answer) {
        console.log('정수 n', answer);
        rl.close();
    })
    let d = new Array(1001).fill(0);
    // 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
    // n = 1이면 (2x1) 1개 경우의 수 존재
    d[1] = 1;
    // n = 2이면 (1x2) 2개, (2x2) 1개, (2x1) 2개로 총 3개 경우의 수 존재
    d[2] = 3;
    for (let i = 3; i < n + 1; n++) {
      d[i] = (d[i - 1] * 1 + d[i - 2] * 2) % 796796;
    }
    return d[n];
};

solution();