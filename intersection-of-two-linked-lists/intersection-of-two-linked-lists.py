# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Bidirect(ListNode):
    def __init__(self, Node, prev_A=None, prev_B=None):
        super().__init__(Node.val)
        self.original = Node
        self.next = Node.next
        self.prev_A = prev_A
        self.prev_B = prev_B


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tmp_A = Bidirect(headA)
        tmp_B = Bidirect(headB)
        
        while tmp_A.next:
            tmp_A_next = Bidirect(tmp_A.next, tmp_A, None)
            tmp_A = tmp_A_next
        while tmp_B.next:
            tmp_B_next = Bidirect(tmp_B.next, None, tmp_B)
            tmp_B = tmp_B_next
        
        if tmp_A.original != tmp_B.original:
            return None
        
        while tmp_A.prev_A and tmp_B.prev_B:
            if tmp_A.prev_A.original != tmp_B.prev_B.original:
                return tmp_A.original
            tmp_A = tmp_A.prev_A
            tmp_B = tmp_B.prev_B
    
        
        return tmp_A.original