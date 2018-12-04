
class Solution(object):

	def generateAllSubsets(self, nums):
		subsets = []
		for size in xrange(1, len(nums) + 1):
			self.generateSubsetsOfSize(nums, size, 0, [], subsets)
		return subsets

	def generateSubsetsOfSize(self, nums, size, i, acc, subsets):
		if len(acc) == size:
			subsets.append(list(acc))
		elif len(acc) < size:
			for j in xrange(i, len(nums)):
				newAcc = list(acc)
				newAcc.append(nums[j])
				self.generateSubsetsOfSize(nums, size, j + 1, newAcc, subsets)
	
	def maxSubsetLen(self, nums, k):
		subsets = self.generateAllSubsets(nums)
		maxLen = 0
		for s in subsets:
			agg = sum(s)
			if agg == k:
				if maxLen < len(s):
					maxLen = len(s)
		return maxLen

	def maxSubArrayLen(self, nums, k):
		maxLen = 0

		#convert to cumulative sum
		for i in xrange(1, len(nums)):
			nums[i] = nums[i] + nums[i - 1]

		numMap = {}
		#0th entry should be -1 so that i - numMap[nums[i] - k] will add one to the result if nums[i] - k is 0
		#this is bc a value of 0 adds to the length of the array, should not subtract from it
		numMap[0] = -1
		for i in xrange(0, len(nums)):
			#if nums[i] - k is in numMap as a cumulative sum, and we are at nums[i] cumulative sum
			#then nums[i] - (nums[i] - k) = k and we have found a contiguous subarray of size i - j where
			#j is the index of the cumulative sum nums[i] - k.
			if nums[i] - k in numMap:
				maxLen = max(maxLen, i - numMap[nums[i] - k])
			#if the map does not have a cumulative sum added yet, add it
			#note we do not replace if we find duplicates bc we want the left-most (longest) subarray
			if nums[i] not in numMap:
				numMap[nums[i]] = i

		return maxLen

sol = Solution()
print(sol.maxSubArrayLen([1, -1, 5, -2, 3], 3))
print(sol.maxSubArrayLen([2, -1, 2, 1], 1))
