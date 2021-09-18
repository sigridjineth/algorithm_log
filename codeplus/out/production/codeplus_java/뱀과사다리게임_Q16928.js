const input = require("fs")
	.readFileSync("/dev/stdin")
	.toString()
	.trim()
	.split("\n");

let solution = (input) => {
    let [n, m] = input[0].split(" ").map((v) => parseInt(v));
    let dist = new Array(101).fill(-1);
    let next = input.slice(1, n + m + 1).map((v) => v.split(" ").map(Number)).reduce((acc, cur, idx, arr) => {
        acc[cur[0]] = cur[1];
        return acc;
    }, []);
    dist[1] = 0;
    let queue = [];
    queue.push(1);
    
    while (queue.length !== 0) {
        let x = queue.shift();
        for (let i = 1; i < 7; i++) {
            let y = x + i;
            if (y > 100) {
                continue;
            };
            if (next[y] === undefined && dist[y] === -1) {
                dist[y] = dist[x] + 1;
                queue.push(y);
            };
            if (next[y] !== undefined && dist[next[y]] === -1) {
                dist[next[y]] = dist[x] + 1;
                dist[y] = dist[x] + 1; // 이게 안되면 괜히 이미 거쳐간 사다리/뱀 녀석을 또 큐에 추가해줘야 할 수 있다.
                queue.push(next[y]);
            }
        }
    }
  
    return dist[100];
}

console.log(solution(input))
