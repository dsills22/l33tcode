class Solution:
	def myAtoi(self, intStr):
		val = 0
		MAX_INT = 2 ** 31 - 1
		MIN_INT = -1 * 2 ** 31
		sign = 1
		i = 0
		arr = []
		for c in intStr:
			if i == 0 and c == ' ':
				continue

			if i == 0 and c == '-':
				sign = -1
			elif i == 0 and c == '+':
				sign = 1
			else:
				if ord(c) >= 48 and ord(c) <= 57:
					arr = [ord(c) - 48] + arr
				else:
					break

			i = i + 1

		l = len(arr)
		i = 0
		for a in arr:
			val = val + a * 10 ** i
			i = i + 1

		if val > MAX_INT and sign == 1:
			return MAX_INT
		elif val > MAX_INT and sign == -1:
			return MIN_INT
		else:
			return sign * val


sol = Solution()
print(sol.myAtoi("42"))
print(sol.myAtoi("          42"))
print(sol.myAtoi("          42kdhjaksjdhkjashdk"))
print(sol.myAtoi("          42 1"))
print(sol.myAtoi("          -42 1"))
print(sol.myAtoi("          - 42 1"))
print(sol.myAtoi("          42asdsadasd1234"))
print(sol.myAtoi("          4938274982374982379487239847239842asdsadasd1234"))
print(sol.myAtoi("          -4938274982374982379487239847239842asdsadasd1234"))
print(sol.myAtoi("ashkjahfj123"))
print(sol.myAtoi("2147483648"))
print(sol.myAtoi("-91283472332"))



