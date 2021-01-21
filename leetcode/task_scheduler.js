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

// https://www.three-snakes.com/coding-test/leet-code/621
// 와... 함수형 자바스크립트를 잘 사용하면 정말 가능성이 무궁무진하다는 것을 깨달았다.
let leastInterval_retry = function(tasks, n) {
    if (n === 0) return tasks.length;
  
    const countMap = tasks.reduce((map, task) => {
      if (!map[task]) map[task] = 0;
      map[task] += 1;
      return map;
    }, {});
  
    const max = Math.max(...Object.keys(countMap).map((value) => countMap[value]));
    const isSameMaxCount = Object.keys(countMap).reduce((sameCount, key) => {
      if (max === countMap[key]) sameCount += 1;
      return sameCount;
    }, 0) - 1;
    const idle = n * (max-1);
    const remain = tasks.length - (max + isSameMaxCount + idle);
    
    return max + idle + isSameMaxCount + (remain > 0 ? remain : 0);
  };

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
console.log(leastInterval_retry(tasks, n))
