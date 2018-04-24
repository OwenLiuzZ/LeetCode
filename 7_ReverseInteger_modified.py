class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = 1
        if x < 0:
            sign = -1
        number = abs(x)
        sum = 0
        while number != 0:
            sum = sum * 10 + number % 10
            number /= 10
        result = sign * sum
        if result > 2147483647 or result < -2147483648:
            return 0
        return sign * sum