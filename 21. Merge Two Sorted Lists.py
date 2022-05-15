'''
21. Merge Two Sorted Lists
@auth: Wei-Ming Chen, PhD
@date: 2022/05/14
@update: 2022/05/14
@description:
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    

    Example 1:


    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    Example 2:

    Input: list1 = [], list2 = []
    Output: []
    Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]
    

    Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
'''

import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 and not list2: return None
        if not list1: return list2
        if not list2: return list1

         # list1 as min, list2 as max
        if list1.val > list2.val: list1, list2 = list2, list1

        pre, ptr = list1, list1
        while list2:
            if not ptr or ptr.val > list2.val:
                pre.next = list2
                pre, ptr, list2 = list2, list2, ptr
            else:
                pre, ptr = ptr, ptr.next

        curr = list1
        while curr:
            print(curr.val)
            curr = curr.next if curr.next else None

        return list1


if __name__ == '__main__':
    # Runtime: faster than 76.02% of Python3 online submissions
    # Memory Usage: less than 33.02% of Python3 online submissions

    list1 = ListNode(1,ListNode(2,ListNode(4))) # [1,2,4]
    llis2 = ListNode(1,ListNode(3,ListNode(4))) # [1,3,4]
    # Output: [1,1,2,3,4,4]

    # list1 = ListNode() # []
    # llis2 = ListNode() # []
    # Output: []

    # list1 = None # []
    # llis2 = ListNode(0) # []
    # Output: []

    start_time = time.time()
    print("Output:", Solution.mergeTwoLists(list1, llis2))
    print("Runtime: %6f sec:" % (time.time() - start_time))
