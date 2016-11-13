class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ''
        k = k-1
        n_L = 1
        for x in xrange(1,n):
            n_L = n_L*x
        used = dict.fromkeys([i for i in range(1,n+1)],0)
        for x in xrange(1,n+1):
            less = 0
            a = k/n_L+1
            for i in xrange(1,n+1):
                if(used[i]==1 and i<a+less+1):
                    less += 1
            a+=less
            used[a] = 1
            result += str(a)
            k = k%n_L
            n_L = 1 if x==n else n_L/(n-x)
            
        return result