class Solution:
	def isValid(self, s):
		stack = []
		for c in s:
			if c == "(" or c == "[" or c == "{":
				stack.append(c)
			else:
				if len(stack) == 0:
					return False
				lastChar = stack.pop()
				if lastChar == "(" and c != ")":
					return False
				elif lastChar == "[" and c != "]":
					return False
				elif lastChar == "{" and c != "}":
					return False
		return len(stack) == 0

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()["))
print(sol.isValid("()[]"))
print(sol.isValid("(({})[({})])"))
print(sol.isValid("(()))"))