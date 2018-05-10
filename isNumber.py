import re

class Solution(object):
	def isInt(self, s):
		return bool(re.match('^[+-]{0,1}\d+$', s))
	
	def isNumber(self, s):
		if s == None:
			return False

		s = s.strip()

		if len(s) == 0:
			return False

		if 'e' in s:
			parts = s.split('e')
			if len(parts) != 2:
				return False
			if len(parts[0].rstrip()) != len(parts[0]):
				return False
			return self.isNumber(parts[0]) and self.isInt(parts[1])

		return bool(re.search('\d', s)) and bool(re.match('^[+-]{0,1}\d*\.{0,1}\d*$', s))

sol = Solution()
print(sol.isNumber('0'))
print(sol.isNumber(' 0.1 '))
print(sol.isNumber('abc'))
print(sol.isNumber('1 a'))
print(sol.isNumber('2e10'))
print(sol.isNumber(' -.'))
print(sol.isNumber('+1'))
print(sol.isNumber('-2'))
print(sol.isNumber('2 e10'))

