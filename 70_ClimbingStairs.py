class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        else:
            first = 1
            second = 2
            while n > 2:
                third = first + second
                first = second
                second = third
                n = n-1
            return third

solution = Solution()
print solution.climbStairs(3)
