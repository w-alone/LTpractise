class Solution(object):
	def maxArea(self,height):
		i = 0;
		j = len(height)-1
		maxarea = (j-i)*min(height[i],height[j])
		while i<j:
			maxarea = max(maxarea,(j-i)*min(height[i],height[j]))
			if height[i]<height[j]:
				i = i+1
			else:
				j = j-1
		return maxarea