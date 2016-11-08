class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head , tail , middle= 0,len(nums)-1,(0+len(nums)-1)/2
        while head <= tail:
           # if head == tail and target!=nums[head]:
           #     return -1
           # elif head==tail and target == nums[head]:
           #     return head
            if(target == nums[head]):
                return head
            elif(target < nums[head]):
                if nums[head]<nums[tail]:
                    while head<=tail:
                        middle = (head+tail)/2
                        if nums[middle]==target:
                            return middle
                        elif nums[middle]> target:
                            tail = middle-1
                        else:
                            head = middle+1
                middle = (head+tail)/2
                if nums[middle]==target:
                    return middle
                if(nums[middle]<nums[tail] and target<nums[middle]):
                    tail = middle-1
                else:
                    head = middle+1
            else:
                middle = (head+tail)/2
                if nums[head]<=nums[tail]:
                    while head<=tail:
                        middle = (head+tail)/2
                        if nums[middle]==target:
                            return middle
                        elif nums[middle]> target:
                            tail = middle-1
                        else:
                            head = middle+1
                if nums[middle]==target:
                    return middle
                if(nums[middle]>nums[tail] and target>nums[middle]):
                    head = middle+1
                else:
                    tail = middle
        return -1
