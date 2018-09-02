#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

#Example 1:
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

#Example 2:
#Input: "cbbd"
#Output: "bb"

#binary search in len for the answer

class Solution(object):
	def getIsPalindrome(self, s, left, right):
		while right > left and s[left] == s[right]:
			left = left + 1
			right = right - 1
		return right <= left

	def findPalindromeOfSize(self, s, size):
		l = len(s)
		if size > l:
			return None

		for i in range(0, l - size + 1):
			left = i
			right = i + size - 1
			while right > left and s[left] == s[right]:
				left = left + 1
				right = right - 1
			if right <= left:
				return i
		return None

	def longestPalindrome(self, s):
		#for i in range(len(s) - 1, 0, -1):
		#	pal = self.findPalindromeOfSize(s, i + 1)
		#	if pal != None:
		#		return pal
		#return ""

		pal = None
		maxPalI = None
		maxPalSize = None
		maxLen = len(s)
		curr = maxLen
		hi = maxLen
		lo = 0
		while lo < curr:
			pal = self.findPalindromeOfSize(s, curr)
			if pal == None:
				pal = self.findPalindromeOfSize(s, curr + 1)
				if pal == None:
					hi = curr
				else:
					curr = curr + 1
					while pal - 1 >= 0 and pal + curr < maxLen and s[pal - 1] == s[pal + curr]:
						pal = pal - 1
						curr = curr + 2

					maxPalI = pal
					maxPalSize = curr
					lo = curr
				curr = int((lo + hi) / 2)
			else:
				while pal - 1 >= 0 and pal + curr < maxLen and s[pal - 1] == s[pal + curr]:
					pal = pal - 1
					curr = curr + 2

				maxPalI = pal
				maxPalSize = curr
				lo = curr
				curr = int((lo + hi) / 2)
		if maxPalI == None:
			return ""
		else:
			return s[maxPalI : maxPalI + maxPalSize]


sol = Solution()
#print(sol.longestPalindrome("babad"))
#print(sol.longestPalindrome("cbbd"))
#print(sol.longestPalindrome(""))
#print(sol.longestPalindrome("abb"))

inputVal = "akjhfshfjkdshkflydfhrkjwhfiuqyfihsdkjfhdkjsfhdkjqweewqfhkdsfkdhfkjsdhfkhkdfjpopyuioppoiuyffvvvffhdsbgjhwfihfkjshdkfahskfherjhgfiweyfhidhskfcgasyfiwehdksjfhcaskdfoewfhkasgjfghfkasdfkjsdhfkjhdskjfhsdkghiuerygiuwrhsdjfhiulewyrfohrwsdjhfbceuwysdkfhleiwjsdngvbhjsdfgiwuehsdfb42ir835tyfuyweghdsbvnwoijehf79wyrtgfu4ewbdskjhvewijgiuerfisdfkheraghjedshfwgkjhrfdkgqwertyuiopqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqhsdygfiuyghkjhfbsdfjh,iltugorwieghkjsdbfkutuo4reujhguvhbsdjfhvefkjdgnvbds,fkuwrueogjnerjksdfbhlieuwhfgkjdhgkjfdkgjhdfkjghrtyghiuerthfdgiueryg84y589erghkjdfgbhjkfheligioreug89yiugh5otgjhiueryf8oertuyghirlkfhirkjsdgnelrifhjb508yg7erughkgkhjklgfjiodfugyuigyfiugydifug"
newInput = ""
for i in range(0, 1600):
	newInput = newInput + inputVal
print(sol.longestPalindrome(newInput))

#print(sol.longestPalindrome("kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"))

