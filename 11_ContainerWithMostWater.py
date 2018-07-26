class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_s = 0
        start = 0
        end = len(height) - 1
        while start < end:
            h1 = height[start]
            h2 = height[end]
            if h1 > h2:
                space = h2 * (end - start)
                if space > max_s:
                    max_s = space
                end -= 1
            else:
                space = h1 * (end - start)
                if space > max_s:
                    max_s = space
                start += 1
        return max_s

solution = Solution()
solution.maxArea([1,2,4,3])