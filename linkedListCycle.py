#LinkedList cycle

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x, nextNode=None):
		self.val = x
		self.next = nextNode

class Solution(object):
	def hasCycle(self, head):
		if head == None:
			return False
		explored = {}
		while head.next != None:
			explored[head] = True
			if head.next in explored:
				return True
			head = head.next
		return False

sol = Solution()
print(sol.hasCycle(ListNode(1, ListNode(1, ListNode(1)))))
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node2
print(sol.hasCycle(node1))
