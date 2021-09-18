n, m = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

def go(index, sum):
	global answer
	if (i == n):
		if (s == m):
			answer += 1
		return
	go(i + 1, sum + a[index])
	go(i + 1, sum)

go(0, 0)

if (m == 0):
	answer -= 1
	
print(answer)
