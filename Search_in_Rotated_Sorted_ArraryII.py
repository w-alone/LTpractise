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

        class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head , tail = 0,len(nums)-1
        # while nums[tail]==nums[head]:
        #     tail -= 1
        #     print tail
        middle = head + tail >> 1
        while head <= tail:
            if(target == nums[middle]):
                return True

            #elif(target < nums[middle] and (nums[middle] > nums[head] or nums[middle] == nums[head] != nums[tail])):               
            elif(target < nums[middle] and nums[middle] > nums[head] ):               

                if(target < nums[head]):
                    head = middle + 1
                else:
                    tail = middle-1

            elif(target < nums[middle]):
                if(nums[middle]==nums[head]) :
                    head = head+1
                else:
                    tail = middle-1

            #elif(target > nums[middle] and (nums[middle] < nums[head] or nums[middle] == nums[head] == nums[tail])):
            elif(target > nums[middle] and nums[middle] < nums[head] ):
                if(target < nums[head]):
                    head = middle+1
                else:
                    tail = middle-1

            else:
                if(nums[middle]==nums[tail]) :
                    tail = tail-1
                else:
                    head = middle+1
            #print head , tail
            middle = head + tail >> 1

        return False

