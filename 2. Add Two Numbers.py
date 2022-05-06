'''
2. Add Two Numbers
@auth: Wei-Ming Chen, PhD
@date: 2022/05/06
@update: 2022/05/06
@description:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''

import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(l1, l2):
        b1, b2 = [l1.val], [l2.val]
        while l1.next is not None:
            l1 = l1.next
            b1.append(l1.val)
        while l2.next is not None:
            l2 = l2.next
            b2.append(l2.val)

        b1_len, b2_len = len(b1), len(b2)
        if b1_len > b2_len:
            b2 += [0 for x in range(b1_len-b2_len)]
        if b2_len > b1_len:
            b1 += [0 for x in range(b2_len-b1_len)]
        b3 = [[b1.pop(),b2.pop()] for i in range(len(b1))]

        sv = 0; # stored value
        l3 = ListNode(next = ListNode())
        tmp = l3.next
        i = 0;

        while b3:
            v1,v2 = b3.pop()
            if v1+v2+sv <= 9:
                tmp.val = v1+v2+sv
                sv = 0
            if v1+v2+sv >= 10:
                tmp.val = v1+v2+sv-10
                sv = 1
            if b3:
                tmp.next = ListNode()
                tmp = tmp.next
                i += 1

        if sv: tmp.next = ListNode(sv)

        a = []
        l3 = l3.next
        while l3.next is not None:
            a += [l3.val]
            l3 = l3.next
        print(a + [l3.val])

        return l3.next

if __name__ == '__main__':
    # Runtime: faster than 43.55% of Python3 online submissions
    # Memory Usage: less than 10.51% of Python3 online submissions

    # l1 = ListNode(2,ListNode(4,ListNode(3,None))) # [2,4,3]
    # l2 = ListNode(5,ListNode(6,ListNode(4))) # [5,6,4]

    # l1 = ListNode(0) # [0]
    # l2 = ListNode(0) # [0]

    # l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))) #[9,9,9,9,9,9,9]
    # l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9)))) #[9,9,9,9]
    # l1 = [9,9,9,9,9,9,9]
    # l2 = [9,9,9,9]

    # l1 = ListNode(2,ListNode(4,ListNode(9))) # [2,4,9]
    # l2 = ListNode(5,ListNode(6,ListNode(4,ListNode(9)))) # [5,6,4,9]

    start_time = time.time()
    print("Output:", Solution.addTwoNumbers(l1, l2))
    print("Runtime: %6f sec:" % (time.time() - start_time))
