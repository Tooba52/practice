class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        first = list1.val
        print(first)

solution = Solution()
list1 = [1,2,4]
list2 = [1,3,5]
print(solution.mergeTwoLists(list1,list2))