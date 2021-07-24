from collections import deque

def solution():
	n = int(input())
	a = [[] for _ in range(n)]
	check = [False] * n
	parent = [-1] * n
	
	for _ in range(n - 1):
		u, v = map(int, input().split())
		u -= 1
		v -= 1
		a[u].append(v)
		a[v].append(u)

	order = list(map(int, input().split()))
	order = [x - 1 for x in order]
	
	q = deque()
	q.append(0)
	check[0] = True
	m = 1 # 큐의 크기는 1에서 시작이다. 시작점을 넣었기 때문이다.

	for i in range(n):
		# 아직 BFS 가 진행중인데 큐가 비어있음.
		if not q:
			return 0

		# order 의 순서대로 하나씩 검사
		x = q.popleft()
		if (x != order[i]):
			return 0
			
		# 큐에 넣을 정점의 수
		cnt = 0
		for y in a[x]:
			if (check[y] is False):
				parent[y] = x
				cnt += 1
				
		for j in range(cnt):
			# 큐에는 m - 1개가 있고, 그 이후에 cnt개를 넣는다.
			# 의 개수 m과 새롭게 추가할 개수 j가 합쳐져서
			# 전체 n개(index n - 1)를 넘어가면 안된다.
			# 범위를 체크하고, 부모노드가 틀리거나 없는 경우 확인
			if (m + j >= n or parent[order[m + j]] != x):
				return 0

			# 순서대로 넣어주기
			q.append(order[m + j])
			check[order[m + j]] = True
		m += cnt
		
	return 1
	
print(solution())
