#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#Your algorithm should run in O(n) complexity.
#Example:
#	Input: [100, 4, 200, 1, 3, 2]
#	Input: [100, 200, 1, 3, 2, 4, 0]
#	Output: 4
#	Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution(object):
	def longestConsecutive(self, nums):
		graph = {}
		visited = {}
		ans = 0
		for n in nums:
			if n not in graph:
				graph[n] = {"left": None, "right": None, "num": n}
				if n - 1 in graph:
					graph[n]["left"] = graph[n - 1]
					graph[n - 1]["right"] = graph[n]
				if n + 1 in graph:
					graph[n]["right"] = graph[n + 1]
					graph[n + 1]["left"] = graph[n]

		for n in nums:
			if n not in visited:
				stack = [graph[n]]
				count = 0
				while len(stack) > 0:
					node = stack.pop()
					visited[node["num"]] = True
					if node["left"] != None and node["left"]["num"] not in visited:
						stack.append(node["left"])
					if node["right"] != None and node["right"]["num"] not in visited:
						stack.append(node["right"])
					count = count + 1
				if count > ans:
					ans = count
		return ans

sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([100, 200, 1, 3, 2, 4]))
print(sol.longestConsecutive([100, 200, 1, 3, 2, 4, 0]))
print(sol.longestConsecutive([0]))
print(sol.longestConsecutive([]))
