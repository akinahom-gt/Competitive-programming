class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        crr = ListNode(0)
        crr.next = head

        l1  = []
        l2 = []

        while crr.next:
            l1.append(crr.next.val)
            crr = crr.next

        while head:
            l2.append(head.val)
            head = head.next

        return l1 == l2[::-1]
