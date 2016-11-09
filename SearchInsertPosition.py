class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        mid = (end-start)/2
        while start<end:
            if nums[mid]<target:
                start = mid+1
                mid = start+(end-start)/2
            elif nums[mid]>target:
                end = mid-1
                #mid = start+(end-start)/2
                if(end <= 0):
                    mid = 0
                    break
                mid = start+(end-start)/2
            else:
                break
        if nums[mid]==target:
            return mid
        else:
            if nums[mid]<target:
                return mid+1
            elif nums[mid] > target and mid == 0:
                return 0
            else:
                return mid
