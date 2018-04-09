class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i + 1:]:
                # Notice that the function of list.index(content, begin_index, final_index)
                return [i, nums.index(target - nums[i], i + 1, len(nums))]






