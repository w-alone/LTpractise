# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next==None) :
            return head

        temp = ListNode(1)
        p = head
        r = temp
        while p!=None:
            if p.next==None or p.next.val!=p.val:
                    r.next = p
                    r = p
                    p = p.next
                    r.next = None
            else:
                while p.val==p.next.val:
                    p = p.next
                    if(p.next==None):
                        break
                p = p.next
        return temp.next

        