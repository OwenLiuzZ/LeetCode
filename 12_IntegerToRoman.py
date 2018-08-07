class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if (num > 3999) and (num < 1):
            return ''
        else:
            roma_num = ''
            count = 3
            while num >= 1:
                res = num / (10**count)

                if res != 0 and count == 3:
                    roma_num += res*'M'

                if res != 0 and count == 2:
                    if res < 4:
                        roma_num += 'C' * res
                    if res == 4:
                        roma_num += 'CD'
                    if res == 5:
                        roma_num += 'D'
                    if (res > 5) and (res < 9):
                        roma_num += 'D'+'C'*(res-5)
                    if res == 9:
                        roma_num += 'CM'

                if res != 0 and count == 1:
                    if res < 4:
                        roma_num += 'X' * res
                    if res == 4:
                        roma_num += 'XL'
                    if res == 5:
                        roma_num += 'L'
                    if (res > 5) and (res < 9):
                        roma_num += 'L' + 'X' * (res - 5)
                    if res == 9:
                        roma_num += 'XC'

                if res != 0 and count == 0:
                    if res < 4:
                        roma_num += 'I' * res
                    if res == 4:
                        roma_num += 'IV'
                    if res == 5:
                        roma_num += 'V'
                    if (res > 5) and (res < 9):
                        roma_num += 'V' + 'I' * (res - 5)
                    if res == 9:
                        roma_num += 'IX'

                num -= res*(10**count)
                count -= 1
            return roma_num
solution = Solution()
print solution.intToRoman(10)