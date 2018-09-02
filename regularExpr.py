#regular expression matching, support for * and . 

class Solution2(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if len(pattern) - j is 0:
                return len(text) - i is 0
            first_match = len(text) - i > 0 and pattern[j] in { text[i], '.' }
            if len(pattern) - j > 1 and pattern[j+1] == '*':
                result = (first_match and dp(i+1, j)) or dp(i, j+2)
            else:
                result = first_match and dp(i+1, j+1)
            memo[i, j] = result
            return result
        return dp(0, 0)

class Solution:
	def isStr(self, s):
		return s != "*" and s != "." and s != None

	def get(self, arr, index):
		if len(arr) > index:
			return arr[index]
		else:
			return None

	def match(self, SP, sI, pI, DB):
		#print(self.get(s, sI), self.get(p, pI), sI, pI)
		if sI * 100 + pI in DB:
			return False

		if self.get(SP["p"], pI) == None and self.get(SP["s"], sI) != None:
			DB[sI * 100 + pI] = False
			return False
		elif self.get(SP["p"], pI) == None:
			return True
		elif self.get(SP["p"], pI + 1) == "*":
			c = SP["p"][pI]
			pI = pI + 2
			if self.match(SP, sI, pI, DB):
				return True
			else:
				while sI < len(SP["s"]) and (SP["s"][sI] == c or c == "."):
					sI = sI + 1
					if self.match(SP, sI, pI, DB):
						return True
				DB[sI * 100 + pI] = False
				return False
		elif self.get(SP["s"], sI) != None and (self.get(SP["p"], pI) == "." or self.get(SP["p"], pI) == self.get(SP["s"], sI)):
			return self.match(SP, sI + 1, pI + 1, DB)
		else:
			DB[sI * 100 + pI] = False
			return False

	def isMatch(self, s, p):
		if p == "":
			return s == p
		if len(p) == 1:
			return (p == "." and len(s) == 1) or p == s
		return self.match({"s": s, "p": p}, 0, 0, {})

sol = Solution2()
print(sol.isMatch("aaa", "aaa"), True)
print(sol.isMatch("aaa", "a.*"), True)
print(sol.isMatch("aaa", "a.*b"), False)
print(sol.isMatch("aaa", "a.*.*.*.*a"), True)
print(sol.isMatch("aaa", "a.*.*.*.*.*.*aaa"), False)
print(sol.isMatch("aaa", "a.*aa"), True)
print(sol.isMatch("aaa", "a.*a"), True)
print(sol.isMatch("mississippi", "mis*is*p*."), False)
print(sol.isMatch("aa", "a*"), True)
print(sol.isMatch("ab", ".*"), True)
print(sol.isMatch("aab", "c*a*b"), True)

print(sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"), False)
