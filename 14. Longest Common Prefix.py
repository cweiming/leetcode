'''
14. Longest Common Prefix
@auth: Wei-Ming Chen, PhD
@date: 2022/05/13
@update: 2022/05/13
@description:
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.


    Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.
'''

import time

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        minstep = [len(str) for str in strs]
        minstep = min(minstep) if any(minstep) else 0
        prefix, str = "", strs.pop()

        for i,v in enumerate(str):
            for s in strs:
                if minstep and v == s[i]: v = s[i]
                else: minstep = 0
            if minstep: prefix += v
            else: break
            minstep -= 1

        return prefix

if __name__ == '__main__':
    # Runtime: faster than 85.36% of Python3 online submissions
    # Memory Usage: less than 50.80% of Python3 online submissions

    strs = ["flower","flow","flight"]
    # # Output: "fl"

    strs = ["dog","racecar","car"]
    # # Output: ""

    strs = ["","b"]
    # # Output: ""

    strs = ["aaa","aa","aaa"]
    # # Output: ""

    strs = [""]
    # # Output: ""

    strs = ["a"]
    # Output: "a"

    start_time = time.time()
    print("Output:", Solution().longestCommonPrefix(strs))
    print("Runtime: %6f sec:" % (time.time() - start_time))
