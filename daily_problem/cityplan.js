find_parent = (parent, x) => {
  if (parent[x] != x) {
    parent[x] = find_parent(parent, parent[x]);
  };
  return parent[x];
}

union_parent = (parent, a, b) => {
  a = find_parent(parent, a);
  b = find_parent(parent, b);
  if (a < b) {
    parent[b] = a;
  } else {
    parent[a] = b;
  }
}

solution = () => {
  [v, e] = window.prompt().split(" ").map((element) => Number(element));
  let parent = new Array(v+1).fill(0);
  let edges = []; // 간선 전체를 담을 변수
  let result = 0; // 최종 비용을 담을 변수

  for (let i = 1; i < v+1; i++) {
    parent[i] = i;
  }

  for (let i = 0; i < e; i++) {
    [a, b, cost] = window.prompt().split(" ").map((element) => Number(element));
    edges.push({
      cost: cost,
      a: a,
      b: b
    })
  }

  edges.sort((a, b) => {
    return a.cost - b.cost;
  });

  last = 0; // 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

  for (let edge of edges) {
    let cost = edge.cost;
	let a = edge.a;
	let b = edge.b;
    if (find_parent(parent, a) != find_parent(parent, b)) {
      union_parent(parent, a, b);
      result = result + cost;
      last = cost; // 마지막 간선을 cost에서 제외한다.
    }
  }

  console.log(result - last);
}
