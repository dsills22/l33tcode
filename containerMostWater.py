#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such 
#that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#Note: You may not slant the container and n is at least 2.

class Solution:
	def maxArea(self, height):
		left = 0
		right = len(height) - 1
		maxVol = 0

		while left < right:
			leftHeight = height[left]
			rightHeight = height[right]
			maxVol = max(maxVol, min(leftHeight, rightHeight) * (right - left))
			if leftHeight > rightHeight:
				right = right - 1
			elif leftHeight <= rightHeight:
				left = left + 1

		return maxVol

sol = Solution()
print(sol.maxArea([1, 1]))
print(sol.maxArea([0, 1]))
print(sol.maxArea([0, 0]))
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,8,6,2,5,4,8,3,8]))
print(sol.maxArea([1,8,6,2,5,4,8,3,8,110,9,10,12,1,15,56]))


