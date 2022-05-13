'''
9. Palindrome Number
@auth: Wei-Ming Chen, PhD
@date: 2022/05/13
@update: 2022/05/13
@description:
    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.


    Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


    Constraints:

    -231 <= x <= 231 - 1


    Follow up: Could you solve it without converting the integer to a string?
'''

import time

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        remainder = []
        while x:
            remainder += [x % 10]
            x //= 10

        return remainder == remainder[::-1]

if __name__ == '__main__':
    # Runtime: faster than 64.55% of Python3 online submissions
    # Memory Usage: less than 61.00% of Python3 online submissions

    x = 121
    # Output: true

    # x = -121
    # Output: false

    # x = 10
    # Output: false


    start_time = time.time()
    print("Output:", Solution().isPalindrome(x))
    print("Runtime: %6f sec:" % (time.time() - start_time))
