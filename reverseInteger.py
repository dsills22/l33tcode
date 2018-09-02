import math

class Solution(object):
	def reverse(self, x):
		if x == 0:
			return 0
		ret = 0
		power = int(math.log(abs(x), 10))
		for p in range(0, power + 1):
			powerI = 10 ** (power - p)
			num = int(x / powerI)

			if abs(ret) >= 147483648 and (power - p > 0 or (abs(num) > 2 or (abs(ret) > 147483648 and abs(num) >= 2))):
				return 0

			ret += num * 10 ** p
			x -= num * powerI
		return ret

sol = Solution()
print(sol.reverse(12345))
print(sol.reverse(-123))
print(sol.reverse(10))
print(sol.reverse(1))
print(sol.reverse(0))
print(sol.reverse(100))
print(sol.reverse(1001))
print(sol.reverse(18874500))
print(sol.reverse(-12))
print(sol.reverse(-18874500))
print(sol.reverse(2147483648))
print(sol.reverse(-2147483648))
print(sol.reverse(8463847412))
print(sol.reverse(8463847413))
print(sol.reverse(8463847422))
