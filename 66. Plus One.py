'''
66. Plus One
@auth: Wei-Ming Chen, PhD
@date: 2022/05/15
@update: 2022/05/15
@description:
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    

    Example 1:

    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].
    Example 2:

    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4,3,2,2].
    Example 3:

    Input: digits = [9]
    Output: [1,0]
    Explanation: The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    Thus, the result should be [1,0].
    

    Constraints:

    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain any leading 0's.
'''

import time

class Solution:
    def plusOne(self, digits: int) -> int:
        carry = 1
        for i in range(1,len(digits)+1):
            sum = (digits[-i]+carry)
            carry = sum // 10
            digits[-i] = sum % 10
            if not carry: return digits
        return [1] + digits

if __name__ == '__main__':
    # Runtime: faster than 70.18% of Python3 online submissions
    # Memory Usage: less than 59.93% of Python3 online submissions


    # digits = [1,2,3]
    # Output: [1,2,4]

    # digits = [4,3,2,1]
    # Output: [4,3,2,2]

    digits = [9]
    # Output: [1,0]

    start_time = time.time()
    print("Output:", Solution().plusOne(digits))
    print("Runtime: %6f sec:" % (time.time() - start_time))
