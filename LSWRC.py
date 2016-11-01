class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chDict=[-1]*256
        start=0
        maxLen=0

        for i in xrange(len(s)):
            asc=ord(s[i])
            if chDict[asc]==-1 or chDict[asc]<start:
                chDict[asc]=i
            else:
                if maxLen<i-start:
                    maxLen=i-start
                start=chDict[asc]+1
                chDict[asc]=i

        return max(maxLen, len(s)-start)
        