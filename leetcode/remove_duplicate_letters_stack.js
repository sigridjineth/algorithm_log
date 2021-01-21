solution = (s) => {
    splitArray = s.split("");
    counter = new Counter(splitArray);
    stack = [];

    for (let char of splitArray) {
        counter[char] -= 1;
        if (stack.includes(char)) {
            continue;
        };
        while (stack.length > 0 && char < stack[stack.length-1] && counter[stack[stack.length-1]] > 0) {
            stack.pop();
        };
        stack.push(char);
    };

    return stack.join('');
}

function Counter(array) {
    array.forEach(val => this[val] = (this[val] || 0) + 1);
};

console.log(solution("cbacdcbc"));