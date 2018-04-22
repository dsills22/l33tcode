
class Solution(object):
	def treeToDoublyList(self, root):
		stack = []
		stack.append(root)
		while len(stack) > 0:
			node = self.peek(stack)
			if node.left:
				stack.append(node.left)
			# in order traversal
			# 