'''
3. Longest Substring Without Repeating Characters
@auth: Wei-Ming Chen, PhD
@date: 2022/05/09
@update: 2022/05/10
@description:

    Given a string s, find the length of the longest substring without repeating characters.



    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


    Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

'''

import time

class Solution:
    def lengthOfLongestSubstring(s):
        ws, i = 3, 0
        if len(s) <= ws or len(set(s)) < ws: return len(set(s))
        while True:
            # print(i, ws, s[i:i+ws+1])
            if len(set(s[i:i+ws+1])) > ws: ws += 1
            elif i+1 == len(s): break
            else: i += 1
        return ws

if __name__ == '__main__':
    # Runtime: faster than 24.17.01% of Python3 online submissions
    # Memory Usage: less than 93.74% of Python3 online submissions

    # s = "abcabcbb"
    # Output: 3

    # s = "bbbbb"
    # Output: 1

    # s = "pwwkew"
    # Output: 3

    s = "arbsxtcgatcxyatcaxyzdxbegxd"
    Output: 8

    start_time = time.time()
    print("Output:", Solution.lengthOfLongestSubstring(s))
    print("Runtime: %6f sec:" % (time.time() - start_time))
