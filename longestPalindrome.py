class Solution(object):
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        Ma = ''
        Max = 0
        Id = 0
        if(s == '' or len(s)==1):
            return s
        for i in s:
            Ma += '!'+i
        Ma += '!'
        Mp = [0]*len(Ma)
        for i in xrange(0,len(Ma)):
            
            Mp[i] = min(Mp[2*Id-i],Max-i) if(Max>i) else 1
            
            while(Mp[i]+i<=len(Ma)-1 and i-Mp[i]>=0):
                if(Ma[Mp[i]+i] == Ma[i-Mp[i]]):
                    Mp[i] += 1
                else:
                    break
            if(Mp[i]+i>Max):
                Max = Mp[i]+i
                Id = i
        Id = Mp.index(max(Mp))
        if(Id%2 == 0):
            Id = Id / 2
            Max = (max(Mp)-1)/2
            return s[Id-Max:Id]+s[Id:Id+Max]
        else:
            Id = (Id-1)/2
            Max = (max(Mp)-1)/2
            return s[Id-Max:Id]+s[Id:Id+Max+1]