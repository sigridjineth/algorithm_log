let dailyTemperatures = function(T) {
    let list = T;
    let answer = new Array(list.length).fill(0);
    let stack = [];
    
    for (let i = 0; i < list.length; i++) {
        let cur = list[i];
        while (stack.length > 0 && cur > list[stack[stack.length-1]]) {
            let last = stack.pop();
            answer[last] = i - last;
        };
        stack.push(i);
    };
    return answer
};