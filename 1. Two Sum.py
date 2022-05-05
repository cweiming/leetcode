'''
1. Two Sum
@auth: Wei-Ming Chen, PhD
@date:
@update:
@description:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.



    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]


    Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


    Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''

import time

class Solution:
    def twoSum(nums, target):
        # target = current v + next v
        # next v = target - current v
        d = {}
        for i,v in enumerate(nums):
            if v in d:
                return [d[v],i]
            d[target-v] = i

if __name__ == '__main__':
    # Runtime: faster than 51.40% of Python3 online submissions
    # Memory Usage: less than 9.57% of Python3 online submissions

    # nums = [-1,-2,-3,-4,-5]
    # target = -8
    nums = [2,5,3,9]
    target = 7
    # nums = [0,4,3,0]
    # target = 0

    start_time = time.time()
    print("Output:", Solution.twoSum(nums, target))
    print("Runtime: %6f sec:" % (time.time() - start_time))
