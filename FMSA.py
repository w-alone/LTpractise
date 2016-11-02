class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i , j = 0 , 0
        while i < len(nums1) and j < len(nums2):
        	if nums1[i] >= nums2[j]:
        		nums1.insert(i,nums2[j])
        		j += 1
        	i += 1
        if j < len(nums2):
        	nums1.extend(nums2[j:len(nums2)])
        print nums1
        if len(nums1)%2==0:
        	print nums1[len(nums1)>>1],nums1[(len(nums1)>>1)-1]
        	return float((nums1[len(nums1)>>1]+nums1[(len(nums1)>>1)-1]))/2
        else:
        	return nums1[(len(nums1)>>1)]