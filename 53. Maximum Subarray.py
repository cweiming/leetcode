'''
53. Maximum Subarray
@auth: Wei-Ming Chen, PhD
@date: 2022/05/21
@update: 2022/05/21
@description:
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    A subarray is a contiguous part of an array.

    

    Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    Example 2:

    Input: nums = [1]
    Output: 1
    Example 3:

    Input: nums = [5,4,-1,7,8]
    Output: 23
    

    Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    

    Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

import time

class Solution:
    def maxSubArray(self, nums) -> int:
        curr, mx = 0, nums[0]
        for n in nums:
            curr = n if curr < 0 else curr+n
            mx = max(curr, mx)
        return mx

if __name__ == '__main__':
    # Runtime: faster than 87.29% of Python3 online submissions
    # Memory Usage: less than 99.75% of Python3 online submissions

    nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
    # Output: 6

    # nums = [1]
    # Output: 1

    # nums = [5,4,-1,7,8]
    # Output: 23

    # nums = [1, -1, 1]
    # Output: 1

    # nums = [1,2,-1,-2,2,1,-2,1]
    # Output: 3

    # nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
    # Output: 6

    start_time = time.time()
    print("Output:", Solution().maxSubArray(nums))
    print("Runtime: %6f sec:" % (time.time() - start_time))
