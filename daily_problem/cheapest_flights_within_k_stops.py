class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # graph adjacent list
        for u, v, w in flights:
            graph[u].append((v, w))
        # Q variable: [(price, static point, remaining stopovers)]
        Q = [(0, src, K)]
        # determine the minimal cost starting from minimum point to destination
        while Q:
            price, node, k = heapq.heappop(Q)
            if (node == dst): # if arriving at the destination
                return price
            if (k >= 0): # while the stopover condition does not meet yet
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
        return -1