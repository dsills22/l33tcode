# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution(object):
	def copyRandomList(self, head):
		if head == None:
			return None

		sourceHash = {}
		targetHash = {}
		retHead = RandomListNode(head.label)
		retCurr = retHead
		targetHead = head

		i = 0
		sourceHash[head] = i
		targetHash[i] = retCurr

		while head.next != None:
			i = i + 1
			head = head.next
			sourceHash[head] = i

			retCurr.next = RandomListNode(head.label)
			retCurr = retCurr.next
			targetHash[i] = retCurr

		head = targetHead
		retCurr = retHead
		if head.random != None:
			retCurr.random = targetHash[sourceHash[head.random]]

		while head.next != None:
			head = head.next
			retCurr = retCurr.next
			if head.random != None:
				retCurr.random = targetHash[sourceHash[head.random]]

		return retHead

sol = Solution()

rll = RandomListNode("q")
rll.next = RandomListNode("w")
rll.next.next = RandomListNode("e")
rll.next.next.next = RandomListNode("r")

rll.next.random = rll.next.next.next
rll.next.next.next.random = rll.next
rll.random = rll

copy = sol.copyRandomList(rll)
print(copy.label)
print("RANDOM: " + (copy.random and copy.random.label or ""))
while copy.next != None:
	copy = copy.next
	print(copy.label)
	print("RANDOM: " + (copy.random and copy.random.label or ""))