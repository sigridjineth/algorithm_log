// 플로이드 워셜 알고리즘

const INF = Infinity;

const fw = function(dist) {
    const len = dist.length;
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            for (let k = 0; k < len; k++) {
                if (dist[j][k] > dist[j][i] + dist[i][k])
                    dist[j][k] = dist[j][i] + dist[i][k];
            };
        };
    };
};

const main = function() {
    const graph = [
        [0, 5, INF, 8],
        [7, 0, 9, INF],
        [2, INF, 0, 4],
        [INF, INF, 3, 0]
    ];
    fw(graph);
    for (let i = 0; i < graph.length; i++) {
        console.log(graph[i]);
    };
};

