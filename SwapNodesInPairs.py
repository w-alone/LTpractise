# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next==None):
            return head
        t = head
        p = head
        q = p.next
        r = q
        while p!=None and q!=None:
            if t.next != r:
                t.next = q
            p.next = q.next
            q.next = p
            t = p
            p = p.next
            if p==None or p.next==None:
                break
            q = p.next
        return r
