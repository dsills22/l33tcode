import math

class Solution:
	def reverse(self, x):
		if x >= -9 and x <= 9:
			return x
		ret = 0
		maxPower = int(math.log(abs(x), 10))
		for i in range(0, maxPower + 1):
			ithPower = 10 ** (maxPower - i)
			ithNum = int(x / ithPower)
			ret = ret + (ithNum * 10 ** i)
			x = x - (ithNum * ithPower)
		return ret

	def isPalindrome(self, x):
		if x < 0:
			return False
		else:
			revX = self.reverse(x)
			return revX == x

sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(0))
print(sol.isPalindrome(10))
print(sol.isPalindrome(101))
print(sol.isPalindrome(12345678900987654321))
