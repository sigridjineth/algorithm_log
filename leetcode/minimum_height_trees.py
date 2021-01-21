class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # exception condition
        if (n <= 1):
            return [0]
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        # adding the first leaf node
        leaves = []
        for i in range(n+1):
            if (len(graph[i]) == 1):
                leaves.append(i)
        # iterating till the remaining node length is 1
        while (n > 2):
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                # leaves를 탐색하며
                # 순서대로 graph의 leaf에 해당하는 녀석을 하나 꺼내서
                neighbor = graph[leaf].pop()
                # 반대편 쪽에도 하나 지우고
                graph[neighbor].remove(leaf)
                # 그 지운 녀석이 하나가 남으면 새로이 추가한다.
                if (len(graph[neighbor]) == 1):
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves