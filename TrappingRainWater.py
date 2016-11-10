class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i , j = 0,len(height)-1
        container = 0

        while i<j:
        	if height[i] > height[i+1]:
        		break
        	else:
        		i += 1
        while i<j:
        	if height[j] > height[j-1]:
        		break
        	else:
        		j -= 1


        while i<j:
            sub_con = 0
            if height[i]<=height[j]:
                k = i+1
                while k<j and height[k]<height[i]:
                	sub_con += height[k]
                	k+=1
                container += (k-1-i)*height[i]-sub_con 
                i = k
            else:
                k = j-1
                while k>i and height[k]<height[j]:
                    sub_con += height[k]
                    k-=1
                container += (j-1-k)*height[j]-sub_con
                j = k
        	
        return container