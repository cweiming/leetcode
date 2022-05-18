'''
88. Merge Sorted Array
@auth: Wei-Ming Chen, PhD
@date: 2022/05/18
@update: 2022/05/18
@description:
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



    Example 1:

    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    Example 2:

    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].
    Example 3:

    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


    Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109


    Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''

import time

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        l,i,j = m+n, m-1, n-1
        while j >= 0 and i < l:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[i], nums1[i+1] = nums2[j], nums1[i]
                i -= 1
                continue
            if i+1 >= m: nums1[i+1] = nums2[j]
            i,j = l-j-1, j-1
        return nums1

if __name__ == '__main__':
    # Runtime: faster than 48.50% of Python3 online submissions
    # Memory Usage: less than 86.26% of Python3 online submissions

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    # Output: [1,2,2,3,5,6]

    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0
    # # Output: [1]

    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1
    # # Output: [1]

    # nums1 = [2,0]
    # m = 1
    # nums2 = [1]
    # n = 1
    # # Output: [1,2]

    # nums1 = [4,5,6,0,0,0]
    # m = 3
    # nums2 = [1,2,3]
    # n = 3
    # # Output: [1,2,3,4,5,6]

    # nums1 = [1,2,3,4,5,6]
    # m = 5
    # nums2 = [6]
    # n = 1
    # # Output: [1,2,3,4,5,6]

    nums1 = [0,0,0,0,0]
    m = 0
    nums2 = [1,2,3,4,5]
    n = 5
    # Output: [1,2,3,4,5,6]

    start_time = time.time()
    print("Output:", Solution().merge(nums1, m, nums2, n))
    print("Runtime: %6f sec:" % (time.time() - start_time))
