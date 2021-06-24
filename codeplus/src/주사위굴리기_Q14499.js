const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

const solution = (input) => {
  let dx = [0, 0, -1, 1];
  let dy = [1, -1, 0, 0];
  let [n, m, x, y, k] = input[0].split(" ").map(Number);
  let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number));
  let dice = Array(7).fill(0);
  let move = input[n + 1].split(" ").map(Number);
  
  for (let now of move) {
    now = now - 1;
    let nx = x + dx[now];
    let ny = y + dy[now];
    if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
      continue;
    }
    if (now === 0) {
      let temp = dice[1];
      dice[1] = dice[4];
      dice[4] = dice[6];
      dice[6] = dice[3];
      dice[3] = temp;
    } else if (now === 1) {
      temp = dice[1];
      dice[1] = dice[3];
      dice[3] = dice[6];
      dice[6] = dice[4];
      dice[4] = temp;
    } else if (now === 2) {
      temp = dice[1];
      dice[1] = dice[5];
      dice[5] = dice[6];
      dice[6] = dice[2];
      dice[2] = temp;
    } else if (now === 3) {
      temp = dice[1];
      dice[1] = dice[2];
      dice[2] = dice[6];
      dice[6] = dice[5];
      dice[5] = temp;
    }
    x = nx;
    y = ny;
    if (a[x][y] === 0) {
        a[x][y] = dice[6];
    } else {
        dice[6] = a[x][y];
        a[x][y] = 0;
    }
    console.log(dice[1]);
  }
};

solution(input)
