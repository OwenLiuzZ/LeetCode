class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 1 or numRows == 1 or len(s) <= numRows:
            return s
        else:
            convertS = ""
            distance = 2
            for i in range(numRows):
                temp = ""
                if i == 0:
                    for j in range(len(s)) :
                        if j % (numRows - 1) == 0 and (j / (numRows - 1)) % 2 == 0:
                            temp = temp + s[j]
                    convertS = convertS + temp
                elif i == numRows-1:
                    for j in range(len(s)) :
                        if j % (numRows - 1) == 0 and (j / (numRows - 1)) % 2 == 1:
                            temp = temp + s[j]
                    convertS = convertS + temp
                else:
                    for j in range(len(s)):
                        if j >= i:
                            k = j-i
                            if (k % (numRows - 1) == 0 and (k / (numRows - 1)) % 2 == 0) or ((k+distance) % (numRows - 1) == 0 and ((k+distance) / (numRows - 1)) % 2 == 0):
                                temp = temp + s[j]
                    distance += 2
                    convertS += temp
        return convertS






# solution = Solution()
# print (solution.convert("PAYPALISHIRING",4))
numRows = 3
L = [''] * numRows
print L

