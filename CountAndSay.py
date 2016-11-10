class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result='1'
        for x in xrange(0,n-1):
        	result = self.handle(result)
        return result
        

    def handle(self, n):
    	count = 0
        result = ''
    	for x in xrange(0,len(n)):
        	if(x==0 or n[x]==n[x-1]):
        		count += 1
        	else:
        		result += str(count*10+int(n[x-1]))
        		count = 1 
        	if(x==(len(n)-1)):
        		result += str(count*10+int(n[x]))
        return result 