#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

class Solution:
	def trap(self, height):
		maxH = -1
		maxInd = 0
		i = 0
		l = len(height)
		water = 0
		while i < l:
			h = height[i]
			if h >= maxH:
				maxH = h
				maxInd = i
			betweenBlocks = 0
			dist = 0
			while i + 1 < l and height[i + 1] < h:
				betweenBlocks = betweenBlocks + height[i + 1]
				i = i + 1
				dist = dist + 1
			if i + 1 < l:
				barrier = height[i + 1]
				water = water + (min([h, barrier]) * dist) - betweenBlocks
			i = i + 1

		i = l - 1
		while i > maxInd:
			h = height[i]
			betweenBlocks = 0
			dist = 0
			while i - 1 > 0 and i > maxInd and height[i - 1] < h:
				betweenBlocks = betweenBlocks + height[i - 1]
				i = i - 1
				dist = dist + 1
			barrier = height[i - 1]
			water = water + (min([h, barrier]) * dist) - betweenBlocks
			i = i - 1

		return water


sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([]))
print(sol.trap([0]))
print(sol.trap([10, 0, 0, 0, 10]))
print(sol.trap([10, 0, 0, 0, 10, 0, 0, 0, 10]))
print(sol.trap([0, 1, 0, 0, 0, 3, 1, 2, 0, 1, 2, 0, 3, 5, 4, 3, 2, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0]))




