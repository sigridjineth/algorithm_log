// 2020.11.15 전보 문제 풀이를 위한 다익스트라 알고리즘 구현

solution = (N, road, K, start) => {
    let answer = -1;
	  let count = 0;
    
    // 그래프 생성
    const graph = new Array(N).fill(null).map(() => new Array());
    for (let path of road) {
        const [u, v, w] = path;
        graph[u-1].push([v-1, w]);
        graph[v-1].push([u-1, w]);
    }
    
    // 우선순위 큐 생성
    const dist = new Array(N).fill(Number.MAX_SAFE_INTEGER);
    const visited = new Array(N).fill(false);
    const priorityQueue = new PriorityQueue(dist);
    
    // 시작하는 start번 초기화
    priorityQueue.enqueue(start);
    dist[start] = 0;
    
    // 다익스트라 알고리즘
    while (priorityQueue.queue.length > 0) {
        const curr = priorityQueue.dequeue();
        
        if (visited[curr]) {
            continue;
        }
        
        for (const [next, weight] of graph[curr]) {
            if (dist[next] > dist[curr] + weight) {
                dist[next] = dist[curr] + weight;
                priorityQueue.enqueue(next);
            }
        }
    }
    
    // 최종 결과
    for (let distance of dist) {
        if (distance > answer) {
            answer = distance;
			count++;
        }
    }
    
    return [count, answer];
}

class PriorityQueue {
    constructor(dist) {
        this.queue = [];
        this.dist = dist;
    }
    
    enqueue(nodeIdx) {
        this.queue.push(nodeIdx);
    }
    
    dequeue() {
        let entry = 0;
        let entryIdx = this.queue[entry];
        
        this.queue.forEach((nodeIdx, idx) => {
            if (this.dist[entryIdx] > this.dist[nodeIdx]) {
                entryIdx = nodeIdx;
                entry = idx;
            }
        });
        
        return this.queue.splice(entry, 1);
    }
};
