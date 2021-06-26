const solution = (input) => {
    let n = 4;
    let a = input.slice(0, n).map((v) => v.split("").map(Number));
    let k = input[n];
    let order = input.slice(n + 1, n + 1 + k).map((v) => v.split(" ").map(Number));
    
    for (let i = 0; i < k; i++) {
        let [no, dir] = order[i];
        no = no - 1; // index to minus one
        // 각각의 톱니는 동시에 회전해야 하기 때문에
        // 1) 각 톱니가 어느 방향으로 회전해야 하는 지 구하자
        let d = Array(n).fill(0);
        d[no] = dir;
        // 왼쪽 톱니를 연쇄적으로 구하고
        for (let i = no - 1; i >= 0; i--) {
            if (a[i][2] !== a[i + 1][6]) {
                d[i] = (-d[i + 1]);
            } else {
                // 한 톱니가 회전하지 않으면
                // 그 톱니의 왼쪽에 있는 톱니는 회전하지 않는다.
                break;
            };
        };
        // 오른쪽 톱니를 연쇄적으로 구하고
        for (let i = no + 1; i < n; i++) {
            if (a[i - 1][2] !== a[i][6]) {
                d[i] = (-d[i - 1]);
            } else {
                // 한 톱니가 회전하지 않으면
                // 그 톱니의 왼쪽에 있는 톱니는 회전하지 않는다.
                break;
            };
        };
        // 기록한 것을 바탕으로 회전을 시작한다
        for (let i = 0; i < n; i++) {
            if (d[i] === 0) {
                continue;
            } else if (d[i] === 1) {
                // 시계 방향 회전
                let temp = a[i][7];
                for (let j = 7; j >= 1; j--) {
                    a[i][j] = a[i][j - 1];
                };
                a[i][0] = temp;
            } else if (d[i] === -1) {
                // 반시계 방향 회전
                let temp = a[i][0];
                for (let j = 0; j < 7; j++) {
                    a[i][j] = a[i][j + 1];
                };
                a[i][7] = temp;
            };
        };
    };
    
    let answer = 0;
    for (let i = 0; i < n; i++) {
        if (a[i][0] === 1) {
            answer += (1 << i);
        };
    };
    
    return answer;
   }
   
   let input = ["10101111", "01111101", "11001110", "00000010", "2", "3 -1", "1 1"]
   
   console.log(solution(input))
