'''
344. Reverse String
@auth: Wei-Ming Chen, PhD
@date: 2022/05/13
@update: 2022/05/13
@description:
    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.

    

    Example 1:

    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    Example 2:

    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
    

    Constraints:

    1 <= s.length <= 105
    s[i] is a printable ascii character.
'''

import time

class Solution:
    def reverseString(self, s) -> None:
        for i in range(0, len(s)//2+len(s)%2):
            s[i], s[-i-1] = s[-i-1], s[i]
        return s

if __name__ == '__main__':
    # Runtime: faster than 60.62% of Python3 online submissions
    # Memory Usage: less than 88.65% of Python3 online submissions

    s = ["h","e","l","l","o"]
    # Output: ["o","l","l","e","h"]

    s = ["H","a","n","n","a","h"]
    # Output: ["h","a","n","n","a","H"]

    start_time = time.time()
    print("Output:", Solution().reverseString(s))
    print("Runtime: %6f sec:" % (time.time() - start_time))
