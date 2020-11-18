class Queue {
  constructor() {
    this._arr = [];
  }

  enqueue(item) {
    this._arr.push(item);
  }

  dequeue() {
    return this._arr.shift();
  }

  isEmpty() {
    return this._arr.length == 0;
  }
}

topology_sort = (time, indegree, graph) => {
  // 알고리즘 수행 결과를 담을 리스트
  let result = Object.values(time);
  let q = new Queue();

  // 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for (let i = 1; i < v + 1; i++) {
    if (indegree[i] == 0) {
      q.enqueue(i);
    }
  }

  // 큐가 빌 때까지 반복
  while (!q.isEmpty()) {
    // 큐에서 원소 꺼내기
    let now = q.dequeue();
    // 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for (let i of graph[now]) {
      // 최대 시간을 보는 것이므로 현재까지 루트 노드 또는 자기 자신의 시간과 지금 체크하고 있는 노드의 시간과 나의 강의 시간을 합쳤을 때 어느 것이 더 큰 지 비교한 후 더 큰 시간에 업데이트 한다.
      result[i] = Math.max.apply(null, [result[i], result[now] + time[i]]);
      // 진입 차수를 1 낮춘다.
      indegree[i] = indegree[i] - 1;
      // 새롭게 진입차수가 0이 되는 노드를 큐에 삽입한다.
      if (indegree[i] == 0) {
        q.enqueue(i);
      }
    }
  }

// 위상 정렬을 수행한 결과 출력
    for (let i = 1; i < v + 1; i++) {
      console.log(result[i]);
    }
};

solution2 = () => {
  // 노드의 개수 입력받기
  [v] = window.prompt('노드의 개수 입력해주기').split("").map((element) => Number(element));
  // 모든 노드에 대한 진입차수는 0으로 초기화
  let indegree = new Array(v+1).fill(0);
  // 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
  let graph = Array(v+1).fill(null).map(() => Array());
  // 각 강의 시간을 0으로 초기화
  let time = new Array(v+1).fill(0);
  // 방향 그래프의 모든 간선 정보를 입력받기
  for (let i = 1; i < v+1; i++) {
    let data = window.prompt('데이터를 입력해주세요.').split(" ").map((element) => Number(element));
    time[i] = data[0];
    data.map((element, index) => {
	  if (element == -1) {
		return;
      };
      if (index != 0) {
        // 해당 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호 입력
        indegree[i] = indegree[i] + 1;
        graph[element].push(i);
      }
    })
  }
  topology_sort(time, indegree, graph);
};
