#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Ex:
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

#Definition for singly-linked list.
#Comment out before submitting to leetcode!
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		return str(self.__dict__)

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		sumRoot = ListNode(0)
		sumll = sumRoot
		carry = 0

		while l1 != None:
			l2Val = 0
			if l2 != None:
				l2Val = l2.val
				l2 = l2.next

			x = l1.val + l2Val + carry

			if x >= 10:
				x = x - 10
				carry = 1
			else:
				carry = 0

			sumll.val = x
			l1 = l1.next
			if l1 != None:
				sumll.next = ListNode(0)
				sumll = sumll.next
		
		while l2 != None:
			sumll.next = ListNode(0)
			sumll = sumll.next
			x = l2.val + carry
			if x >= 10:
				x = x - 10
				carry = 1
			else:
				carry = 0

			sumll.val = x
			l2 = l2.next

		if carry == 1:
			sumll.next = ListNode(0)
			sumll = sumll.next
			sumll.val = carry

		return sumRoot

sol = Solution()
l1 = ListNode(4)
l2 = ListNode(7)
print(sol.addTwoNumbers(l1, l2))

l1.next = ListNode(3)
print(sol.addTwoNumbers(l1, l2))

l2.next = ListNode(8)
print(sol.addTwoNumbers(l1, l2))

l2.next = ListNode(3)
print(sol.addTwoNumbers(l1, l2))

l2.next.next = ListNode(7)
print(sol.addTwoNumbers(l1, l2))
