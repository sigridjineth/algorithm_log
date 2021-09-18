n = int(input())
a = list(map(int, input().split()))
c = [False] * (n * 100000)

def go(index, sum):
	if (index == n):
		print(sum)
		c[sum] = True
		return
	go(index + 1, sum + a[index])
	go(index + 1, sum)
	
go(0, 0)
i = 1

while True:
	if (c[i] == False):
		break
	i += 1
	
print(i)
