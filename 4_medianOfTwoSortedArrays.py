class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # We assume that there exists two array A[i]&B[j] with length m,n respectively.
        # This algorithm must satisfy n>=m and to find the separation of the two array,
        # We need to find i to calculate the median of two array:
        # max(A[i-1], B[j-1]) (when m + n is odd) or
        # (max(A[i-1], B[j-1]) + min(A[i], B[j]))/2 (when m + n is even)
        m = len(nums1)
        n = len(nums2)
        # Swap two array to satisfy the condition
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        i_min = 0
        i_max = m
        half_len = int((m + n + 1) / 2)

        if n == 0:
            raise ValueError

        # Use binary search to find i
        while i_min <= i_max:
            i = int((i_min + i_max)/2)
            j = half_len - i

            # Means i is too small, we must increase it.
            if i < m and nums2[j-1] > nums1[i]:
                i_min = i + 1

            # Means i is too big, must decrease it
            elif i > 0 and nums1[i-1] > nums2[j]:
                i_max = i - 1

            # Means i is perfect
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])

                if (m+n) % 2 == 1:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                if (m + n) % 2 == 0:
                    return (max_left+min_right)/2.0




solution = Solution()
num1 = [1, 2]
num2 = [1, 2]
print(solution.findMedianSortedArrays(num1,num2))



