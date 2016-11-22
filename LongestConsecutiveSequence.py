class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        used = dict.fromkeys(nums,0)
        print used
        longest = 0
        temp_log = 0
        length = 0
        for i in xrange(0,len(nums)):
            if(used[nums[i]]!=1):
                length = 1
                temp_log = 1
                used[nums[i]]=1
                while (nums[i]+length in nums and used[(nums[i]+length)]==0):
                   # length+=1
                    #if nums[i]+length in nums:
                    used[(nums[i]+length)] = 1
                    temp_log += 1
                    length += 1
                    #if nums[i]-length in nums:
                length = 1
                while (nums[i]-length in nums and used[(nums[i]-length)]==0):
                    used[(nums[i]-length)] = 1
                    temp_log += 1
                    length += 1
                longest = max(temp_log,longest)
        return longest