#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next==None) :
            return head
        p = head.next
        head.next = None
        r = head
        while p!=None:
            if r.val==p.val:
                p = p.next
            else:
                r.next = p
                r = p
                p = p.next
                r.next = None
        return head

