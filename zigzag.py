class Solution(object):
	def convert(self, s, numRows):
		rows = []
		for i in range(0, numRows):
			rows.append("")
		
		i = 0
		goingDown = True

		for c in s:
			rows[i] = rows[i] + c
			
			if i >= numRows - 1:
				goingDown = False

			if i == 0:
				goingDown = True

			if goingDown:
				i = min(i + 1, numRows - 1)
			else:
				i = max(i - 1, 0)

		ret = ""
		for r in rows:
			ret = ret + r
		return ret

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
## CORRECT: PAHNAPLSIIGYIR
###       : PAHNAPLSIIGYIR

print(sol.convert("PAYPALISHIRING", 4))
## CORRECT: PINALSIGYAHRPI
###       : PINALSIGYAHRPI

print(sol.convert("AB", 1))