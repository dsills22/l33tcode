

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for i, n in enumerate(nums):
        	if n in numMap:
        		numMap[n]["iNum"] = numMap[n]["iNum"] + 1
        		numMap[n]["i"].append(i)
        	else:
        		numMap[n] = {"iNum": 1, "i": [i]}
        for i, n in enumerate(nums):
        	remain = target - n
        	if remain in numMap:
        		if remain != n:
        			return [i, numMap[remain]["i"][0]]
        		elif numMap[remain]["iNum"] > 1:
        			return [numMap[remain]["i"][0], numMap[remain]["i"][1]]

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([0, 2, 2, 2], 4))
print(sol.twoSum([], 4))
print(sol.twoSum([1], 4))
print(sol.twoSum([1,5,6], 4))