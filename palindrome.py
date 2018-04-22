import math
import re, string

class Solution:
	def isPalindrome(self, s):
		s = re.sub(r'\W+', '', s).lower()
		n = len(s)

		if n <= 1:
			return True

		mid = math.floor(n / 2)
		p1 = s[0:mid] #not inclusive

		if n % 2 == 1: #odd
			mid = mid + 1

		p2 = (s[mid:n])[::-1]

		return p1 == p2

sol = Solution()
print(sol.isPalindrome(""))
print(sol.isPalindrome("a"))
print(sol.isPalindrome("abba"))
print(sol.isPalindrome("aca"))
print(sol.isPalindrome("amanaplanacanalpanama"))
print(sol.isPalindrome("A man, A plan, A Canal, Panama"))
print(sol.isPalindrome("A man "))
print(sol.isPalindrome("sdihfdhkf"))
print(sol.isPalindrome("ab"))

