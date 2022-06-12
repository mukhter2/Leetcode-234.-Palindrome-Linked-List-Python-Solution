class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = ListNode()
        fast= ListNode()
        slow=head
        fast=head
        fastCounter=1
        lst=[]
        while fast.next is not None:
            lst.append(slow.val)
            fast=fast.next
            fastCounter+=1
            slow=slow.next
            if fast.next is not None:
                fast=fast.next
                fastCounter+=1
        if fastCounter%2==1 and fastCounter>1:
            slow=slow.next
        while slow.next is not None:
            x=lst.pop()
            if x != slow.val:
                return False
            slow=slow.next
        if fastCounter != 1:
            x=lst.pop()
            if x != slow.val:
                return False
        return True
        
    
