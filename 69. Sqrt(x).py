'''
69. Sqrt(x)
@auth: Wei-Ming Chen, PhD
@date: 2022/05/14
@update: 2022/05/14
@description:
    Given a non-negative integer x, compute and return the square root of x.

    Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

    Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

    

    Example 1:

    Input: x = 4
    Output: 2
    Example 2:

    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
    

    Constraints:

    0 <= x <= 231 - 1
'''

import time

class Solution:
    def mySqrt(self, x: int) -> int:
        i = x
        while i:
            if i*i < x: break
            i //= 2
        while i:
            if i*i > x: return i-1
            i += 1
        return x

if __name__ == '__main__':
    # Runtime: faster than 18.61% of Python3 online submissions
    # Memory Usage: less than 57.63.54% of Python3 online submissions

    x = 4
    # Output: 2

    x = 8
    # Output: 2

    start_time = time.time()
    print("Output:", Solution().mySqrt(x))
    print("Runtime: %6f sec:" % (time.time() - start_time))
