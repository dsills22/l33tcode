# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
    	return self.cloneGraphHelper(node, {})

    def cloneGraphHelper(self, node, visited):
    	if node != None:
    		if node.label in visited:
    			return visited[node.label]

    		clone = UndirectedGraphNode(node.label)
    		visited[node.label] = clone
    		for c in node.neighbors:
    			clone.neighbors.append(self.cloneGraphHelper(c, visited))
    		return clone
    	else:
    		return None

    def printGraph(self, node):
    	self.printGraphHelper(node, {}, 0)

    def printGraphHelper(self, node, visited, depth):
    	if node != None:
    		tabs = "\t" * depth
    		if node.label in visited:
    			print(tabs + str(node.label))
    			return None

    		print(tabs + str(node.label))
    		visited[node.label] = clone
    		for c in node.neighbors:
    			self.printGraphHelper(c, visited, depth + 1)
    		return None

sol = Solution()

# node1 = UndirectedGraphNode(1)
# node2 = UndirectedGraphNode(2)
# node3 = UndirectedGraphNode(3)

# node1.neighbors = [node2, node3]
# node2.neighbors = [node1, node2]
# node3.neighbors = [node1, node2, node3]

# clone = sol.cloneGraph(node1)
# sol.printGraph(clone)



# node1 = UndirectedGraphNode(0)

# node1.neighbors = [node1, node1, node1]

# clone = sol.cloneGraph(node1)
# sol.printGraph(clone)


node1 = UndirectedGraphNode(0)
node2 = UndirectedGraphNode(1)
node3 = UndirectedGraphNode(2)

node1.neighbors = [node1, node1, node1]
node2.neighbors = [node1, node1, node1]
node3.neighbors = [node1, node1, node1]

clone = sol.cloneGraph(node1)
sol.printGraph(clone)

