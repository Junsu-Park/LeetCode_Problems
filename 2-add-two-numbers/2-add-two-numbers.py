# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1 = deque([])
        L2 = deque([])
        while True:
            L1.appendleft(str(l1.val))
            if l1.next:
                l1 = l1.next
            else:break
        while True:
            L2.appendleft(str(l2.val))
            if l2.next:
                l2 = l2.next
            else:break
        ans = list(str(int(''.join(L1)) + int(''.join(L2))))
        tmp_node = ListNode(int(ans.pop()))
        start_node = tmp_node
        while ans:
            next_node = ListNode(int(ans.pop()))
            tmp_node.next = next_node
            tmp_node = next_node
        
        return start_node

    
    
####### Ideal Solution #######

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummyHead = ListNode(0)
#         curr = dummyHead
#         carry = 0
#         while l1 != None or l2 != None or carry != 0:
#             l1Val = l1.val if l1 else 0
#             l2Val = l2.val if l2 else 0
#             columnSum = l1Val + l2Val + carry
#             carry = columnSum // 10
#             newNode = ListNode(columnSum % 10)
#             curr.next = newNode
#             curr = newNode
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummyHead.next
