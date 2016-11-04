#!/usr/bin/env python
class Solution(object):
	def QuickSort(self,nums,p,r):
	    	if(p<r):
	    		q = self.Partion(nums,p,r)
	    		self.QuickSort(nums,p,q-1)
	    		self.QuickSort(nums,q+1,r)


	def Partion(self,nums,p,r):
	    	key = nums[r]
	    	i = p-1
	        j = p
	        while j <= r-1:
	            if(nums[j]<=key):
	                i += 1
	                nums[i],nums[j] = nums[j],nums[i]
	            j+=1
	    	nums[i+1],nums[r] = nums[r],nums[i+1]
	    	return i+1


	def threeSumClosest(self,nums,target):
	    value = 10000000000
	    min_value = 10000000000
	    length = len(nums)
	    self.QuickSort(nums,0,len(nums)-1)
	    for i in xrange(0,length):
	    	#if (i==0 or nums[i]!=nums[i-1]):
		        j = i+1
		        k = length-1
		        while j<k:
		        	if abs(nums[i]+nums[j]+nums[k]-target) < value:
		        		value = abs(nums[i]+nums[j]+nums[k]-target)
		        		min_value = nums[i]+nums[j]+nums[k]
		        		#while nums[j]==nums[j+1] and j+1<length-1:
		        			#j += 1
		        		#while nums[k]==nums[k-1] and k-1 > i:
		        			#k -= 1
		        		#j += 1
		        		#k -= 1
		        	elif nums[i]+nums[j]+nums[k] > target: #or (target < 0 and nums[i]+nums[j]+nums[k] < target):
		        		k -= 1
		        	else:
		        		j += 1	
	    return min_value

