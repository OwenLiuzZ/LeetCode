class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return len(s)
        else:
            res = ''
            for i in range(len(s)):
                temp = s[i]
                for j in range((i + 1), len(s)):
                    if s[j] not in temp:
                        temp = temp + s[j]
                    else:
                        break
                if len(res) < len(temp):
                    res = temp
            return len(res)
