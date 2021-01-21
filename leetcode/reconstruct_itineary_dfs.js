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

let findItinerary = function(tickets) {
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
    
    function dfs(a) {
        // deciphering the first value and visiting in order
        while (graph.get(a).length > 0) {
            dfs(graph.get(a).shift());
        };
        route.push(a);
    };
    
    dfs('JFK');
    return route.reverse();
};

console.log(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]));