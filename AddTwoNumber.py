# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        headnode = ListNode(0)
	headnode.next = None
	p = headnode
	carry = 0
	while (l1 and l2):
		if ((l1.val+l2.val+carry)<10):
			newnode = ListNode(l1.val+l2.val+carry)
			newnode.next = None
			p.next = newnode
			p = p.next
			l1 = l1.next
			l2 = l2.next
			carry = 0
		else:
			newnode = ListNode(l1.val+l2.val+carry-10)
			newnode.next = None
			p.next = newnode
			p = p.next
			carry = 1
			l1 = l1.next
			l2 = l2.next
	if(l1):
		while (l1):
			if ((l1.val+carry)<10):
				newnode = ListNode(l1.val+carry)
				newnode.next = None
				p.next = newnode
				p = p.next
				l1 = l1.next
				carry = 0
			else:
				newnode = ListNode(l1.val+carry-10)
				newnode.next = None
				p.next = newnode
				p = p.next
				l1 = l1.next
				carry = 1
		if(carry):
			newnode = ListNode(carry)
			newnode.next = None
			p.next = newnode
	if(l2):
		while (l2):
			if ((l2.val+carry)<10):
				newnode = ListNode(l2.val+carry)
				newnode.next = None
				p.next = newnode
				p = p.next
				l2 = l2.next
				carry = 0
			else:
				newnode = ListNode(l2.val+carry-10)
				newnode.next = None
				p.next = newnode
				p = p.next
				l2 = l2.next
				carry = 1
		if(carry):
			newnode = ListNode(carry)
			newnode.next = None
			p.next = newnode
			
	if(carry):
			newnode = ListNode(carry)
			newnode.next = None
			p.next = newnode
	return headnode.next