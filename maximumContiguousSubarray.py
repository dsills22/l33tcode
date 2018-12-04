
class Solution:
	def maxSubArray(self, nums):
		i = 0
		size = len(nums)

		if size <= 0:
			return None

		largest = nums[i]
		while i < size and nums[i] <= 0:
			largest = max(nums[i], largest)
			i = i + 1

		if i == size:
			return largest

		maxVal = 0
		candidateVal = 0
		for i in range(i, size):
			maxVal = max(maxVal, candidateVal)
			if nums[i] >= 0:
				candidateVal = candidateVal + nums[i]
			else:
				subtractVal = candidateVal + nums[i]
				if subtractVal <= 0:
					candidateVal = 0
				else:
					candidateVal = subtractVal

		return max(maxVal, candidateVal)

sol = Solution()
print(sol.maxSubArray([0]))
print(sol.maxSubArray([1, 2, 3, -5, -1, 10]))
print(sol.maxSubArray([1, 2, 3, -5, 4, -1, 10]))
print(sol.maxSubArray([-1, -2, 0, -3, -5, 0, -9, 1, 2, 3, -5, 4, -1, 10]))
print(sol.maxSubArray([1, 2, 3, -5, 0, -1, 10]))
print(sol.maxSubArray([1, 2, 3, -5, 2, -1, 10]))
print(sol.maxSubArray([1, 2, 3, -5, 3, -1, 10]))
