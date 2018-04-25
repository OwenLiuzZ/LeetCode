class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        valueList = []
        sign = 1
        sum = 0
        if len(str) == 0:
            return 0
        if str[0] == '-':
            sign = -1
            str = str[1:len(str) + 1]
        elif str[0] == '+':
            sign = 1
            str = str[1:len(str) + 1]
        for s in str:
            if ord(s)-ord('0') >= 0 and ord(s)-ord('0') <= 9 :
                valueList.append(ord(s)-ord('0'))
            else:
                break
        if len(valueList) == 0:
            return 0
        else:
            valueList = valueList[::-1]
            for i in range(len(valueList)):
                sum += valueList[i]*(10**i)
            if sum*sign < -2147483648:
                return -2147483648
            elif sum*sign > 2147483647:
                return 2147483647
            else:
                return sum*sign

solution = Solution()
print solution.myAtoi('12l')
