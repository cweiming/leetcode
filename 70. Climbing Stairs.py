'''
70. Climbing Stairs
@auth: Wei-Ming Chen, PhD
@date: 2022/05/20
@update: 2022/05/20
@description:
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    

    Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    Example 2:

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    

    Constraints:

    1 <= n <= 45
'''

import time

class Solution:
    def climbStairs(self, n: int) -> int:
        step = n
        for i in range(2, n//2+1):
            # C(n-element, k-combination)
            ne, kc = 1, 1
            for x in range(n-i, (n-i)-i, -1): ne *= x
            for x in range(2, i+1): kc *= x
            step += ne//kc
        return step

if __name__ == '__main__':
    # Runtime: faster than 94.83% of Python3 online submissions
    # Memory Usage: less than 96.60% of Python3 online submissions
    n = 1
    # Output: 1

    n = 2
    # Output: 2

    # n = 3
    # Output: 3

    # n = 4
    # Output: 5

    # n = 5
    # Output: 8

    # n = 6
    # Output: 13

    n = 45
    # Output: 1836311903

    start_time = time.time()
    print("Output:", Solution().climbStairs(n))
    print("Runtime: %6f sec:" % (time.time() - start_time))
