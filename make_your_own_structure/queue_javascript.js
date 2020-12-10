class Queue {
    constructor() {
        this.input = [];
        this.output = []; // input과 output은 서로 순서가 다르다.
    }
    push(x) {
        this.input.push(x);
    };
    peek() {
        if (this.output.length === 0) {
            while (this.input.length > 0) {
                this.output.push(this.input.pop()); // 맨 끝에 있는 것부터 맨 앞으로 넣는다.
            };
        };
        return this.output[this.output.length - 1];
    };
    pop() {
        this.peek();
        return this.output.pop();
    };
    empty() {
        return this.output.length === 0 && this.input.length === 0;
    };
};