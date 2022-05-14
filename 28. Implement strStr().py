'''
28. Implement strStr()
@auth: Wei-Ming Chen, PhD
@date: 2022/05/14
@update: 2022/05/14
@description:
    Implement strStr().

    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Clarification:

    What should we return when needle is an empty string? This is a great question to ask during an interview.

    For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

    

    Example 1:

    Input: haystack = "hello", needle = "ll"
    Output: 2
    Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1
    

    Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.
'''

import time

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sw = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+sw] == needle: return i
        return -1
        

if __name__ == '__main__':
    # Runtime: faster than 59.03% of Python3 online submissions
    # Memory Usage: less than 75.54% of Python3 online submissions

    haystack = "hello"
    needle = "ll"
    # Output: 2

    # haystack = "aaaaa"
    # needle = "bba"
    # Output: -1

    start_time = time.time()
    print("Output:", Solution().strStr(haystack, needle))
    print("Runtime: %6f sec:" % (time.time() - start_time))
