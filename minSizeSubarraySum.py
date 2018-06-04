#Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s. 
#If there isn't one, return 0 instead.

class Solution:
	def minSubArrayLen(self, s, nums):
		sumVal = 0
		minLen = float("inf")
		currLen = 0
		leftPosn = 0
		numsLen = len(nums) - 1
		for n in nums:
			sumVal = sumVal + n
			currLen = currLen + 1
			if sumVal >= s:
				minLen = min(minLen, currLen)
				while(sumVal >= s and leftPosn < numsLen):
					minLen = min(minLen, currLen)
					leftMostNum = nums[leftPosn]
					sumVal = sumVal - leftMostNum
					currLen = currLen - 1
					leftPosn = leftPosn + 1
		if minLen == float("inf"):
			return 0
		else:
			return minLen


sol = Solution()
print(sol.minSubArrayLen(7, [4,3,6,6,8,9,10,6,1,5,2,7,3,2,1,2]))
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
print(sol.minSubArrayLen(3, [8, 9, 7, 6]))
print(sol.minSubArrayLen(11, [1, 2, 3, 4, 5]))
