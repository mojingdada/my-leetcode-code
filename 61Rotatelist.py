# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        i=head
        n=1
        while(i.next!=None):
            i=i.next
            n = n + 1
        i.next=head
        i=dummy
        k=k%n
        for l in range(0,n - k):
            i=i.next
        first=i.next
        i.next=None
        return first


