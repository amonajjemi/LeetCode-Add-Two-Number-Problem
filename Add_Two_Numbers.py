# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = None;
        carry = 0;
        while(l1 != None and l2 != None):
            current = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) / 10;
            l1 = l1.next;
            l2 = l2.next;
            if(result == None):
                result = current;
            else:
                temp = result;
                while(result.next != None):
                    result = result.next;
                result.next = current;
                result = temp;
                
        temp = result;
        while(result.next != None):
            result = result.next;
            
        while(l1 != None):
            result.next = l1;
            result = result.next;
            if(carry != 0):
                carry = (result.val + 1) / 10;
                result.val = (result.val + 1) % 10;
            l1 = l1.next;
            
        while(l2 != None):
            result.next = l2;
            result = result.next;
            if(carry != 0):
                carry = (result.val + 1) / 10;
                result.val = (result.val + 1) % 10;
            l2 = l2.next;
            
        if(l1 == None and l2 == None and carry == 1):
            result.next = ListNode(carry);
        result = temp;
        return result;
            
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """