class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.findMid(head) # calling the findMid function
        midNext = mid.next # assigning to midnext
        mid.next = None # assigning next pointer of mid to null
        headB = self.reverse(midNext) # calling the reverse function
        headA = head
        self.mergeLinkedLists(headA,headB) # calling the mergeLinkedLists function
        
    def findMid(self,head): 
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None: # run until fast.next and fast.next.next not equal to none
            slow = slow.next # incrementing 1 node
            fast = fast.next.next # incrementing 2 nodes

        return slow # returning slow

    def reverse(self,head):
        prev = None # initializing prev 
        curr = head # initializing curr to head

        while curr: # run until curr not equal to null
            temp = curr.next # setting temp to curr.next
            curr.next = prev # changing pointer to prev
            prev = curr # assigning curr to prev
            curr = temp # assigning temp to curr

        return prev # returning prev

    def mergeLinkedLists(self,head1,head2):
        p1 = head1 
        p2 = head2
        while p2: # run until p2 is not null
            temp = p1.next # assigning p1 next to temp
            p1.next = p2 # assigning p1 next pointer to p2
            p2 = p2.next # incrementing pointer
            p1.next.next = temp # assigning p1.next.next to temp
            p1 = temp # assigning temp to p1