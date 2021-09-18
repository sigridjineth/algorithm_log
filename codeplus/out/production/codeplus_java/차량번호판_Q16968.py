def solution_recursive():
	def go(s, index, last):
		if (len(s) == index):
			return 1
		if (s[index] == 'c'):
			start = ord('a')
			end = ord('z')
		else:
			start = ord('0')
			end = ord('9')
		ans = 0
		for i in range(start, end + 1):
			if (i != last):
				ans += go(s, index + 1, i)
		return ans
		
	s = input()
	return go(s, 0, '#')

print(solution_recursive())

def solution_combination():
	s = input()
	ans = 1
	for i in range(len(s)):
		if (s[i] == 'c'):
			cnt = 26
		else:
			cnt = 10
		if (i > 0 and s[i] == s[i - 1]):
			cnt -= 1
		ans = ans * cnt
	return ans

print(solution_combination())
