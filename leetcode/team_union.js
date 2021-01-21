solution = () => {
    [n, m] = window.prompt().split(" ").map((element) => Number(element));
    let parent = new Array(n+1).fill(0);
    for (let i = 0; i < n + 1; i++) {
        parent[i] = i;
    };
    for (let i = 0; i < m; i++) {
        [opr, a, b] = window.prompt().split(" ").map((element) => Number(element));
        // if union
        if (opr == 0) {
            union_parent(parent, a, b);
        } else if (opr == 1) {
            if (find_parent(parent, a) == find_parent(parent, b)) {
                console.log('YES');
            } else {
                console.log('NO');
            };
        };
    };
};

find_parent = (parent, x) => {
    if (parent[x] != x) {
        parent[x] = find_parent(parent, parent[x]);
    };
    return parent[x];
};

union_parent = (parent, a, b) => {
    a = find_parent(parent, a);
    b = find_parent(parent, b);
    if (a < b) {
        parent[b] = a;
    } else {
        parent[a] = b;
    };
};
