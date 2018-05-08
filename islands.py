
class Node:
	def __init__(self):
		self.up = None
		self.right = None
		self.down = None
		self.left = None
		self.visited = False

class Solution:
	def hash(self, row, col, offset):
		return (row * offset) + col

	def markVisited(self, node):
		if node != None:
			if not node.visited:
				node.visited = True
				self.markVisited(node.up)
				self.markVisited(node.right)
				self.markVisited(node.down)
				self.markVisited(node.left)

	def makeNode(self):
		return Node()

	def numIslands(self, grid):
		islandCount = 0
		numRows = len(grid)
		if numRows == 0:
			return islandCount
		numCols = len(grid[0])
		if numCols == 0:
			return islandCount
		offset = numRows * numCols
		nodeHash = {}
		for row in xrange(numRows):
			for col in xrange(numCols):
				curr = grid[row][col]
				if curr == '0':
					continue
				else: #curr == 1
					h = self.hash(row, col, offset)
					
					node = None
					if h not in nodeHash:
						node = self.makeNode()
						nodeHash[h] = node
					else:
						node = nodeHash[h]

					if row - 1 >= 0 and grid[row - 1][col] == '1':
						upHash = self.hash(row - 1, col, offset)
						node.up  = nodeHash[upHash]
					if col - 1 >= 0 and grid[row][col - 1] == '1':
						leftHash = self.hash(row, col - 1, offset)
						node.left = nodeHash[leftHash]
					if row + 1 < numRows and grid[row + 1][col] == '1':
						down = self.makeNode()
						downHash = self.hash(row + 1, col, offset)
						nodeHash[downHash] = down
						node.down = down
					if col + 1 < numCols and grid[row][col + 1] == '1':
						rightHash = self.hash(row, col + 1, offset)
						right = None
						if rightHash not in nodeHash:
							right = self.makeNode()
						else:
							right = nodeHash[rightHash]
						nodeHash[rightHash] = right
						node.right = right

		for key in nodeHash:
			node = nodeHash[key]
			if node.visited:
				continue
			else:
				islandCount = islandCount + 1
				self.markVisited(node)

		return islandCount

sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print(sol.numIslands([["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]))
print(sol.numIslands([["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","1"]]))
print(sol.numIslands([["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","1"]]))
print(sol.numIslands([["1","1","1","1","1"],["1","0","0","0","1"],["1","0","0","0","1"],["1","1","1","1","1"]]))
print(sol.numIslands([["1","0","0","0","1"],["1","0","0","0","1"],["1","0","0","0","1"],["1","1","1","1","1"]]))
