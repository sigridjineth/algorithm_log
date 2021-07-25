def solution():
	N, M = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]
	
	up = N * M
	
	left = 0
	for i in range(N):
	    for j in range(M):
	        if j == 0:
	            left += arr[i][j]
	        else:
	            if arr[i][j-1] < arr[i][j]:
	                left += arr[i][j] - arr[i][j-1]
	
	front = 0
	for j in range(M):
	    for i in range(N):
	        if i == 0:
	            front += arr[i][j]
	        else:
	            if arr[i-1][j] < arr[i][j]:
	                front += arr[i][j] - arr[i-1][j]
	        
	answer = 2 * (up + left + front)
	print(answer)

solution()
