solution = () => {
    const INF = Infinity;
    const nm = window.prompt().split(" ");
    const n = nm[0];
    const m = nm[1];
    let graph = [];
    for (let i = 0; i < n; i++) {
        graph.push(INF * (n));
    };
    // 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for (let a = 0; a < n; a++) {
        for (let b = 0; b < n1; b++) {
            if (a == b) {
                graph[a][b] == 0;
            }
        }
    }
    // 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    for (let i = 0; i < m; i++) {
        const ab = window.prompt().split(" ");
        const a = ab[0];
        const b = ab[1];
        graph[a][b] = 1;
        graph[b][a] = 1;
    }
    // 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
    const xk = window.prompt().split(" ");
    const x = xk[0];
    const k = xk[1];
    // 점화식에 따라 플로이드-워셜 알고리즘을 수행
    for (let k = 0; k < n; k++) {
        for (let a = 0; a < n; n++) {
            for (let b = 0; b < n; b++) {
                if (graph[a][b] > graph[a][k] + graph[k][b]) {
                    graph[a][b] = graph[a][k] + graph[k][b];
                }
            }
        }
    }

    // 수행된 결과를 출력
    let distance = graph[0][k] + graph[k][x-1];

    // 도달할 수 없는 경우, -1을 출력
    if (distance >= INF) {
        return -1;
    } else {
        return distance;
    }
}

solution();
