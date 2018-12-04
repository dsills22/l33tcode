#Integer to English

class Solution:
	def numberToWords(self, num):
		numStr = str(num)
		length = len(numStr)
		i = 0

		if num <= 20:
			return self.baseWord(numStr)

		result = ""
		commas = 0
		commaStack = []

		while length > 0:			
			if commas >= 1:
				commaStack.append(self.baseWord(str(10 ** (commas * 3))) + " ")

			curr = ""
			if length >= 3:
				i = i - 3
				currentThree = numStr[i : length]
				curr = self.sizeThree(currentThree)
				commas = commas + 1
				length = length - 3
			elif length >= 2:
				i = i - 2
				currentTwo = numStr[i : length]
				curr = self.sizeTwo(currentTwo)
				length = length - 2
			else:
				i = i - 1
				curr = self.sizeOne(numStr[0])
				length = length - 1

			commaStr = " "
			if curr != "":
				if len(commaStack) > 0:
					commaStr = commaStack.pop()
				result = curr + commaStr + result

		return result.strip()

	def sizeThree(self, numStr):
		num = int(numStr)
		numStr = str(num)
		if len(numStr) <= 2:
			return self.sizeTwo(numStr)
		elif num > 0:
			return self.sizeOne(numStr[0]) + self.sizeOne("100") + self.sizeTwo(numStr[1:3])
		else:
			return ""

	def sizeTwo(self, numStr):
		num = int(numStr)
		numStr = str(num)
		if (numStr.endswith("0") or num <= 20) and num > 0:
			return self.sizeOne(numStr)
		elif num > 0:
			return self.sizeOne(str(int(numStr[0]) * 10)) + self.sizeOne(numStr[1])
		else:
			return ""

	def sizeOne(self, numStr):
		return self.baseWord(numStr) + " "

	def baseWord(self, num):
		if num == "0":
			return "Zero"
		if num == "1":
			return "One"
		if num == "2":
			return "Two"
		if num == "3":
			return "Three"
		if num == "4":
			return "Four"
		if num == "5":
			return "Five"
		if num == "6":
			return "Six"
		if num == "7":
			return "Seven"
		if num == "8":
			return "Eight"
		if num == "9":
			return "Nine"
		if num == "10":
			return "Ten"
		if num == "11":
			return "Eleven"
		if num == "12":
			return "Twelve"
		if num == "13":
			return "Thirteen"
		if num == "14":
			return "Fourteen"
		if num == "15":
			return "Fifteen"
		if num == "16":
			return "Sixteen"
		if num == "17":
			return "Seventeen"
		if num == "18":
			return "Eighteen"
		if num == "19":
			return "Nineteen"
		if num == "20":
			return "Twenty"
		if num == "30":
			return "Thirty"
		if num == "40":
			return "Forty"
		if num == "50":
			return "Fifty"
		if num == "60":
			return "Sixty"
		if num == "70":
			return "Seventy"
		if num == "80":
			return "Eighty"
		if num == "90":
			return "Ninety"
		if num == "100":
			return "Hundred"
		if num == "1000":
			return "Thousand"
		if num == "1000000":
			return "Million"
		if num == "1000000000":
			return "Billion"
		return ""


sol = Solution()
print(sol.numberToWords(0))
print(sol.numberToWords(1))
print(sol.numberToWords(19))
print(sol.numberToWords(20))
print(sol.numberToWords(21))
print(sol.numberToWords(32))
print(sol.numberToWords(55))
print(sol.numberToWords(155))
print(sol.numberToWords(155000))
print(sol.numberToWords(155000000))
print(sol.numberToWords(155300000))
print(sol.numberToWords(155000001))
print(sol.numberToWords((2 ** 31) - 1))
print(sol.numberToWords(11045))
print(sol.numberToWords(30))
print(sol.numberToWords(40))
print(sol.numberToWords(50))
print(sol.numberToWords(300))
print(sol.numberToWords(3000))
print(sol.numberToWords(30000))
print(sol.numberToWords(10000000))







