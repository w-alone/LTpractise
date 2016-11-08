class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        partion = -1
        change = 0
        if len(nums) >= 1:
	        for i in xrange(len(nums)-1,0,-1):
	        	if nums[i]>nums[i-1]:
	        		partion = i-1
	        		break
	        if partion!=-1:
		       	for i in xrange(len(nums)-1,0,-1):
		       		if nums[i]>nums[partion]:
		       			change = i
		       			break
	       		nums[partion],nums[change] = nums[change],nums[partion]
	       	#value = nums[len(nums)-1]
	       	print partion
	       	#sort from partion+1 -> len(num)-1
	       	times = len(nums)-partion-1 >> 1

	       	for i in xrange(0,times):
	       		nums[partion+1+i],nums[len(nums)-1-i] = nums[len(nums)-1-i],nums[partion+1+i]
	       	#nums[partion+1] = value
		   	#else:
		    	# value = nums[len(nums)-1]
		       	
		     #   	for i in xrange(len(nums)-1,0,-1):
		     #   		nums[i]=nums[i-1]
		     #   	nums[0]=value