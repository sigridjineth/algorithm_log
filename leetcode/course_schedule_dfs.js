// 코스 스케줄 LEETCODE #207
// DFS로 순환 구조 판별
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
};

let canFinish = function(numCourses, prerequisites) {
    let graph = new DefaultMap(() => []);
    for ([x, y] of prerequisites) {
        graph.get(x).push(y);
    };

    const traced = new Set();
    const visited = new Set();
    
    function dfs(i) {
        // iteration structure would be False
        if (traced.has(i)) {
            return false;
        };
        // if already visited node then it means it passes the condition then return true
        if (visited.has(i)) {
            return true;
        }
        traced.add(i);
        
        for (let y of graph.get(i)) {
            if (dfs(y) === false) {
                return false;
            };
        };
        // remove node after iteration
        traced.delete(i);
        // add node to visited after iteration
        visited.add(i);
        return true;
    };
    
    // determine whether it is cycled structure
    for (let x of graph) {
        if (dfs(x[0]) === false) {
            return false;
        };
    };
    
    return true;
};
