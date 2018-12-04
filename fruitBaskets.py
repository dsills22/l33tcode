
class Solution:
	def totalFruit(self, arr):
		left = 0
		right = 0
		basket1Count = 0
		basket2Count = 0
		basket1Type = None
		basket2Type = None
		totalCount = 0
		for right in range(0, len(arr)):
			val = arr[right]
			if basket1Type == None:
				basket1Type = val
				basket1Count = 1
			elif basket1Type == val:
				basket1Count = basket1Count + 1
			elif basket2Type == None:
				basket2Type = val
				basket2Count = 1
			elif basket2Type == val:
				basket2Count = basket2Count + 1
			else:
				keepLooping = True
				while keepLooping:
					leftVal = arr[left]

					if leftVal == basket1Type:
						basket1Count = basket1Count - 1
						if basket1Count == 0:
							basket1Type = val
							basket1Count = 1
							keepLooping = False
					elif leftVal == basket2Type:
						basket2Count = basket2Count - 1
						if basket2Count == 0:
							basket2Type = val
							basket2Count = 1
							keepLooping = False

					left = left + 1

			totalCount = max(totalCount, basket1Count + basket2Count)

		return totalCount

sol = Solution()
print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
print(sol.totalFruit([1,2,3,2,2]))
print(sol.totalFruit([0,1,2,2]))
print(sol.totalFruit([1,2,1]))
print(sol.totalFruit([]))
print(sol.totalFruit([0]))
print(sol.totalFruit([0,0]))
print(sol.totalFruit([0,1]))
print(sol.totalFruit([0,1,2]))
print(sol.totalFruit([0,0,1,1]))

