# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = 0
        # Calculate the value of the L1
        i = 0
        num1 = num1 + l1.val * 10 ** i
        while l1.next != None:
            l1 = l1.next
            i = i + 1
            num1 = num1 + l1.val * 10 ** i
        # Calculate the value of the L2
        j = 0
        num2 = num2 + l2.val * 10 ** j
        while l2.next != None:
            l2 = l2.next
            j = j + 1
            num2 = num2 + l2.val * 10 ** j
        # print num1,num2
        s = num1 + num2
        # print s
        l3 = []
        if s == 0:
            l3 = [0]

        else:
            while s > 0:
                l3.append(s % 10)
                s = s / 10
        return l3

# For test
solution = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
(l1.next).next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
(l2.next).next = ListNode(4)

l4 = solution.addTwoNumbers(l1,l2)
print (l4)