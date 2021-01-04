// LEETCODE 621
class Counter {
    constructor(array) {
        this.count = {}
        array.forEach(val => this.count[val] = (this.count[val] || 0) + 1)
    };
    getCounter() {
        return this.count
    };
    most_common(k) {
      const keysSorted = Object.keys(this.count).sort((a, b) => this.count[b] - this.count[a]);
      return keysSorted.slice(0, k+1)
    };
    subtract(element) {
        this.count[element] -= 1
    };
    remove_zero() {
        this.count = Object.keys(this.count).reduce((acc, curr) => {
            if(this.count[curr] >= 0) {
                acc[curr] = this.count[curr]
            }
            return acc;
        }, {})
    };
    isBreak() {
        return Object.values(this.count).every(x => (x === 0))
    }
};

leastInterval = (tasks, n) => {
    let result = 0
    let counter = new Counter(tasks)
    while (true) {
        let sub_count = 0
        for (let task of counter.most_common(n+1)) {
            sub_count += 1
            result += 1
            counter.subtract(task)
            counter.remove_zero()
        }
        if (counter.isBreak()) {
            break
        }
        if (n - sub_count + 1 < 0) {
            continue;
        } else {
            result += n - sub_count + 1
        }
    }
    return result
}

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
console.log(leastInterval(tasks, n))
