def solution():
	n = int(input())
	check = [False]*(50*20+1)
	for i in range(n+1):
	    for j in range(n-i+1):
	        for k in range(n-i-j+1):
	            l = n-i-j-k
	            val = i+5*j+10*k+50*l
	            check[val] = True
	ans = 0
	for i in range(1, 50*20+1):
	    if check[i]:
	        ans += 1
	return ans

print(solution())
