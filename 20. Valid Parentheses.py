'''
20. Valid Parentheses
@auth: Wei-Ming Chen, PhD
@date: 2022/05/14
@update: 2022/05/14
@description:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    

    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "()[]{}"
    Output: true
    Example 3:

    Input: s = "(]"
    Output: false
    

    Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
'''

import time

class Solution:
    def isValid(self, s: str) -> bool:
        bk, sk = {")":"(", "}":"{", "]":"["}, []
        for v in s:
            if v in bk and sk and bk[v] == sk[-1]: sk.pop()
            else: sk.append(v)
        return sk == []

if __name__ == '__main__':
    # Runtime: faster than 81.39% of Python3 online submissions
    # Memory Usage: less than 98.19% of Python3 online submissions

    s = "((([])))"
    # Output: true

    s = "()[]{}"
    # Output: true

    s = "(]"
    # Output: false

    s = "(){}}{"
    # Output: false
    
    s = "[()[(){}]]"
    # Output: true

    # s = "[()[([){]}]]"
    # Output: false

    start_time = time.time()
    print("Output:", Solution().isValid(s))
    print("Runtime: %6f sec:" % (time.time() - start_time))
