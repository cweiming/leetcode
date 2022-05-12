'''
5. Longest Palindromic Substring
@auth: Wei-Ming Chen, PhD
@date: 2022/05/11
@update: 2022/05/11
@description:

    Given a string s, return the longest palindromic substring in s.

    Example 1:

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
    Example 2:

    Input: s = "cbbd"
    Output: "bb"


    Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
'''

import time

class Solution:
    def longestPalindrome(s):
        lps = s[0]
        for c in set(s):
            ci = [i for i,v in enumerate(s) if v == c]
            if len(ci) <= 1: continue

            if len(set(s[ci[0]:ci[-1]+1])) == 1:
                if len(s[ci[0]:ci[-1]+1]) > len(lps): lps = s[ci[0]:ci[-1]+1]
                continue

            for i in range(0,len(ci)):
                for j in range(i+1,len(ci)):
                    ps, ps_len = s[ci[i]:ci[j]+1], ci[j]-ci[i]+1
                    # print(ps_len, ci[i], ci[j], ps)
                    chk = ps[:-(ps_len//2)-(ps_len%2)] == ps[-(ps_len//2):][::-1]
                    if chk and len(ps) > len(lps): lps = ps

        return lps

    # def longestPalindrome(s):
    #     paired = {}
    #     for r,v1 in enumerate(s):
    #         for c,v2 in enumerate(s):
    #             if v1 == v2: paired[(r,c)] = 1

    #     lps = s[0]
    #     for k in paired.keys():
    #         ps, queue = "", [k]
    #         while queue:
    #             r,c = queue.pop()
    #             paired[(r,c)] = 0
    #             ps += s[r]
    #             for dr,dc in [[1,-1],[-1,1]]:
    #                 if (r+dr,c+dc) in paired and paired[(r+dr,c+dc)]:
    #                     queue.append((r+dr,c+dc))
    #         if len(ps) % 2:
    #             ps_check = ps[:-(len(ps)//2)-1] == ps[-(len(ps)//2):][::-1]
    #         else:
    #             ps_check = ps[:-(len(ps)//2)] == ps[-(len(ps)//2):][::-1]
    #         if ps_check and len(ps) > len(lps): lps = ps

    #     return lps

    # def longestPalindrome(s):
    #     #print(s, list(range(len(s))[1:-1]))
    #     lps = ""
    #     for i in range(len(s))[1:-1]:
    #         q = [[i-1, i+1]]
    #         while q:
    #             x,y = q.pop()
    #             #print("bb", x,y)
    #             if s[x] == s[y]: lps = s[x:y+1]
    #             if x-1 >=0 and y+1 < len(s): q.append([x-1,y+1])
    #             #print("cc", [x-1,y+1], lps)

    #     return lps

if __name__ == '__main__':
    # Runtime: faster than 28.17% of Python3 online submissions
    # Memory Usage: less than 62.18% of Python3 online submissions

    # s = "babad"
    # Output: bab

    # s = "cbbd"
    # Output: bb

    # s = "bb"
    # Output: bb

    # s = "ac"
    # Output: a

    # s = "b"
    # Output: b

    # s = "aaaa"
    # Output: aaaa

    # s = "abbcccbbbcaaccbababcbcabca"
    # Output: "bbcccbb"

    # s = "xaabacxcabaaxcabaax"
    # Output: "xaabacxcabaax"

    # s = "aacabdkacaa"
    # Output: "aca"

    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # Output: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    start_time = time.time()
    print("Output:", Solution.longestPalindrome(s))
    print("Runtime: %6f sec:" % (time.time() - start_time))
