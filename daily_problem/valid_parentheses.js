let isValid = function(str) {
    stack = [];
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    };
    for (let char of str.split("")) {
        if (!Object.keys(table).includes(char)) {
            stack.push(char);
        } else if (stack.length === 0 || table[char] != stack.pop()) {
            return false
        };
    };
    return stack.length === 0;
};