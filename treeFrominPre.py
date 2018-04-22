# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def printTree(self, tree, level=0, prefix="root: "):
		if tree:
			print(("\t" * level) + prefix + str(tree.val))
			tree.printTree(tree.left, level + 1, "left child: ")
			tree.printTree(tree.right, level + 1, "right child: ")

#preorder = [3,9,20,15,7]
#inorder =  [9,3,15,20,7]

class Solution(object):
    def buildTree(self, preorder, inorder):
    	inOrderHash = {}
    	for i, val in enumerate(inorder):
    		inOrderHash[val] = i

    	if len(preorder) == 0:
    		return None
    	else:
    		tree = TreeNode(preorder[0])
    		leftStack = [tree]
    		rightStack = [tree]

    		for i in range(1, len(preorder)):
    			currPreVal = preorder[i]
    			currPosn = inOrderHash[currPreVal]

    			leftParent = leftStack.pop()
    			leftParentPosn = inOrderHash[leftParent.val]

    			if currPosn < leftParentPosn:
    				leftParent.left = TreeNode(currPreVal)
    				leftStack.append(leftParent.left)
    				#rightStack.append(leftParent.left)
    				rightStack.append(leftParent)
    			else:
    				rightStack.append(leftParent)

    				#print("stack")
    				#for s in rightStack:
    				#	print(s.val, inOrderHash[s.val], currPosn)

    				while len(rightStack) > 0 and currPosn > inOrderHash[rightStack[len(rightStack) - 1].val]:
    					rightParent = rightStack.pop()
    					rightParentPosn = inOrderHash[rightParent.val]
    				#print(rightParent.val)
    				rightParent.right = TreeNode(currPreVal)
    				leftStack.append(rightParent.right)
    				rightStack.append(rightParent.right)

    		return tree

sol = Solution()

tree = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
tree.printTree(tree)

tree = sol.buildTree([3,5,8,9,1,7,2], [2,7,1,9,8,5,3])
tree.printTree(tree)

tree = sol.buildTree([2,7,1,9,8,5,3], [3,5,8,9,1,7,2])
tree.printTree(tree)

tree = sol.buildTree([2,7,1,9,8,5,3], [2,7,1,9,8,5,3])
tree.printTree(tree)

tree = sol.buildTree([1,2,3], [2,3,1])
tree.printTree(tree)

tree = sol.buildTree([1,2,3,4], [3,2,1,4])
tree.printTree(tree)

tree = sol.buildTree([4,2,1,3], [1,2,3,4])
tree.printTree(tree)




