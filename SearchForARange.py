class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        mid = (end-start)/2
        while start<=end:
        	if nums[mid]<target:
        		start = mid+1
        		mid = start+(end-start)/2
        	elif nums[mid]>target:
        		end = mid-1
        		mid = start+(end-start)/2
        	else:
        		break
        if nums[mid]==target:
        	start = mid
        	end = mid
        	while start-1>=0 and nums[start-1]==target:
        		start -= 1
        	while end+1<= len(nums)-1 and nums[end+1]==target:
        		end += 1
        	return [start,end]
        else:
        	return [-1,-1]
