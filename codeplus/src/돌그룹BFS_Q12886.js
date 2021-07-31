let solution = (input) => {
    let [a, b, c] = input.split(" ").map((v) => Number(v));
    let sum = a + b + c;
    let check = new Array(1001).fill(false).map((v) => new Array(1001).fill(false));
    let ans = 0;
    
    if (sum % 3 !== 0) {
        return ans;
    };
    
    let queue = [];
    queue.push(new Group(a, b));
    check[a][b] = true;
    check[b][a] = true;
    
    let flag = false;
    while (queue.length !== 0) {
        let g = queue.shift();
        let a = g.a;
        let b = g.b;
        let c = sum - a - b;
        let nums = [a, b, c];
        
        // 모두 같아진 경우 멈춘다.
        if (a === b && b === c) {
            flag = true;
            break;
        };
        
        // a, b, c가 각각 다른 경우 모든 경우에 대해 개수를 조정하고 다음 탐색을 위해 Queue에 넣는다.
        for (let i = 0; i < 3; i++) {
            for (let j = i + 1; j < 3; j++) {
                if (nums[i] !== nums[j]) {
                    let ni = (nums[i] > nums[j]) ? nums[i] - nums[j] : nums[i] * 2;
                    let nj = (nums[j] > nums[i]) ? nums[j] - nums[i] : nums[j] * 2;

                    // 범위 내에 있으며 이전에 체크하지 않은 경우라면
                    if (ni <= 1000 && nj <= 1000 && !check[ni][nj] && !check[nj][ni]) {
                        check[ni][nj] = true;
                        check[nj][ni] = true;
                        queue.push(new Group(ni, nj));
                    };
                } else {
                    continue;
                };
            };
        };
    };
    
    if (flag) {
        ans = 1;
    };
    
    return ans;
};

let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

console.log(solution(input))
