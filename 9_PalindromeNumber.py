class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x <= 9:
            return True
        else:
            reverseValue = 0
            temp = x
            while temp > 0:
                reverseValue = reverseValue*10 + temp%10
                temp = temp/10
            return reverseValue==x
