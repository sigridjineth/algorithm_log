// 일정 재구성 LEETCODE #332 그래프 반복 풀이
class DefaultMap extends Map {
    constructor(getDefaultValue, ...mapConstructorArgs) {
        super(mapConstructorArgs);
        if (typeof getDefaultValue !== 'function') {
            throw new Error('getDefaultValue must be a function');
        };
        this.getDefaultValue = getDefaultValue;
    };
    get = (key) => {
        if (!this.has(key)) {
            this.set(key, this.getDefaultValue(key));
        };
        return super.get(key);
    };
}

solution = (tickets) => {
    let graph = new DefaultMap(() => []);
    // constructing a orderly graph
    tickets.sort(function (a, b) {
        if (a[0] === b[0]) {
            if (a[1] >= b[1]) {
                return 1;
            };
            if (b[1] > a[1]) {
                return -1;
            };
        };
        if (a[0] > b[0]) {
            return 1;
        };
        if (b[0] > a[0]) {
            return -1;
        };
    });

    for ([a, b] of tickets) {
        graph.get(a).push(b);
    };

    let route = [];
    let stack = ['JFK'];

    while (stack.length > 0) {
        // 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while (graph.get(stack[stack.length-1]).length > 0) {
            stack.push(graph.get(stack[stack.length-1]).shift());
        };
        route.push(stack.pop());
    };

    return route.reverse();
};

console.log(solution([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]));