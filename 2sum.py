class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x1 in xrange(0,len(nums)):
            for x2 in xrange(x1+1,len(nums)):
                if(nums[x1]+nums[x2] == target):
                    return x1+1,x2+1
        