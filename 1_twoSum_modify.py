class Solution(object):

    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

# For test
solution = Solution()
print solution.twoSum([2, 5, 7, 10], 12)
