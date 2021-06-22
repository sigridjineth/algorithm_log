const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

const solution = (input) => {
  let [n, m, r] = input[0].split(" ").map(Number);
  let a = input.slice(1, n + 1).map((v) => v.split(" ").map(Number))
  let groups = [];
  let group_number = parseInt(Math.min(n, m) / 2);

  for (let k = 0; k < group_number; k++) {
    let current_group = [];
    for (let j = k; j < m - k; j++) {
      current_group.push(a[k][j]);
    }
    for (let i = k + 1; i < n - k - 1; i++) {
      current_group.push(a[i][m - k - 1]);
    }
    for (let j = m - k - 1; j > k; j--) {
      current_group.push(a[n - k - 1][j]);
    }
    for (let i = n - k - 1; i > k; i--) {
      current_group.push(a[i][k]);
    }
    groups.push(current_group);
  }
    
  for (let k = 0; k < group_number; k++) {
      let current_group = groups[k];
      let l = current_group.length;
      let index = r % l;
      for (let j = k; j < m - k; j++) {
          a[k][j] = current_group[index];
          index = (index + 1) % l;
      };
      for (let i = k + 1; i < n - k - 1; i++) {
          a[i][m - k - 1] = current_group[index];
          index = (index + 1) % l;
      };
      for (let j = m - k - 1; j > k; j--) {
          a[n - k - 1][j] = current_group[index];
          index = (index + 1) % l;
      };
      for (let i = n - k- 1; i > k; i--) {
          a[i][k] = current_group[index];
          index = (index + 1) % l;
      };
  };
    
  return a.map((v) => v.join(" ")).join("\n");
};

console.log(solution(input))
