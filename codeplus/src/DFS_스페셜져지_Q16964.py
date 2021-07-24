from collections import deque

def solution():
	# 과정 1: 그래프의 무방향 간선을 입력받는다.
	n = int(input())
	a = [[] for _ in range(n)]

	for _ in range(n - 1):
		u, v = map(int, input().split())
		u -= 1
		v -= 1
		a[u].append(v)
		a[v].append(u)

	# 과정 2: 사용자의 DFS 순회값을 입력받고, 그 순서를 계산한다.
	# 인접 리스트의 순서도 이에 따라 바꿔준다.
	b = list(map(int, input().split()))
	b = [x - 1 for x in b]
	order = [0] * n

	for i in range(n):
		order[b[i]] = i

	for i in range(n):
		a[i].sort(key = lambda x: order[x])

	# 과정 3: 만들어진 그래프를 탐색하고 사용자 입력과 비교한다.
	dfs_order = []
	check = [False] * n

	def dfs(x):
		if (check[x]):
			return
		dfs_order.append(x)
		check[x] = True
		for y in a[x]:
			dfs(y)

	dfs(0)

	ok = True
	for i in range(n):
		if (dfs_order[i] != b[i]):
			ok = False
			break

	return (1 if ok else 0)

print(solution())
