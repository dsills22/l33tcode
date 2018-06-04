#Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
class Solution:
	def validPalindrome(self, s):
		first = 0
		last = len(s) - 1
		deleted = 0
		while first <= last:
			if s[first] == s[last]:
				first = first + 1
				last = last - 1
			else:
				if first < last - 1 and s[first + 1] == s[last] and s[first] == s[last - 1]:
					if first + 1 < last - 1 and s[first + 2] == s[last - 1]:
						deleted = deleted + 1
						first = first + 2
						last = last - 1
					elif first < last - 2 and s[first + 1] == s[last - 2]:
						deleted = deleted + 1
						first = first + 1
						last = last - 2
					else:
						return False
				elif first < last and s[first + 1] == s[last]:
					deleted = deleted + 1
					first = first + 2
					last = last - 1
				elif first < last - 1 and s[first] == s[last - 1]:
					deleted = deleted + 1
					first = first + 1
					last = last - 2
				else:
					return False

			if deleted > 1:
				return False
		return True

sol = Solution()
print(sol.validPalindrome("abab"))
print(sol.validPalindrome("ababa"))
print(sol.validPalindrome("aaa"))
print(sol.validPalindrome("a"))
print(sol.validPalindrome("ab"))
print(sol.validPalindrome("abb"))
print(sol.validPalindrome("aab"))
print(sol.validPalindrome("abc"))
print(sol.validPalindrome("aabdeenddbaagbddeedbaa"))
print(sol.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
#gmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmg
#cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu

