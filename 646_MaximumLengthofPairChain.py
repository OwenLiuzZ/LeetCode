class Solution(object):
    # Time Limit Exceeded
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        maxLength = 0
        if not pairs:
            return maxLength
        else:
            pairs = sorted(pairs, key=lambda x:x[1])
            for pair in pairs[:]:
                chain = [pair]
                for i in range(len(pairs)):
                    if pairs[i][0] > chain[len(chain)-1][1]:
                        chain.append(pairs[i])
                maxLength = max(maxLength,len(chain))
            return maxLength


solution = Solution()
print solution.findLongestChain([[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]])

