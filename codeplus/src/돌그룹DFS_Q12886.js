let solution = (input) => {
    let [a, b, c] = input.split(" ").map((v) => Number(v));
    let sum = a + b + c;
    let check = new Array(1001).fill(false).map((v) => new Array(1001).fill(false));
    let ans = 0;
    
    function dfs(a, b) {
        let c = sum - a - b;
        if (a === b && b === c) { // 값이 모두 같으면 true 반환
            return true;
        };
        let nums = [a, b, c];
        let flag = false;
        // a, b, c로 3개의 값에 대해 상호 비교를 수행
        for (let i = 0; i < 3; i++) {
            for (let j = i + 1; j < 3; j++) {
                if (nums[i] !== nums[j]) {
                    let ni = (nums[i] > nums[j]) ? nums[i] - nums[j] : nums[i] * 2;
                    let nj = (nums[j] > nums[i]) ? nums[j] - nums[i] : nums[j] * 2;
                
                    // 범위 내에 있으며 이전에 체크하지 않은 경우라면
                    if (ni <= 1000 && nj <= 1000 && !check[ni][nj] && !check[nj][ni]) {
                        check[ni][nj] = true;
                        check[nj][ni] = true;
                        flag = dfs(ni, nj);
                    };
                    // 만약 true가 반환되었다면 값이 모두 같은 것이므로 true 반환
                    if (flag) {
                        return true;
                    };
                } else {
                    continue;
                };
            };
        };
        // 여기 전까지 true가 반환되지 못했다면 false 반환
        return false;
    };
    
    check[a][b] = true;
    check[b][a] = true;

    if (sum % 3 === 0 && dfs(a, b)) {
        ans = 1;
    };
    
    return ans;
};

console.log(solution(input))
