'''
2. Add Two Numbers
@auth: Wei-Ming Chen, PhD
@date: 2022/05/06
@update: 2022/05/09
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
        sv = 0; # stored value
        curr = ListNode(next = ListNode())
        ptr = curr.next
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            if v1+v2+sv <= 9:
                ptr.val = v1+v2+sv
                sv = 0
            if v1+v2+sv >= 10:
                ptr.val = v1+v2+sv-10
                sv = 1

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2:
                ptr.next = ListNode()
                ptr = ptr.next
            else:
                break
        if sv: ptr.next = ListNode(sv)

        return curr.next


if __name__ == '__main__':
    # Runtime: faster than 70.12% of Python3 online submissions
    # Memory Usage: less than 99.44% of Python3 online submissions

    # l1 = ListNode(2,ListNode(4,ListNode(3,None))) # [2,4,3]
    # l2 = ListNode(5,ListNode(6,ListNode(4))) # [5,6,4]
    # output [7, 0, 8]

    # l1 = ListNode(0) # [0]
    # l2 = ListNode(0) # [0]
    # output [0]

    # l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))) #[9,9,9,9,9,9,9]
    # l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9)))) #[9,9,9,9]
    # output [8, 9, 9, 9, 0, 0, 0, 1]

    l1 = ListNode(2,ListNode(4,ListNode(9))) # [2,4,9]
    l2 = ListNode(5,ListNode(6,ListNode(4,ListNode(9)))) # [5,6,4,9]
    # output [7,0,4,0,1]

    start_time = time.time()
    print("Output:", Solution.addTwoNumbers(l1, l2))
    print("Runtime: %6f sec:" % (time.time() - start_time))
