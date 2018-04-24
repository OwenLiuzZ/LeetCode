class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x >= - 2**31) and (x <= 2**31-1):
            L = []
            reverseInt = 0
            if x >= 0:
                while x > 0:
                    L.append(x % (10**1))
                    x = x / (10**1)
                L = L[::-1]
                for i in range(len(L)):
                    reverseInt += L[i] * (10**i)
                if reverseInt >= -2**31 and reverseInt <= 2**31-1:
                    return reverseInt
                else:
                    return 0
            else:
                x = -x
                while x > 0:
                    L.append(x % (10 ** 1))
                    x = x / (10 ** 1)
                L = L[:: -1]
                for i in range(len(L)):
                    reverseInt += L[i] * (10 ** i)
                if reverseInt >= -2 ** 32 and reverseInt <= 2 ** 31 - 1:
                    return -reverseInt
                else:
                    return 0
        else:
            return 0

solution= Solution()
print solution.reverse(1534236469)

